# ADR-003 - Initialiser un socle Drupal 11 DDEV-first et low-code

## Contexte

Le cadrage produit est maintenant assez stable pour initialiser le depot applicatif.

Contraintes deja validees :

- environnement local standardise sur DDEV ;
- approche low-code ;
- code custom exceptionnel ;
- `.gitignore` maintenu en permanence ;
- documentation gestionnaire a integrer dans le back-office Drupal.

Issue liee :

- `#5 Preparer le socle applicatif Drupal`

## Decision

Initialiser le depot applicatif sur la base suivante :

- **Drupal 11** via `drupal/recommended-project` ;
- docroot `web/` ;
- environnement local **DDEV-first** ;
- depot prepare pour accueillir des modules contrib avant tout custom ;
- hygiene de depot stricte des le premier commit.

Le socle doit aussi reserver une place claire pour :

- modules custom bornes ;
- theme custom ;
- future documentation gestionnaire embarquee dans le back-office.

Baseline contrib retenue pour le socle :

- Drush ;
- Gin ;
- Admin Toolbar ;
- Metatag ;
- Pathauto ;
- Redirect ;
- Simple XML Sitemap ;
- Drupal Commerce.

Vigilance :

- `Webform` est actuellement retenu sur une branche **beta** compatible Drupal 11 ;
- `inline_entity_form` est actuellement retenu sur une branche **dev** compatible Drupal 11, comme dependance de Commerce ;
- ces dependances pre-release doivent etre reevaluees regulierement et remplacees par une version stable des que possible.

## Alternatives ecartees

- demarrage sans DDEV ;
- skeleton artisanal sans base Drupal standard ;
- custom lourd des l'initialisation ;
- structure melangeant code, backlog et documentation projet.

## Consequences

- le repo applicatif devient rapidement clonable et executable localement ;
- la recherche de contrib devient une etape obligatoire avant toute fonctionnalite ;
- les conventions de dossiers sont posees tot ;
- la documentation gestionnaire embarquee devra etre pensee comme une vraie brique du back-office.

## Impact IA

- fichiers a relire : `04-architecture-drupal-cible.md`, `05-backoffice-gestionnaire.md`
- lots concernes : architecture Drupal, back-office gestionnaire, design system editable
- risques de duplication : ne pas reecrire cet ADR dans le README applicatif ; y faire reference
