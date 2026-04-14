# Architecture Drupal cible

## Socle recommande

- Drupal 11
- environnement local : **DDEV**
- Theme admin : **Gin**
- Navigation admin : **Admin Toolbar**
- Edition media : Media Library
- Workflows : Content Moderation + Workflows
- SEO : Metatag + Pathauto + Redirect + Simple XML Sitemap
- Formulaires : Webform
- Consentement / cookies : module dedie conforme RGPD
- Analytics : solution sobre et compatible consentement, idealement Matomo

## Regle d'environnement local

Le developpement local doit etre pense **DDEV-first** :

- demarrage standardise pour tous ;
- services locaux predictibles ;
- commandes projet executees via DDEV ;
- documentation d'installation alignee sur DDEV.

Le projet ne doit pas dependre d'une installation locale artisanale propre a un seul poste.

## Composition editoriale

### Choix principal

- **Layout Builder** comme systeme de composition principal
- **Single Directory Components** comme base de composants reutilisables
- **UI Suite** seulement si un vrai besoin ulterieur de bibliotheque contrib se confirme

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

## Modules contrib a considerer

| Besoin | Piste |
| --- | --- |
| Admin intuitif | Gin, Admin Toolbar |
| Pages modulaires | Layout Builder, UI Suite |
| Composants coherents | SDC, composants thematiques |
| Formulaires | Webform |
| Automatisations | ECA |
| SEO | Metatag, Pathauto, Redirect, Simple XML Sitemap |
| Recherche interne | Search API si besoin reel |
| Consentement | module cookies / consentement adapte au RGPD |
| Analytics respectueux | Matomo |
| Seed content initial | Default Content si besoin reel et borne |
| Aide back-office integree | mecanisme core/contrib dedie avant custom |
| Controle terrain / scan | ticketing contrib a evaluer avant custom |

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
3. ne considerer un petit custom borne qu'en absence d'autre solution viable.

Le code custom doit rester **l'exception**, pas la norme.

Un besoin ne doit pas partir en implementation tant que la recherche core / contrib n'a pas ete faite et consignée.

Un gros custom n'est jamais acceptable si un contrib stable suffit.

## Hygiene de depot

Le repo applicatif doit maintenir un `.gitignore` strict et a jour en permanence.

Objectif :

- ne jamais commiter de fichiers generes localement ;
- ne jamais commiter de secrets ;
- ne jamais laisser grossir le depot avec des artefacts evitables ;
- garder un poste clonable et reproductible.
