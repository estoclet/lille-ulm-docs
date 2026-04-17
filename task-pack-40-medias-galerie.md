# Agent task pack - Import medias Joomla dans le Media Drupal

## Statut
running

## Agent cible

codex

## Type de travail

migration

## Issue GitHub liee

#40

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-013-reprise-selective-des-donnees-joomla.md
- refonte-site/08-medias-et-assets.md

## Pre-requis

Aucun pre-requis bloquant.

## Objectif

Preparer et executer l'import des images source de PhocaGallery (et des visuels marketing utiles) dans le systeme Media de Drupal, en excluant les miniatures auto-generees et les assets techniques.

## Livrable attendu

- Un module ou script d'import (`lille_ulm_media_import` ou commande drush custom) qui :
  - lit les images depuis un repertoire source configurable (par defaut `../joomla-files/images/`) ;
  - distingue les images source des miniatures generees (les miniatures PhocaGallery ont un suffixe `_xs`, `_sm`, `_md`, `_lg`, `_phocagallery` ou sont dans des sous-dossiers `thumbs/`) ;
  - cree des entites `media` de type `image` dans Drupal pour chaque image source retenue ;
  - organise les medias par categorie (avion, vue, atterrissage, pilote, marketing) selon le sous-dossier source ;
  - renseigne le champ `alt` a partir du nom de fichier nettoye (sans extension, tirets en espaces).
- Documentation dans le commentaire d'issue : commande a executer, chemin source attendu.

Images a importer (prioritaires) :
- `images/phocagallery/avion/` — images source uniquement (hors thumbs)
- `images/phocagallery/vue/` — images source uniquement
- `images/phocagallery/atterrissage/` — images source uniquement
- `images/phocagallery/pilote/` — images source uniquement
- `images/stories/IMG_0108.JPG` — visuel marketing home
- `images/stories/logo_credit_agricole.jpg` — logo reassurance paiement
- `images/bon/` — visuels bons cadeaux
- `images/emailbon/` — visuels email transactionnel

Images a exclure :
- miniatures auto-generees (`*_xs.*`, `*_sm.*`, `*_md.*`, `*_lg.*`, tout fichier dans `thumbs/`)
- `images/M_images/`
- `images/smilies/`
- `images/banners/`
- `images/paypal.png`, `images/wire_transfer_eur_big.png`
- assets generiques Joomla

## Fichiers a lire

- refonte-site/08-medias-et-assets.md
- framework-refonte-drupal-ia/decisions/ADR-013-reprise-selective-des-donnees-joomla.md

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/
- refonte-site/

## Contraintes

Cote app (dans le depot lille-ulm-drupal-app), lire avant de coder :
`config/sync/` pour verifier le type de media `image` existant et les champs disponibles.

- Le repertoire source Joomla n'est pas encore monte dans DDEV. Le script doit accepter le chemin source en parametre et traiter proprement l'absence du repertoire (log + sortie propre, pas d'erreur fatale).
- Si le type media `image` n'existe pas dans la config exportee, le creer via config (pas en dur dans le code).
- Les medias crees doivent etre permanents (pas ephemeres).
- Le champ `alt` ne doit pas etre vide — utiliser le nom de fichier nettoye comme valeur par defaut.
- Ne pas ecraser les medias deja existants en cas de rejeu — verifier l'existence avant creation.
- Regrouper les medias par tags ou vocabulary si un systeme de tags media existe deja dans la config.

## En cas de blocage ou d'ambiguite

Si une information manque ou est contradictoire :

1. ne pas trancher a la place de l'humain ;
2. marquer le point comme `decision a prendre` dans la sortie ;
3. continuer sur les points non bloques ;
4. lister les blocages en fin de sortie dans "questions ouvertes".

Ne pas creer de nouveau fichier source de verite pour combler un vide.

## Verification attendue

- Le module ou script s'installe sans erreur.
- En l'absence du repertoire source, la commande affiche un message clair et se termine proprement sans erreur fatale.
- Avec un repertoire source de test contenant quelques images, les medias sont crees avec alt renseigne et organisation par categorie.
- Pas de doublon si la commande est rejouee.

## Definition de fin

- Module ou script pret et documente.
- Test avec un repertoire source valide confirme en DDEV (meme un sous-ensemble reduit).
- Commentaire de cloture poste sur l'issue #40.
- Statut de ce pack passe a `done`.

## Sortie courte a produire

Un commentaire d'issue listant :
1. faits confirmes (module cree, commande documentee) ;
2. decisions a prendre (chemin source definitif, vocabulary tags medias a creer ou non) ;
3. questions ouvertes eventuelles.
