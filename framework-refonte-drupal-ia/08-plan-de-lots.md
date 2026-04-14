# Plan de lots

## Lot 0 - Initialisation

- relire `00-initialisation-projet.md`
- confirmer les sources de verite issues de `refonte-site/`
- arbitrer Commerce ou non en niveau pre-cadrage
- qualifier le sort de `DT Register` et `JEvents`
- confirmer les pages prioritaires du MVP

Sorties minimales :

- 1 ADR de cadrage business
- 1 feature brief parcours offres / vente
- 2 page specs prioritaires
- 1 decision de reprise / archivage legacy

## Lot 1 - Cadrage business

- offres a vendre
- besoin de paiement
- besoin de bon cadeau
- besoin de CRM
- besoin d'agenda

## Lot 2 - Architecture Drupal

- decision Commerce ou non
- decision Layout Builder / UI Suite
- decision analytics / consentement
- decision CRM interne / externe

## Lot 3 - Design system editable

- bibliotheque de composants
- layouts types
- variantes autorisees
- regles d'edition

## Lot 4 - Back-office gestionnaire

- roles
- menus simplifies
- dashboard du jour
- vues de gestion
- aides contextuelles

## Lot 5 - Parcours business

- page offres
- tunnel de vente
- formulaires
- messages transactionnels
- relances

## Lot 6 - Migration

- contenus
- medias
- redirects
- historique utile
- SEO critique

Sous-lots recommandes :

1. contenus et URLs prioritaires ;
2. medias source utiles ;
3. archives transactionnelles `DT Register` ;
4. agenda `JEvents` seulement si un besoin cible est confirme.

## Lot 7 - Qualite

- accessibilite
- SEO
- performance
- RGPD
- recette gestionnaire

## Regle de lot

Chaque lot doit pouvoir etre confie a une IA avec :

- 1 doc source
- 1 template
- 1 sortie

Si ce n'est pas possible, le lot est trop grand.

## Traduction en GitHub Issues

Chaque lot doit ensuite etre declinable en issues courtes :

- visibles et suivables ;
- avec un seul sujet principal ;
- reliees a un label `lot:*` ;
- marquees `client` seulement si leur lecture est acceptable cote client.
