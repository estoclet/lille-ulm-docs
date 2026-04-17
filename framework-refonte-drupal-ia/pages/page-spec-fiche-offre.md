# Page spec - Fiche offre (produit Commerce)

## Objectif de la page

Convaincre et convertir : un visiteur arrive sur une offre precise,
comprend ce qu'il va vivre, et achete ou reserve en confiance.

## Public cible

- acheteur pour soi voulant confirmer son choix ;
- proche cherchant a offrir cette experience specifique ;
- prospect comparant deux offres.

## Blocs autorises

### Zone Commerce (non editable Layout Builder)

- photo principale + galerie secondaire ;
- titre de l'offre ;
- prix et duree ;
- badge "Offrir cette experience" si applicable ;
- formulaire Add to cart / selection de creneau ;
- informations pratiques : age minimum, poids maximum, lieu de depart ;
- reassurance paiement.

### Zone Layout Builder (editable)

- description longue et storytelling ;
- "Ce que vous allez vivre" (liste mise en valeur) ;
- galerie photos complementaire ;
- bloc "Comment ca se passe" (etapes) ;
- FAQ specifique a l'offre (optionnel) ;
- autres offres susceptibles de vous plaire (Vue Commerce).

## CTA principaux

- acheter ce bon ;
- offrir cette experience ;
- choisir une date (si offre reservable) ;
- nous appeler pour cette offre.

Les libelles visibles cote public restent en francais et orientes usage.
Exclure tout libelle technique brut de type `Add to cart`.

## Champs modifiables par le gestionnaire

Via back-office Commerce (fiche produit) :
- titre, prix, statut publie/masque ;
- photo principale et galerie ;
- description courte ;
- duree, age minimum, poids maximum ;
- eligibilite cadeau (field_is_bookable) ;
- disponibilite a la reservation.

Via Layout Builder (zone inferieure) :
- description longue ;
- etapes / deroulement ;
- FAQ specifique.

## Contraintes SEO

- H1 = titre de l'offre, unique ;
- metadata title : "[Offre] - Bapteme de l'air ULM Lille - Bondues" ;
- breadcrumb : Accueil > Nos offres > [Offre] ;
- URL stable type /offres/[slug].

## Contraintes accessibilite

- galerie photo navigable au clavier ;
- prix lisible par les lecteurs d'ecran (pas en image) ;
- formulaire add-to-cart avec labels explicites ;
- messages d'erreur de formulaire accessibles.

## Variantes autorisees

- fiche avec selection de creneau (offre reservable) ;
- fiche sans selection de creneau (bon cadeau pur) ;
- fiche avec ou sans FAQ.

## Composants relies

- template Twig `commerce_product--default` ;
- section-band (etapes) ;
- offer-card (autres offres) ;
- hero-media (galerie photo) ;
- contact-strip.

## Source de verite

- ADR-008-logique-prestations-a-offrir.md
- ADR-010-modele-commerce-minimal.md
- ADR-015-reservation-de-creneaux.md
- ADR-018-charte-graphique-et-design-tokens.md
