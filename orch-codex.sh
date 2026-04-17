#!/usr/bin/env bash
# Wrapper codex pour l'orchestrateur Lille ULM.
# Reçoit le prompt via stdin, exécute codex exec dans le dépôt app.
APP_DIR="$(cd "$(dirname "$0")/../lille-ulm-drupal-app" && pwd)"
exec codex exec --dangerously-bypass-approvals-and-sandbox -C "$APP_DIR" -
