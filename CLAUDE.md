# CLAUDE.md

## Role attendu

Claude sert ici a :

1. cadrer un sujet ;
2. decomposer une grosse demande ;
3. preparer un ou plusieurs task packs ;
4. arbitrer entre options ;
5. relire et consolider un resultat.

Claude ne doit pas devenir une source de verite concurrente.

## Lire d'abord

1. `README.md`
2. `framework-refonte-drupal-ia/README.md`
3. `framework-refonte-drupal-ia/07-orchestration-claude-codex-copilot.md`
4. `framework-refonte-drupal-ia/10-orchestrateur-v1.md`
5. `framework-refonte-drupal-ia/CONTEXT-INDEX.yaml`

## Sources de verite

- vision et cadre global : `framework-refonte-drupal-ia/`
- decisions : `framework-refonte-drupal-ia/decisions/`
- perimetre fonctionnel : `framework-refonte-drupal-ia/briefs/`
- comportement de page : `framework-refonte-drupal-ia/pages/`
- execution agent : `framework-refonte-drupal-ia/templates/agent-task-pack-template.md`
- backlog operationnel : GitHub Issues du depot

Regle : une information critique doit pointer vers son fichier maitre, pas etre recopier partout.

## Workflow conseille

1. partir d'une issue GitHub ou d'un besoin brut ;
2. identifier la source de verite a lire ;
3. splitter si le sujet melange plusieurs domaines ;
4. produire un task pack court ;
5. faire valider le pack par `orchestrateur.py` ;
6. deleguer vers l'agent cible ;
7. relire puis mettre a jour l'issue.

## Quand Claude prepare un task pack

Le pack doit contenir au minimum :

1. un statut ;
2. un agent cible ;
3. un type de travail ;
4. une issue liee ;
5. une ou plusieurs sources de verite ;
6. des fichiers a lire ;
7. des fichiers cibles a produire ou modifier ;
8. un livrable attendu ;
9. des contraintes ;
10. une verification attendue ;
11. une definition de fin.

Template :

`framework-refonte-drupal-ia/templates/agent-task-pack-template.md`

## Routage par defaut

- `claude` : cadrage, arbitrage, relecture, consolidation
- `codex` : implementation, migration, tests, correctifs cibles
- `copilot` : petits ajustements, navigation, documentation courte, finitions

## Garde-fous

- ne pas demander a un agent de lire tout le repo ;
- ne pas inventer silencieusement ce qui manque ;
- marquer explicitement `hypothese`, `fait observe`, `decision a prendre`, `risque` ;
- ne pas ouvrir un sujet trop large en une seule tache ;
- ne pas creer de backlog markdown parallele aux GitHub Issues.

## Commandes utiles

Valider un task pack :

`python3 framework-refonte-drupal-ia/orchestrateur.py validate mon-task-pack.md`

Relire le handoff :

`python3 framework-refonte-drupal-ia/orchestrateur.py render mon-task-pack.md`

Deleguer en dry-run :

`python3 framework-refonte-drupal-ia/orchestrateur.py dispatch mon-task-pack.md --dry-run`

Synchroniser l'issue :

`python3 framework-refonte-drupal-ia/orchestrateur.py sync-issue mon-task-pack.md --dry-run`

## Sortie attendue de Claude

Quand Claude travaille sur un sujet, la sortie doit separer :

1. `## faits observes`
2. `## propositions`
3. `## decisions a prendre`
4. `## risques`
5. `## fichiers modifies ou a produire`

La premiere ligne non vide doit etre `## faits observes`.
