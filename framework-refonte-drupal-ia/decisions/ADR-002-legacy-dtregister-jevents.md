# ADR-002 - Ne pas reconduire DT Register et JEvents comme moteurs vivants

## Contexte

Le site actuel contient :

- `DT Register` pour l'historique transactionnel ;
- `JEvents` pour un agenda legacy ;
- des correctifs conservatoires pour maintenir l'existant ;
- 4004 inscriptions historiques et 250 evenements.

Le besoin de reprise existe, mais le socle legacy ne doit pas servir de cible.

Issue liee :

- `#2 Decider du sort de DT Register et JEvents`

## Decision

Ne pas reconduire `DT Register` ni `JEvents` comme moteurs fonctionnels du futur site.

Strategie retenue :

- archiver l'historique utile ;
- reprendre seulement les donnees reellement necessaires ;
- reconstruire le parcours de vente et les confirmations dans Drupal ;
- reconstruire dans Drupal le besoin agenda / disponibilites s'il est confirme metierement, sans reconduire `JEvents` ;
- ne pas partir d'un agenda public legacy par defaut.

## Alternatives ecartees

- migration a l'identique des mecanismes legacy ;
- maintien de `register` comme entree technique publique ;
- reprise automatique de tout l'historique sans tri metier.

## Consequences

- un travail de qualification des donnees legacy devient necessaire ;
- le futur tunnel peut etre pense pour le gestionnaire et non pour la compatibilite Joomla ;
- `JEvents` ne doit etre repris que comme source de reprise eventuelle, pas comme moteur cible ;
- les redirections et l'archivage doivent etre traites comme sujets de migration.

## Impact IA

- fichiers a relire : `00-initialisation-projet.md`, `05-dette-technique-et-risques.md`, `13-matrice-refonte-pages.md`
- lots concernes : cadrage business, migration, parcours business, SEO/redirections
- risques de duplication : ne pas reecrire l'analyse legacy complete dans les specs de pages
