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
- `dispatch` fait passer le pack en `running`, puis en `review` si l'agent repond correctement ;
- un echec d'execution bascule en `blocked`.

## Routine de travail

1. creer ou lier l'issue GitHub ;
2. remplir un task pack court ;
3. lancer `validate` ;
4. lancer `dispatch` en dry-run pour relire le handoff ;
5. lancer `dispatch` avec une commande agent configuree ;
6. relire la sortie et decider `done` ou `blocked` ;
7. lancer `sync-issue` pour tenir l'issue a jour.

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

La commande recueille le handoff sur son entree standard.

## Ce que fait la V1

- valide les champs et les chemins du task pack ;
- genere un prompt de delegation borne avec regles anti-derive obligatoires ;
- avertit si le livrable est sous-specifie ou le contexte trop large ;
- trace les runs dans `.orchestrator-state/` ;
- permet une synchro simple avec GitHub Issues.

## Regles anti-derive injectees dans chaque handoff

Tout handoff genere contient les regles suivantes, non modifiables par le pack :

1. marquer explicitement : fait observe | hypothese | decision a prendre | risque ;
2. si une ambiguite n'est pas resolue par les sources listees : stopper sur ce point, ne pas trancher ;
3. ne pas creer de nouveau fichier source de verite ;
4. ne pas toucher aux fichiers interdits, meme pour corriger ;
5. signaler toute extension de perimetre comme decision a prendre.

## Ce qu'elle ne fait pas

- arbitrage autonome ;
- chainage multi-agents ;
- fermeture automatique d'une issue sans validation ;
- creation implicite de nouvelles sources de verite.
