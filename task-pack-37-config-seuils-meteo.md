# Agent task pack - Formulaire de configuration des seuils meteo

## Statut
done

## Agent cible

codex

## Type de travail

implementation

## Issue GitHub liee

#37

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-017-api-meteo-et-doctrine-integration.md

## Pre-requis

- task-pack-23-implementation-meteo.md en `done` (module lille_ulm_meteo existant avec config schema).

## Objectif

Ajouter un formulaire de configuration (`ConfigFormBase`) dans le module `lille_ulm_meteo` permettant au gestionnaire de modifier les seuils meteo et les parametres API depuis le back-office Drupal, sans deploiement.

## Livrable attendu

- Classe `Form\MeteoSettingsForm` etendant `ConfigFormBase` dans `lille_ulm_meteo`.
- Route `lille_ulm_meteo.settings_form` sous `/admin/config/lille-ulm/meteo`.
- Lien de menu rattache a `commerce.admin_commerce` ou a un groupe de configuration Lille ULM existant.
- Permission `administer lille ulm meteo settings` declaree dans `lille_ulm_meteo.permissions.yml`, accordee au role gestionnaire.
- Formulaire exposant : latitude, longitude, cache_minutes, api_provider (select Open-Meteo / Meteo-France), meteofrance_api_key (champ masque), meteofrance_arome_endpoint, et les cinq seuils.
- Config exportable apres sauvegarde du formulaire.

## Fichiers a lire

- framework-refonte-drupal-ia/decisions/ADR-017-api-meteo-et-doctrine-integration.md

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/

## Contraintes

Cote app (dans le depot lille-ulm-drupal-app), lire avant de coder :
`web/modules/custom/lille_ulm_meteo/` (structure existante), `web/modules/custom/lille_ulm_reservation/lille_ulm_reservation.permissions.yml` et `lille_ulm_reservation.links.menu.yml` (conventions a suivre), `web/modules/custom/lille_ulm_reservation/lille_ulm_reservation.routing.yml` (pattern de route admin a reproduire).

- Etendre uniquement `lille_ulm_meteo` — ne pas modifier les autres modules.
- La cle AROME doit etre un champ de type `password` dans le formulaire (masquage).
- `api_provider` doit etre un champ `select` avec options `open_meteo` et `meteofrance`.
- Les seuils sont des nombres decimaux (`number`, pas `integer`).
- Les libelles des champs doivent etre en francais, coherents avec le back-office gestionnaire.
- La permission `administer lille ulm meteo settings` doit etre accordee au role `gestionnaire` via un `hook_install` ou une config `user.role.gestionnaire` patchee — choisir l'approche la plus legere.
- Pas d'ecran de configuration des seuils cote client public.

## En cas de blocage ou d'ambiguite

Si une information manque ou est contradictoire :

1. ne pas trancher a la place de l'humain ;
2. marquer le point comme `decision a prendre` dans la sortie ;
3. continuer sur les points non bloques ;
4. lister les blocages en fin de sortie dans "questions ouvertes".

Ne pas creer de nouveau fichier source de verite pour combler un vide.

## Verification attendue

- `drush en lille_ulm_meteo` s'execute sans erreur apres l'ajout des nouveaux fichiers.
- L'ecran est accessible a `/admin/config/lille-ulm/meteo` pour un utilisateur avec la permission.
- La sauvegarde du formulaire met a jour la config Drupal sans erreur.
- `drush config:export` inclut les nouvelles valeurs sans erreur de schema.
- Le role gestionnaire peut acceder a l'ecran ; un utilisateur sans permission ne peut pas.

## Definition de fin

- Formulaire accessible et fonctionnel dans DDEV.
- Permission accordee au role gestionnaire.
- Config exportee dans `config/install/`.
- Commentaire de cloture poste sur l'issue #37.
- Statut de ce pack passe a `done`.

## Sortie courte a produire

Un commentaire d'issue listant :
1. faits confirmes (fichiers crees, formulaire accessible, permission accordee) ;
2. decisions a prendre eventuelles ;
3. questions ouvertes eventuelles.
