# Agent task pack - Implementation indicateur meteo reservations

## Statut

ready

## Agent cible

codex

## Type de travail

implementation

## Issue GitHub liee

#36

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-017-api-meteo-et-doctrine-integration.md
- framework-refonte-drupal-ia/briefs/feature-brief-meteo-aide-decision.md

## Pre-requis

- task-pack-22b-backoffice-creneaux.md en `done` (vue gestionnaire des reservations existante dans l'app).

## Objectif

Creer un module Drupal custom `lille_ulm_meteo` qui :

1. appelle l'API Open-Meteo pour la localisation fixe Bondues/Lille ;
2. retourne un indicateur meteo (favorable / a surveiller / defavorable) pour un creneau date ;
3. affiche cet indicateur dans la vue gestionnaire des reservations (produite par 22b) ;
4. met les reponses API en cache 15 minutes (config) ;
5. expose une configuration Drupal (coordonnees GPS, choix d'API, cle AROME optionnelle, seuils).

## Livrable attendu

- Module `web/modules/custom/lille_ulm_meteo/` fonctionnel et activable.
- Config exportable `config/install/lille_ulm_meteo.settings.yml` avec valeurs par defaut.
- Indicateur affiche dans la vue admin des reservations : conditions prevues + badge favorable / a surveiller / defavorable.
- Lien vers Open-Meteo (ou AROME si configure) pour approfondir.
- Tests manuels documentes en commentaire de l'issue : indicateur affiche pour une reservation a venir, cache respecte, bascule AROME testee en dry-run.

## Fichiers a lire

- framework-refonte-drupal-ia/decisions/ADR-017-api-meteo-et-doctrine-integration.md
- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/briefs/feature-brief-meteo-aide-decision.md
- framework-refonte-drupal-ia/04-architecture-drupal-cible.md


## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/

## Contraintes

Cote app (dans le depot lille-ulm-drupal-app), lire avant de coder :
`web/modules/custom/lille_ulm_reservation/` (entite slot, vue gestionnaire), `web/modules/custom/lille_ulm_commerce/` (conventions), `web/sites/default/settings.project.php` (gouvernance config).

- Open-Meteo par defaut : appel `https://api.open-meteo.com/v1/forecast` avec parametres `hourly=windspeed_10m,windgusts_10m,precipitation,visibility,cloudcover_low`. Pas de cle API.
- AROME Meteo-France configurable : si `lille_ulm_meteo.settings:api_provider = 'meteofrance'` et cle presente, basculer sur l'endpoint AROME. La bascule ne necessite pas de redeploiement.
- Localisation fixe : lat `50.6833`, lon `3.0833` (secteur Bondues/Lille), stockee en config Drupal, pas en dur dans le code.
- Cache 15 minutes (duree configurable) via le service cache Drupal standard.
- Seuils par defaut (config, modifiables) :
  - vent moyen > 20 km/h → defavorable
  - rafales > 35 km/h → defavorable
  - precipitations > 0.5 mm/h → defavorable
  - visibilite < 5 km → defavorable
  - cloud_cover_low > 75 % → proxy plafond < 500 m → defavorable
- Pas d'automatisation : le module ne declenche jamais de report ni d'annulation (ADR-016). Il affiche uniquement.
- Pas de surface cliente publique dans ce lot.
- Le module ne cree pas de nouveau type d'entite. Donnees meteo non persistees en base — uniquement en cache.
- En cas d'indisponibilite API : afficher "meteo indisponible" sans bloquer la vue.

## En cas de blocage ou d'ambiguite

Si une information manque ou est contradictoire :

1. ne pas trancher a la place de l'humain ;
2. marquer le point comme `decision a prendre` dans la sortie ;
3. continuer sur les points non bloques ;
4. lister les blocages en fin de sortie dans "questions ouvertes".

Ne pas creer de nouveau fichier source de verite pour combler un vide.

## Verification attendue

- `drush en lille_ulm_meteo` s'execute sans erreur.
- La vue gestionnaire des reservations affiche un badge meteo pour chaque creneau a venir.
- Un creneau dans le passe n'affiche pas d'indicateur ou affiche "donnees non disponibles".
- Le cache est respecte : deux requetes rapprochees ne provoquent pas deux appels API.
- La config est exportable via `drush config:export` et importable sans erreur.
- Si api_provider = 'meteofrance' sans cle, le module se replie sur Open-Meteo et logue un avertissement.

## Definition de fin

- Module active localement dans DDEV.
- Indicateur visible et fonctionnel dans la vue admin des reservations.
- Config exportee dans `config/install/`.
- Commentaire de cloture poste sur l'issue liee avec captures ou log de verification.
- Statut de ce pack passe a `done`.

## Sortie courte a produire

Un commentaire d'issue listant :
1. faits confirmes (ce qui est implemente) ;
2. decisions a prendre (seuils a valider en recette avec le gestionnaire, proxy plafond nuageux) ;
3. questions ouvertes eventuelles.
