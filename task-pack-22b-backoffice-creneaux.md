# Agent task pack - Interface gestionnaire creneaux et report

## Statut
ready

## Agent cible

codex

## Type de travail

implementation

## Issue GitHub liee

#22

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/decisions/ADR-015-reservation-de-creneaux.md
- framework-refonte-drupal-ia/decisions/ADR-010-modele-commerce-minimal.md
- framework-refonte-drupal-ia/05-backoffice-gestionnaire.md

## Objectif

Donner au gestionnaire une interface simple pour :

1. ouvrir et fermer des creneaux date/heure ;
2. consulter les reservations a venir ;
3. reporter ou reaffecter une reservation existante.

Ce pack suppose que le modele de donnees du pack 22a est deja en place (entite creneau, champ sur ligne de commande, logique de verrou et confirmation).

## Livrable attendu

- vue d'administration listant les creneaux (ouverts, fermes, reserves) avec filtres date et statut ;
- formulaire de creation et d'edition d'un creneau par le gestionnaire (date/heure, capacite, statut) ;
- action de report : le gestionnaire peut deplacer la date/heure d'une reservation confirmee, sans perdre le lien avec la commande ni l'acheteur ;
- notification ou log minimal lors d'un report (a minima une trace consultable) ;
- permissions distinctes : le gestionnaire peut gerer les creneaux, l'acheteur ne peut pas modifier sa reservation directement.

## Pre-requis

Le pack `task-pack-22a-modele-creneau.md` doit etre en statut `done` avant de dispatcher ce pack.
L'entite creneau, les champs de ligne de commande et la logique de verrou doivent etre installes et configures.

## Fichiers a lire

- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/decisions/ADR-015-reservation-de-creneaux.md
- framework-refonte-drupal-ia/decisions/ADR-010-modele-commerce-minimal.md
- framework-refonte-drupal-ia/05-backoffice-gestionnaire.md
- framework-refonte-drupal-ia/04-architecture-drupal-cible.md

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/
- docs/

## Contraintes

- Drupal 11 + DDEV, theme admin Gin ;
- l'interface doit rester utilisable par un gestionnaire debutant (pas d'ecran surcharge) ;
- le report ne doit pas casser le lien entre la reservation et la commande ;
- la meteo n'est pas integree dans ce pack : elle reste une aide manuelle a la decision de report ;
- ne pas implementer d'interface publique cote acheteur dans ce pack ;
- s'appuyer sur les vues et formulaires Drupal standard avant de partir sur du custom.

## Verification attendue

- le gestionnaire peut creer un creneau et le voir apparaitre dans la liste ;
- le gestionnaire peut fermer un creneau et verifier qu'il n'est plus selectionnable a l'achat ;
- le gestionnaire peut reporter une reservation confirmee vers un autre creneau disponible ;
- le lien commande / reservation reste intact apres le report ;
- un utilisateur sans role gestionnaire ne peut pas modifier les creneaux.

## Definition de fin

L'interface est disponible dans DDEV, les cas de la section "Verification attendue" sont tous reproductibles manuellement, les permissions sont configurees et exportees.

## Sortie courte a produire

1. faits confirmes : briques Drupal reutilisees (Views, Form API, permissions)
2. propositions : ecrans, routes, actions implementes
3. questions ouvertes : arbitrages non couverts par les ADR (ex. notification acheteur lors d'un report)
4. fichiers modifies : liste des fichiers crees ou modifies dans le repo applicatif
