# Framework IA pour la refonte Drupal

## But

Ce dossier fournit un cadre de **gestion de projet**, **conception** et **developpement** pour preparer une refonte Drupal fortement assistee par IA :

- **Claude** pour cadrer, decomposer, arbitrer et relire ;
- **Codex** pour implementer, migrer, tester et produire des diffs ;
- **Copilot** pour accelerer les petites modifications, la navigation et la documentation.

Il est concu pour limiter deux problemes frequents :

1. trop de fichiers a parcourir ;
2. des fichiers trop gros pour rester faciles a lire, resumer et reutiliser par les agents.

## Regles du cadre

- un fichier = un sujet = une decision ou un mode operatoire ;
- cible : **80 a 140 lignes** par fichier ;
- au dela de **180 lignes**, il faut scinder ;
- chaque sous-sujet important doit etre reference depuis `CONTEXT-INDEX.yaml` ;
- chaque tache IA doit partir d'un **task pack** court, pas d'un dossier entier.

## Garde-fous IA

Le framework est volontairement pense pour limiter :

- l'hallucination ;
- la duplication de verites ;
- les documents trop longs ;
- les derives de perimetre ;
- les relectures impossibles.

Principes obligatoires :

1. une information critique doit pointer vers une **source de verite** ;
2. une hypothese doit etre marquee comme hypothese ;
3. une decision doit vivre dans un **ADR** ;
4. un fichier trop gros doit etre scinde, pas "optimise plus tard" ;
5. un agent ne doit jamais completer un trou par invention silencieuse.

## Ordre de lecture

1. `00-initialisation-projet.md`
2. `01-principes-et-perimetre.md`
3. `02-regles-de-decoupage-pour-ia.md`
4. `03-gouvernance-produit-projet.md`
5. `04-architecture-drupal-cible.md`
6. `05-backoffice-gestionnaire.md`
7. `06-commerce-crm-et-croissance.md`
8. `07-orchestration-claude-codex-copilot.md`
9. `08-plan-de-lots.md`
10. `09-gouvernance-ia-friendly.md`

## Templates

Le dossier `templates/` contient les gabarits minimaux pour lancer :

- une decision ;
- une fonctionnalite ;
- une page ;
- un paquet de travail IA.

## Initialisation du projet

Le framework embarque des elements minimaux issus de `../refonte-site/` pour eviter de recommencer le cadrage a zero.

Ce socle sert a :

- rappeler l'etat reel de l'existant ;
- identifier les pages et parcours prioritaires ;
- isoler les arbitrages qui conditionnent la suite.

`refonte-site/` reste la source d'analyse detaillee ; le framework n'en reprend que le minimum actionnable pour demarrer.

## Pilotage via GitHub Issues

Le backlog operationnel vit dans les **GitHub Issues du repo framework**.

Regles simples :

1. un sujet suivi = une issue ;
2. une decision structurante = une issue puis un ADR ;
3. une issue fermee = un sujet termine ou arbitre ;
4. le framework ne doit pas dupliquer un backlog parallele dans des fichiers Markdown.

Jeu minimal de labels :

- statut : `todo`, `in-progress`, `blocked`
- lot : `lot:cadre`, `lot:design`, `lot:drupal`, `lot:contenu`
- priorite : `prio:haute`, `prio:moyenne`, `prio:basse`
- visibilite client : `client`

La page client ne doit lire que les issues portant le label `client`.

## Regle de maintenance

Avant toute mise a jour du framework :

1. identifier le fichier source a modifier ;
2. verifier si une vraie decision change ou seulement sa formulation ;
3. modifier le plus petit nombre de fichiers possible ;
4. re-scinder si un fichier depasse son budget.

## Resultat vise

Une refonte Drupal :

- modulaire ;
- facile a faire evoluer ;
- exploitable par un gestionnaire debutant ;
- orientee ventes, suivi client, fidelisation et croissance ;
- gouvernee par des documents courts, stables et actionnables.
