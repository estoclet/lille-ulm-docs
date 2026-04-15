# Agent task pack - Modele de donnees reservation de creneau

## Statut
ready

## Agent cible

codex

## Type de travail

implementation

## Issue GitHub liee

#22

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-015-reservation-de-creneaux.md
- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/decisions/ADR-010-modele-commerce-minimal.md

## Objectif

Implementer la structure de donnees minimale permettant :

1. de marquer une offre comme reservable ;
2. de gerer des creneaux date/heure cote serveur ;
3. de rattacher un creneau choisi a la ligne de commande ;
4. de proteger temporairement un creneau pendant le checkout et de le confirmer a la commande placee ;
5. de liberer automatiquement un creneau si la commande est abandonnee.

## Livrable attendu

- champ booleen `reservable` sur le type de produit Commerce cible ;
- entite custom ou contrib `slot` (creneau) : date/heure, capacite initiale 1, statut ouvert/ferme/reserve ;
- champ de reference creneau sur la ligne de commande (`commerce_order_item`) ;
- logique de verrou temporaire a la selection du creneau en panier : expiration configurable (defaut : 30 min) ;
- hook ou event subscriber qui confirme la reservation quand la commande passe en statut `placed` ;
- hook ou event subscriber qui libere le creneau si la commande est annulee ou abandonnee ;
- configuration exportable (config YAML) pour tout ce qui peut l'etre.

## Fichiers a lire

- framework-refonte-drupal-ia/decisions/ADR-015-reservation-de-creneaux.md
- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/decisions/ADR-010-modele-commerce-minimal.md
- framework-refonte-drupal-ia/04-architecture-drupal-cible.md

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/
- docs/

## Contraintes

- Drupal 11 + DDEV ;
- un creneau ne peut pas etre reserve deux fois simultanement (prevention double booking obligatoire) ;
- la source de verite des disponibilites reste cote serveur, jamais cote client ;
- code custom uniquement si aucun contrib stable ne couvre le besoin ; la recherche contrib doit etre documentee dans la section "faits confirmes" de la sortie (nom du module evalue, raison du rejet ou de la selection) avant toute ligne de code custom ;
- capacite initiale du creneau : 1 reservation par creneau ;
- ne pas implementer d'interface gestionnaire dans ce pack (c'est le pack 22b) ;
- ne pas implementer de fonctionnalite meteo dans ce pack ;
- configuration exportable, pas de contenu seed.

## Verification attendue

- un creneau ouvert peut etre selectionne et rattache a une ligne de commande ;
- un creneau selectionne est verrouille et n'apparait plus disponible pour un autre acheteur ;
- le verrou expire si la commande reste en panier au-dela du delai configure ;
- la reservation est confirmee quand la commande passe en `placed` ;
- la reservation est liberee si la commande est annulee ou abandonnee ;
- les structures sont exportees en config YAML.

## Definition de fin

La structure est installable dans DDEV, les cas de la section "Verification attendue" sont tous reproductibles manuellement ou via test, la config est exportee et versionnee.

## Sortie courte a produire

1. faits confirmes : modules Commerce actives, briques existantes reutilisees
2. propositions : entites, champs, hooks ou event subscribers implementes
3. questions ouvertes : arbitrages non resolus par les ADR (ex. contrib retenu ou custom)
4. fichiers modifies : liste des fichiers crees ou modifies dans le repo applicatif
