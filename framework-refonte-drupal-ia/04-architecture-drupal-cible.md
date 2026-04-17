# Architecture Drupal cible

## Socle retenu (état au 2026-04-17)

- Drupal 11
- environnement local : **DDEV**
- Thème admin : **Gin** + Admin Toolbar
- Thème front : **Radix 6.x** (base Bootstrap 5) + sous-thème `lille_ulm_theme`
- Composition éditoriale : **Layout Builder** + **SDC** (ADR-007, ADR-019)
- Edition media : Media Library
- Workflows : Content Moderation + Workflows
- SEO : Metatag + Pathauto + Redirect + Simple XML Sitemap
- Formulaires : Webform
- Consentement / cookies : module dédié conforme RGPD
- Analytics : solution sobre et compatible consentement, idéalement Matomo

## Regle d'environnement local

Le developpement local doit etre pense **DDEV-first** :

- demarrage standardise pour tous ;
- services locaux predictibles ;
- commandes projet executees via DDEV ;
- documentation d'installation alignee sur DDEV.

Le projet ne doit pas dependre d'une installation locale artisanale propre a un seul poste.

## Regle de langue

Le site public et le back-office gestionnaire sont exploites en **francais uniquement**.
Ne pas maintenir d'architecture multilingue active tant qu'un besoin metier explicite ne l'impose pas.

## Composition editoriale

### Choix principal

- **Layout Builder** comme systeme de composition principal
- **Single Directory Components** comme base de composants reutilisables
- **UI Suite** seulement si un vrai besoin ulterieur de bibliotheque contrib se confirme (doctrine — ADR-007)

### Regle

Ne pas utiliser en parallele :

- Layout Builder partout
- Paragraphs partout
- blocs custom partout

Sans doctrine claire.

Doctrine recommandee :

- Layout Builder pour les pages ;
- composants SDC pour les blocs reutilisables ;
- UI Suite seulement si elle apporte une vraie valeur supplementaire ;
- Paragraphs seulement si un contenu imbrique repetable le justifie vraiment.

## Drupal Commerce : decision

### Pertinent si

- vente en ligne maintenue ;
- besoin de commandes ;
- promotions / coupons ;
- suivi client ;
- relances ;
- exports / reporting ;
- bons cadeaux ou prestations vendues.

### Peut etre evite si

- simple prise de contact ;
- tunnel externe de vente ;
- aucun besoin de commande interne.

## Base commerce recommandee

Si Commerce est retenu :

- Drupal Commerce
- produits = prestations / bons cadeaux
- variations = declinaisons vendables de l'offre
- promotions / coupons
- emails transactionnels
- tableaux de bord commandes / paiements / statuts
- logique metier "bon cadeau" explicitement specifiee

## Modules contrib retenus

| Besoin | Module | Version |
| --- | --- | --- |
| Admin intuitif | gin, admin_toolbar | en place |
| Thème front | radix | ^6 |
| Composants Bootstrap SDC | ui_suite_bootstrap | 5.2.0 |
| Styles sections Layout Builder | layout_builder_styles | ^2 |
| Restriction palette blocs | layout_builder_restrictions | ^3 |
| Templates de sections | section_library | ^2 |
| Formulaires | webform | en place |
| Commerce | drupal/commerce | en place |
| SEO | metatag, pathauto, redirect | à installer |
| Automatisations | ECA | à évaluer |
| Consentement | module RGPD dédié | à choisir |
| Analytics | Matomo | à installer |

`gin_lb` est **exclu** : incompatible Drupal 11 + gin_toolbar 3.x.

## Doctrine seed content

Le projet ne doit pas confondre :

- configuration Drupal ;
- contenus editoriaux ordinaires ;
- seed content de premier deploiement.

Regle :

1. la structure va dans la configuration versionnee ;
2. le contenu editorial courant n'a pas vocation a etre versionne ;
3. seul un seed content minimal, stable et vraiment utile au premier deploiement peut etre industrialise.

La piste a privilegier est un module contrib simple de type **Default Content** si un vrai besoin apparait.

Les mecanismes lourds de synchronisation de contenus ne doivent pas etre introduits sans besoin operationnel explicite.

## Regle d'architecture

Chaque nouvelle fonctionnalite doit suivre cet ordre :

1. verifier si le core Drupal couvre deja le besoin ;
2. rechercher un module contrib mature et maintenu ;
3. considerer une couche low-code Drupal si le contrib seul ne suffit pas ;
4. ne considerer un petit custom borne qu'en absence d'autre solution viable.

Le code custom doit rester **l'exception**, pas la norme.

Un besoin ne doit pas partir en implementation tant que la recherche core / contrib /
low-code n'a pas ete faite et consignee.

Un gros custom n'est jamais acceptable si un contrib stable suffit.

## Hygiene de depot

Le repo applicatif doit maintenir un `.gitignore` strict et a jour en permanence.

Objectif :

- ne jamais commiter de fichiers generes localement ;
- ne jamais commiter de secrets ;
- ne jamais laisser grossir le depot avec des artefacts evitables ;
- garder un poste clonable et reproductible.
