#!/usr/bin/env python3
"""Orchestrateur V1 pour les task packs du framework."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
FRAMEWORK_ROOT = Path(__file__).resolve().parent
STATE_ROOT = FRAMEWORK_ROOT / ".orchestrator-state"
RUNS_ROOT = STATE_ROOT / "runs"
ISSUE_STATUS_LABELS = {"todo", "in-progress", "blocked"}
TASK_PACK_STATUSES = {"draft", "ready", "running", "review", "done", "blocked"}
ALLOWED_AGENTS = {"claude", "codex", "copilot"}
REQUIRED_SECTIONS = {
    "statut",
    "agent cible",
    "type de travail",
    "issue github liee",
    "source de verite",
    "objectif",
    "livrable attendu",
    "fichiers a lire",
    "fichiers a ne pas toucher",
    "contraintes",
    "verification attendue",
    "definition de fin",
    "sortie courte a produire",
}


@dataclass
class Section:
    heading: str
    start_line: int
    end_line: int
    content: str


@dataclass
class TaskPack:
    path: Path
    title: str
    sections: dict[str, Section]

    def get(self, name: str) -> str:
        section = self.sections.get(name)
        return "" if section is None else section.content.strip()

    @property
    def status(self) -> str:
        return self.get("statut").strip().lower()

    @property
    def agent(self) -> str:
        return self.get("agent cible").strip().lower()

    @property
    def work_type(self) -> str:
        return self.get("type de travail").strip()

    @property
    def issue(self) -> str:
        return self.get("issue github liee").strip()


def normalize_heading(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def parse_markdown_task_pack(path: Path) -> TaskPack:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    title = ""
    sections: dict[str, Section] = {}
    current_heading: str | None = None
    current_start: int | None = None

    for index, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            continue

        if line.startswith("## "):
            if current_heading is not None and current_start is not None:
                content = "".join(lines[current_start:index]).strip()
                sections[current_heading] = Section(
                    heading=current_heading,
                    start_line=current_start,
                    end_line=index,
                    content=content,
                )
            current_heading = normalize_heading(line[3:])
            current_start = index + 1

    if current_heading is not None and current_start is not None:
        content = "".join(lines[current_start:]).strip()
        sections[current_heading] = Section(
            heading=current_heading,
            start_line=current_start,
            end_line=len(lines),
            content=content,
        )

    if not title:
        raise ValueError(f"{path}: missing H1 title")

    return TaskPack(path=path, title=title, sections=sections)


def parse_list(content: str) -> list[str]:
    if not content:
        return []

    stripped = content.strip()
    if stripped.lower() in {"aucun", "none", "n/a"}:
        return []

    items: list[str] = []
    for raw_line in stripped.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"^\d+\.\s+", "", line)
        items.append(line.strip())
    return items


def resolve_repo_path(task_pack: TaskPack, value: str) -> Path | None:
    candidate = Path(value)
    if candidate.is_absolute():
        return candidate if candidate.exists() else None

    root_relative = (REPO_ROOT / candidate).resolve()
    if root_relative.exists():
        return root_relative

    pack_relative = (task_pack.path.parent / candidate).resolve()
    if pack_relative.exists():
        return pack_relative

    return None


def path_label(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def extract_issue_number(issue_ref: str) -> str | None:
    text = issue_ref.strip()
    if not text:
        return None

    if re.fullmatch(r"#\d+", text):
        return text[1:]

    if re.fullmatch(r"\d+", text):
        return text

    match = re.search(r"/issues/(\d+)$", text)
    if match:
        return match.group(1)

    return None


def validate_task_pack(task_pack: TaskPack) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    missing_sections = sorted(REQUIRED_SECTIONS - set(task_pack.sections))
    if missing_sections:
        errors.append(
            "Missing sections: " + ", ".join(missing_sections)
        )

    if task_pack.status and task_pack.status not in TASK_PACK_STATUSES:
        errors.append(f"Invalid status '{task_pack.status}'")

    if task_pack.agent and task_pack.agent not in ALLOWED_AGENTS:
        errors.append(f"Invalid agent '{task_pack.agent}'")

    if task_pack.status in {"ready", "running", "review", "done", "blocked"}:
        if not extract_issue_number(task_pack.issue):
            errors.append("An issue reference is required outside draft status")

    if not task_pack.get("objectif"):
        errors.append("Section 'Objectif' must not be empty")
    if not task_pack.get("livrable attendu"):
        errors.append("Section 'Livrable attendu' must not be empty")
    elif len(task_pack.get("livrable attendu").split()) < 15:
        warnings.append(
            "Section 'Livrable attendu' is very short; under-specified deliverables increase drift risk"
        )
    if not task_pack.get("contraintes"):
        errors.append("Section 'Contraintes' must not be empty")
    if not task_pack.get("verification attendue"):
        errors.append("Section 'Verification attendue' must not be empty")
    if not task_pack.get("definition de fin"):
        errors.append("Section 'Definition de fin' must not be empty")
    if not task_pack.get("sortie courte a produire"):
        errors.append("Section 'Sortie courte a produire' must not be empty")

    source_files = parse_list(task_pack.get("source de verite"))
    read_files = parse_list(task_pack.get("fichiers a lire"))
    untouched_files = parse_list(task_pack.get("fichiers a ne pas toucher"))

    if not source_files:
        errors.append("At least one source of truth is required")
    if not read_files:
        errors.append("At least one file to read is required")

    if len(read_files) > 8:
        warnings.append(
            f"{len(read_files)} files to read listed; split the task pack if possible"
        )
    if len(source_files) > 3:
        warnings.append(
            f"{len(source_files)} source files listed; keep the source of truth tighter"
        )

    resolved_sources = []
    for label, values in (
        ("Source de verite", source_files),
        ("Fichiers a lire", read_files),
        ("Fichiers a ne pas toucher", untouched_files),
    ):
        for value in values:
            resolved = resolve_repo_path(task_pack, value)
            if resolved is None:
                errors.append(f"{label}: path does not exist -> {value}")
            else:
                if label == "Source de verite":
                    resolved_sources.append(resolved)

    resolved_reads = {
        resolve_repo_path(task_pack, value)
        for value in read_files
        if resolve_repo_path(task_pack, value) is not None
    }
    for source in resolved_sources:
        if source not in resolved_reads:
            warnings.append(
                f"Source of truth not listed in read files -> {path_label(source)}"
            )

    return errors, warnings


def build_handoff(task_pack: TaskPack) -> str:
    source_files = parse_list(task_pack.get("source de verite"))
    read_files = parse_list(task_pack.get("fichiers a lire"))
    untouched_files = parse_list(task_pack.get("fichiers a ne pas toucher"))

    def block(title: str, content: str | Iterable[str]) -> str:
        if isinstance(content, str):
            body = content.strip()
        else:
            items = [f"- {item}" for item in content]
            body = "\n".join(items) if items else "- aucun"
        return f"{title}\n{body}".strip()

    parts = [
        f"Task pack: {task_pack.title}",
        f"Agent cible: {task_pack.agent}",
        f"Type de travail: {task_pack.work_type}",
        f"Issue GitHub: {task_pack.issue or 'non liee'}",
        "",
        "Traite cette demande dans le cadre du framework-refonte-drupal-ia.",
        "Regles anti-derive obligatoires :",
        "- N'invente rien silencieusement. Marque explicitement : fait observe | hypothese | decision a prendre | risque.",
        "- Si une ambiguite n'est pas resolue par les sources de verite listees : marque-la 'decision a prendre' et stoppe sur ce point. Ne tranche pas a la place de l'humain.",
        "- Ne cree pas de nouveau fichier source de verite (ADR, brief, page spec). Si tu juges qu'un ADR est necessaire, signale-le dans 'questions ouvertes' sans le rediger.",
        "- Ne touche pas aux fichiers listes dans 'Fichiers a ne pas toucher', meme pour corriger une coquille.",
        "- Le perimetre de ce pack est ferme. Toute extension de perimetre doit etre signalee comme 'decision a prendre', pas implementee.",
        "",
        block("Objectif", task_pack.get("objectif")),
        "",
        block("Livrable attendu", task_pack.get("livrable attendu")),
        "",
        block("Sources de verite", source_files),
        "",
        block("Fichiers a lire", read_files),
        "",
        block("Fichiers a ne pas toucher", untouched_files),
        "",
        block("Contraintes", task_pack.get("contraintes")),
        "",
        *(
            [block("En cas de blocage ou d'ambiguite", task_pack.get("en cas de blocage ou d'ambiguite")), ""]
            if task_pack.get("en cas de blocage ou d'ambiguite") else []
        ),
        block("Verification attendue", task_pack.get("verification attendue")),
        "",
        block("Definition de fin", task_pack.get("definition de fin")),
        "",
        "Format de sortie obligatoire",
        "1. faits confirms",
        "2. propositions",
        "3. questions ouvertes",
        "4. fichiers modifies",
        "",
        block("Sortie courte a produire", task_pack.get("sortie courte a produire")),
    ]
    return "\n".join(parts).strip() + "\n"


def ensure_state_dirs() -> None:
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)


def slugify(value: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return normalized or "task-pack"


def update_status_in_file(task_pack: TaskPack, new_status: str) -> None:
    section = task_pack.sections.get("statut")
    if section is None:
        raise ValueError("Task pack has no 'Statut' section")

    lines = task_pack.path.read_text(encoding="utf-8").splitlines(keepends=True)
    replacement = [f"{new_status}\n", "\n"]
    lines[section.start_line:section.end_line] = replacement
    task_pack.path.write_text("".join(lines), encoding="utf-8")


def latest_run_for_pack(task_pack: TaskPack) -> Path | None:
    if not RUNS_ROOT.exists():
        return None

    candidates = sorted(RUNS_ROOT.glob("*/metadata.json"))
    matching: list[Path] = []
    for candidate in candidates:
        try:
            payload = json.loads(candidate.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if payload.get("task_pack") == path_label(task_pack.path):
            matching.append(candidate)
    return matching[-1] if matching else None


def build_issue_comment(task_pack: TaskPack) -> str:
    latest_run = latest_run_for_pack(task_pack)
    run_note = "Pas encore de run enregistre."
    if latest_run is not None:
        payload = json.loads(latest_run.read_text(encoding="utf-8"))
        run_note = (
            f"Run `{payload['run_id']}` sur agent `{payload['agent']}` -> "
            f"statut `{payload['final_status']}`."
        )

    read_files = parse_list(task_pack.get("fichiers a lire"))
    return "\n".join(
        [
            f"## Sync task pack - {task_pack.title}",
            "",
            f"- statut task pack : `{task_pack.status}`",
            f"- agent cible : `{task_pack.agent}`",
            f"- issue liee : `{task_pack.issue or 'non renseignee'}`",
            f"- lecture ciblee : {', '.join(read_files) if read_files else 'aucune'}",
            "",
            run_note,
            "",
            "### Sortie courte attendue",
            task_pack.get("sortie courte a produire"),
            "",
            "### Definition de fin",
            task_pack.get("definition de fin"),
        ]
    ).strip() + "\n"


def run_validate(args: argparse.Namespace) -> int:
    task_pack = parse_markdown_task_pack(args.task_pack)
    errors, warnings = validate_task_pack(task_pack)

    if warnings:
        for warning in warnings:
            print(f"WARN: {warning}", file=sys.stderr)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {task_pack.path}")
    return 0


def run_render(args: argparse.Namespace) -> int:
    task_pack = parse_markdown_task_pack(args.task_pack)
    errors, warnings = validate_task_pack(task_pack)
    if errors and not args.allow_invalid:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"WARN: {warning}", file=sys.stderr)
    sys.stdout.write(build_handoff(task_pack))
    return 0


def run_dispatch(args: argparse.Namespace) -> int:
    task_pack = parse_markdown_task_pack(args.task_pack)
    errors, warnings = validate_task_pack(task_pack)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"WARN: {warning}", file=sys.stderr)

    if task_pack.status not in {"ready", "review"}:
        print(
            f"ERROR: dispatch requires status ready or review, got '{task_pack.status}'",
            file=sys.stderr,
        )
        return 1

    handoff = build_handoff(task_pack)
    command = os.getenv(f"LILLE_ULM_ORCH_{task_pack.agent.upper()}_CMD", "").strip()
    if not args.dry_run and not command:
        print(
            f"ERROR: no command configured for agent '{task_pack.agent}'. "
            f"Set LILLE_ULM_ORCH_{task_pack.agent.upper()}_CMD or use --dry-run.",
            file=sys.stderr,
        )
        return 1

    ensure_state_dirs()
    timestamp = dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"{timestamp}-{slugify(task_pack.title)}"
    run_dir = RUNS_ROOT / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    prompt_path = run_dir / "prompt.txt"
    prompt_path.write_text(handoff, encoding="utf-8")

    metadata = {
        "run_id": run_id,
        "task_pack": path_label(task_pack.path),
        "agent": task_pack.agent,
        "issue": task_pack.issue,
        "status_before": task_pack.status,
        "dry_run": bool(args.dry_run),
        "command": command or None,
        "prompt_file": str(prompt_path.relative_to(REPO_ROOT)),
        "created_at": timestamp,
    }

    if args.dry_run:
        metadata["final_status"] = task_pack.status
        (run_dir / "metadata.json").write_text(
            json.dumps(metadata, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
        sys.stdout.write(handoff)
        return 0

    update_status_in_file(task_pack, "running")
    task_pack = parse_markdown_task_pack(task_pack.path)

    try:
        completed = subprocess.run(
            shlex.split(command),
            input=handoff,
            text=True,
            capture_output=True,
            cwd=REPO_ROOT,
            timeout=args.timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        update_status_in_file(task_pack, "blocked")
        metadata["final_status"] = "blocked"
        metadata["timeout"] = args.timeout
        (run_dir / "stdout.txt").write_text(exc.stdout or "", encoding="utf-8")
        (run_dir / "stderr.txt").write_text(exc.stderr or "", encoding="utf-8")
        (run_dir / "metadata.json").write_text(
            json.dumps(metadata, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
        print(f"ERROR: dispatch timed out after {args.timeout}s", file=sys.stderr)
        return 1

    (run_dir / "stdout.txt").write_text(completed.stdout, encoding="utf-8")
    (run_dir / "stderr.txt").write_text(completed.stderr, encoding="utf-8")
    metadata["returncode"] = completed.returncode
    if completed.returncode == 0:
        update_status_in_file(task_pack, "review")
        metadata["final_status"] = "review"
    else:
        update_status_in_file(task_pack, "blocked")
        metadata["final_status"] = "blocked"

    (run_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    sys.stdout.write(completed.stdout)
    if completed.stderr:
        print(completed.stderr, file=sys.stderr, end="")
    return completed.returncode


def run_set_status(args: argparse.Namespace) -> int:
    if args.status not in TASK_PACK_STATUSES:
        print(f"ERROR: invalid status '{args.status}'", file=sys.stderr)
        return 1

    task_pack = parse_markdown_task_pack(args.task_pack)
    update_status_in_file(task_pack, args.status)
    print(f"OK: {task_pack.path} -> {args.status}")
    return 0


def gh_issue_label_for_task_status(status: str) -> str:
    if status == "blocked":
        return "blocked"
    if status in {"running", "review", "done"}:
        return "in-progress"
    return "todo"


def run_sync_issue(args: argparse.Namespace) -> int:
    task_pack = parse_markdown_task_pack(args.task_pack)
    issue_number = extract_issue_number(task_pack.issue)
    if issue_number is None:
        print("ERROR: task pack has no usable issue reference", file=sys.stderr)
        return 1

    ensure_state_dirs()
    comment_body = build_issue_comment(task_pack)
    comment_path = STATE_ROOT / "issue-comment.md"
    comment_path.write_text(comment_body, encoding="utf-8")

    target_label = gh_issue_label_for_task_status(task_pack.status)
    edit_command = [
        "gh",
        "issue",
        "edit",
        issue_number,
    ]
    for label in sorted(ISSUE_STATUS_LABELS):
        edit_command.extend(["--remove-label", label])
    edit_command.extend(["--add-label", target_label])
    comment_command = [
        "gh",
        "issue",
        "comment",
        issue_number,
        "--body-file",
        str(comment_path),
    ]

    if args.dry_run:
        print("DRY-RUN:")
        print(" ".join(shlex.quote(part) for part in edit_command))
        print(" ".join(shlex.quote(part) for part in comment_command))
        print()
        print(comment_body, end="")
        return 0

    edited = subprocess.run(
        edit_command,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if edited.returncode != 0:
        print(edited.stderr, file=sys.stderr, end="")
        return edited.returncode

    commented = subprocess.run(
        comment_command,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if commented.returncode != 0:
        print(commented.stderr, file=sys.stderr, end="")
        return commented.returncode

    print(f"OK: issue #{issue_number} synchronized")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Orchestrateur V1 pour task packs")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate a task pack")
    validate_parser.add_argument("task_pack", type=Path)
    validate_parser.set_defaults(func=run_validate)

    render_parser = subparsers.add_parser("render", help="Render the handoff prompt")
    render_parser.add_argument("task_pack", type=Path)
    render_parser.add_argument(
        "--allow-invalid",
        action="store_true",
        help="Render even if validation fails",
    )
    render_parser.set_defaults(func=run_render)

    dispatch_parser = subparsers.add_parser("dispatch", help="Dispatch a task pack")
    dispatch_parser.add_argument("task_pack", type=Path)
    dispatch_parser.add_argument("--dry-run", action="store_true")
    dispatch_parser.add_argument("--timeout", type=int, default=900)
    dispatch_parser.set_defaults(func=run_dispatch)

    status_parser = subparsers.add_parser("set-status", help="Update task pack status")
    status_parser.add_argument("task_pack", type=Path)
    status_parser.add_argument("status")
    status_parser.set_defaults(func=run_set_status)

    sync_parser = subparsers.add_parser("sync-issue", help="Sync task pack to GitHub")
    sync_parser.add_argument("task_pack", type=Path)
    sync_parser.add_argument("--dry-run", action="store_true")
    sync_parser.set_defaults(func=run_sync_issue)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
