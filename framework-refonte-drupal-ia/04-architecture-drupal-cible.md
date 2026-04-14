# Architecture Drupal cible

## Socle recommande

- Drupal 11
- Theme admin : **Gin**
- Navigation admin : **Admin Toolbar**
- Edition media : Media Library
- Workflows : Content Moderation + Workflows
- SEO : Metatag + Pathauto + Redirect + Simple XML Sitemap
- Formulaires : Webform
- Consentement / cookies : module dedie conforme RGPD
- Analytics : solution sobre et compatible consentement, idealement Matomo

## Composition editoriale

### Choix principal

- **Layout Builder** comme systeme de composition principal
- **UI Suite** pour fournir une bibliotheque de composants et de layouts coherents
- **Single Directory Components** pour stabiliser les composants

### Regle

Ne pas utiliser en parallele :

- Layout Builder partout
- Paragraphs partout
- blocs custom partout

Sans doctrine claire.

Doctrine recommandee :

- Layout Builder pour les pages ;
- composants UI Suite / SDC pour les blocs reutilisables ;
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

## Regle d'architecture

Chaque besoin metier doit preferer :

1. le core Drupal ;
2. un module contrib mature ;
3. un petit module custom borne ;
4. jamais un gros custom si un contrib stable suffit.
