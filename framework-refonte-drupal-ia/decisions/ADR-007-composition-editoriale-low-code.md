# ADR-007 - Composition editoriale low-code avec Layout Builder et SDC en base

## Contexte

Le projet doit permettre au gestionnaire de modifier les pages importantes sans entrer dans une logique de construction trop technique ou trop dispersee.

Le socle Drupal 11 verifie actuellement fournit deja :

- `layout_builder` dans le core ;
- `sdc` dans le core ;
- `field_layout` dans le core.

Le projet suit une regle stricte :

1. core d'abord ;
2. contrib ensuite ;
3. custom en dernier recours.

## Decision

La base de composition editoriale retenue est :

- **Layout Builder** pour composer les pages ;
- **SDC** pour stabiliser les composants reutilisables ;
- **Paragraphs** seulement si un besoin de contenu imbrique repetable apparait clairement plus tard.

Le projet ne retient pas, a ce stade, une dependance contrib supplementaire comme base obligatoire de composition.

Une solution de type **UI Suite** pourra etre evaluee ensuite uniquement si elle apporte une vraie valeur de bibliotheque de composants, sans complexifier inutilement l'edition.

## Pourquoi ce choix

- aligne avec la regle low-code-first ;
- base deja disponible dans Drupal 11 ;
- evite de melanger plusieurs systemes d'edition concurrents ;
- laisse une edition lisible pour des pages comme `Nos offres` et `Contact` ;
- permet d'introduire du contrib plus tard de facon justifiee plutot que speculative.

## Regles pratiques

- une page editoriale = un systeme principal de composition ;
- les composants reutilisables doivent rester peu nombreux et nommes avec un vocabulaire metier ;
- les variantes doivent etre bornees ;
- les cas imbriques complexes ne doivent pas devenir la norme ;
- l'ajout d'un contrib de composition devra etre justifie par un manque concret du core.

## Consequences

- `Layout Builder` devient la piste de build par defaut pour les premieres pages ;
- `SDC` devient la base cible pour les composants thematiques reutilisables ;
- `Paragraphs` n'est pas une brique de depart ;
- le ticket suivant pourra se concentrer sur les composants utiles aux pages prioritaires plutot que rouvrir le debat sur l'outil principal.
