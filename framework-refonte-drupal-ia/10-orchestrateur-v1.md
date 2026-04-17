# Orchestrateur V1

## Finalite

L'orchestrateur V1 rend le framework executable sans casser ses garde-fous :

- un task pack reste l'entree unique ;
- la delegation reste explicite ;
- la revue humaine reste obligatoire ;
- GitHub Issues reste le suivi officiel.

## Composants

La V1 repose sur :

1. `templates/agent-task-pack-template.md`
2. `orchestrateur.py`
3. les issues GitHub du depot
4. des commandes agent optionnelles configurees via variables d'environnement

## Workflow de statut

Le task pack suit un cycle simple :

1. `draft`
2. `ready`
3. `running`
4. `review`
5. `done` ou `blocked`

Regles :

- `draft` autorise une issue vide le temps de cadrer ;
- `ready` exige un pack complet ;
- `dispatch` accepte un pack en `ready` ou `review`, puis le bascule en `running` ;
- un dispatch reussi replace le pack en `review` ;
- un echec d'execution ou une sortie invalide bascule en `blocked`.

## Routine de travail

1. creer ou lier l'issue GitHub ;
2. remplir un task pack court ;
3. lancer `validate` ;
4. lancer `render` ou `dispatch --dry-run` pour relire le handoff ;
5. lancer `dispatch` avec une commande agent configuree ;
6. relire la sortie et les artefacts de run ;
7. decider `done` ou `blocked` ;
8. lancer `sync-issue` pour tenir l'issue a jour.

## Commandes utiles

Validation :

`python3 framework-refonte-drupal-ia/orchestrateur.py validate mon-task-pack.md`

Handoff relisible :

`python3 framework-refonte-drupal-ia/orchestrateur.py render mon-task-pack.md`

Delegation reelle si une commande est configuree :

`LILLE_ULM_ORCH_CODEX_CMD="codex" python3 framework-refonte-drupal-ia/orchestrateur.py dispatch mon-task-pack.md`

Mise a jour de statut :

`python3 framework-refonte-drupal-ia/orchestrateur.py set-status mon-task-pack.md review`

Synchronisation issue :

`python3 framework-refonte-drupal-ia/orchestrateur.py sync-issue mon-task-pack.md --dry-run`

## Variables d'environnement

Les commandes agent sont optionnelles :

- `LILLE_ULM_ORCH_CLAUDE_CMD`
- `LILLE_ULM_ORCH_CODEX_CMD`
- `LILLE_ULM_ORCH_COPILOT_CMD`

Le framework charge aussi le fichier `.env` a la racine du depot si present.
La commande recueille le handoff sur son entree standard.

## Regles anti-derive injectees dans chaque handoff

Tout handoff genere contient les regles suivantes, non modifiables par le pack :

1. marquer explicitement : fait observe | hypothese | decision a prendre | risque ;
2. si une ambiguite n'est pas resolue par les sources listees : stopper sur ce point, ne pas trancher ;
3. ne pas creer de nouvelle source de verite non demandee ;
4. ne pas toucher aux fichiers interdits, meme pour corriger ;
5. signaler toute extension de perimetre comme decision a prendre.

Exception explicite :

- un ADR, un feature brief, une page spec ou un task pack peuvent etre produits
  ou modifies si la tache le demande explicitement dans le livrable attendu ou
  les fichiers cibles.

Le handoff impose aussi un format de sortie avec **5 titres markdown exacts** :

- `## faits observes`
- `## propositions`
- `## decisions a prendre`
- `## risques`
- `## fichiers modifies ou a produire`

La premiere ligne non vide doit etre `## faits observes`.
Toute sortie qui ajoute du texte avant ce titre est rejetee.

## Isolation du dispatch

Un `dispatch` live s'execute dans un **workspace jetable** :

- l'agent travaille sur une copie temporaire du depot ;
- le depot principal n'est plus modifie directement par le run ;
- les changements proposes sont copies dans `framework-refonte-drupal-ia/.orchestrator-state/runs/<run-id>/changes/` ;
- un resume machine est ecrit dans `changes-summary.json`.

Regle :

- si l'agent modifie un fichier hors de `Fichiers cibles a produire ou modifier`,
  le run est invalide et le pack passe en `blocked`.

## Ce que fait la V1

- valide les champs et les chemins du task pack ;
- genere un prompt de delegation borne avec regles anti-derive obligatoires ;
- force la presence d'une section `Fichiers cibles a produire ou modifier` ;
- avertit si le livrable est sous-specifie ou le contexte trop large ;
- trace les runs dans `framework-refonte-drupal-ia/.orchestrator-state/` ;
- rejette une sortie agent qui ne respecte pas le format impose ;
- isole l'execution live dans un workspace jetable ;
- conserve les changements proposes en artefacts de run ;
- permet une synchro simple avec GitHub Issues.

## Ce qu'elle ne fait pas

- arbitrage autonome ;
- chainage multi-agents ;
- fermeture automatique d'une issue sans validation ;
- creation implicite de nouvelles sources de verite.
