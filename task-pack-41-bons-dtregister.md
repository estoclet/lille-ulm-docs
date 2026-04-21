# Agent task pack - Reprise des bons DT Register 2023-2024 dans Drupal Commerce

## Statut
done

## Agent cible

codex

## Type de travail

migration

## Issue GitHub liee

#41

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-013-reprise-selective-des-donnees-joomla.md
- refonte-site/09-reprise-donnees-reservation.md

## Pre-requis

- Les types de commande et champs Commerce existent dans l'app (issues #14-#17 terminees).
- Les variations Commerce ont les SKUs : `BAT-15MIN`, `BAT-30MIN`, `INIT-45MIN`, `INIT-1H`, `INIT-1H30`, `COURS-6X40`.

## Deblocage effectue (2026-04-21)

Le mapping `event_variation_map` utilisait des IDs d'entite auto-incrementes (fragiles).
Remplace par des SKUs stables dans :
- `config/install/lille_ulm_legacy_import.settings.yml`
- `config/sync/lille_ulm_legacy_import.settings.yml`
- `config/schema/lille_ulm_legacy_import.schema.yml` (sequence type : integer → string)
- `src/Service/LegacyBonImporter.php` (lookup par SKU via `getStorage('commerce_product_variation')->getQuery()->condition('sku', ...)`)

Validation confirmee en DDEV :
`drush lille-ulm:import-legacy-bons --source=legacy-test.csv --dry-run`
→ rows_read: 5, rows_eligible: 3, missing_mappings: 0, duplicates: 3, [OK]

## Objectif

Produire les outils permettant de :

1. exporter en CSV l'historique complet `jh3_dtregister_user` (obligation comptable) ;
2. identifier et importer dans Drupal Commerce les bons 2023-2024 avec `payment_verified=1` comme commandes en attente de verification gestionnaire ;
3. offrir une vue back-office au gestionnaire pour clore ces bons un par un.

## Livrable attendu

### 1. Script SQL d'extraction

Fichier `scripts/dtregister-export-2023-2024.sql` ou commande drush documentee produisant :

- export CSV complet (`jh3_dtregister_user`, toutes colonnes, toutes annees) ;
- export filtre 2023-2024 : `payment_verified=1` ET `date >= '2023-01-01'`.

Schema de la table source (issu de l'audit) :

```
jh3_dtregister_user :
  id, eventId, userId, first_name, last_name, email, phone,
  payment_type (Paypal|At_door|NULL|Free), payment_verified (0|1),
  cancel (0|1), date (datetime), published
```

### 2. Module d'import `lille_ulm_legacy_import`

Commande drush `drush lille-ulm:import-legacy-bons --source=<fichier-csv>` qui :

- lit le CSV filtre 2023-2024 ;
- cree une commande Commerce (`order_default`) par ligne avec :
  - statut : `draft` (en attente de verification) ;
  - champ `field_purchase_token` : valeur `legacy-<id>` ;
  - champ `field_recipient_name` : `first_name + last_name` de la ligne source ;
  - champ `field_recipient_email` : email de la ligne source ;
  - note interne : `Bon legacy DT Register #<id> — eventId <eventId> — <payment_type>` ;
- verifie l'unicite sur `field_purchase_token` pour eviter les doublons en cas de rejeu.

### 3. Vue gestionnaire "Bons legacy a verifier"

Vue Drupal (`views`) listant les commandes en statut `draft` avec `field_purchase_token` prefixe `legacy-`, colonnes :

- token ;
- nom beneficiaire ;
- email ;
- note interne (eventId, type de paiement) ;
- actions : "Marquer comme honore" (passe en `completed`) / "Annuler" (passe en `cancelled`).

## Fichiers a lire

- refonte-site/09-reprise-donnees-reservation.md
- framework-refonte-drupal-ia/decisions/ADR-013-reprise-selective-des-donnees-joomla.md

## Fichiers cibles a produire ou modifier

- ../lille-ulm-drupal-app/scripts/dtregister-export-2023-2024.sql
- ../lille-ulm-drupal-app/web/modules/custom/lille_ulm_legacy_import/
- ../lille-ulm-drupal-app/config/sync/views.view.lille_ulm_legacy_bons_a_verifier.yml

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/
- refonte-site/

## Contraintes

Cote app (dans le depot lille-ulm-drupal-app), lire avant de coder :
`config/sync/commerce_order.commerce_order_type.default.yml` (workflow `order_default`),
`config/sync/field.field.commerce_order_item.default.field_purchase_token.yml`,
`config/sync/field.field.commerce_order_item.default.field_recipient_name.yml`,
`config/sync/field.field.commerce_order_item.default.field_recipient_email.yml`.

- Le script SQL doit fonctionner sur une base Joomla 3 standard avec prefixe `jh3_`.
- La commande drush accepte `--dry-run` pour simuler sans ecrire.
- Ne pas creer de nouveau type de commande Commerce — utiliser `order_default`.
- Le champ `field_purchase_token` est unique en base (index existant) : verifier avant insertion.
- Les bons anterieurs a 2023 ne sont pas importes dans Drupal — CSV archive uniquement.
- Pas de donnees personnelles dans les logs ou les messages d'erreur drush (RGPD).
- Le module doit pouvoir tourner sans que la base Joomla source soit accessible — il lit depuis un CSV, pas depuis la BDD Joomla directement.

## En cas de blocage ou d'ambiguite

Si une information manque ou est contradictoire :

1. ne pas trancher a la place de l'humain ;
2. marquer le point comme `decision a prendre` dans la sortie ;
3. continuer sur les points non bloques ;
4. lister les blocages en fin de sortie dans "questions ouvertes".

Ne pas creer de nouveau fichier source de verite pour combler un vide.

## Verification attendue

- Le script SQL est syntaxiquement valide (testable avec `mysql --syntax-check` ou equivalent).
- `drush lille-ulm:import-legacy-bons --source=test.csv --dry-run` s'execute sans erreur avec un CSV de 5 lignes de test.
- En mode reel, les commandes creees sont visibles dans `/admin/commerce/orders` avec statut `draft`.
- La vue "Bons legacy a verifier" est accessible au gestionnaire.
- Un rejeu de la commande drush ne cree pas de doublons.

## Definition de fin

- Script SQL documente dans `scripts/`.
- Module `lille_ulm_legacy_import` installe et commande drush fonctionnelle en DDEV.
- Vue gestionnaire accessible.
- Commentaire de cloture poste sur l'issue #41.
- Statut de ce pack passe a `done`.

## Sortie courte a produire

Un commentaire d'issue listant :
1. faits confirmes (script SQL, commande drush, vue gestionnaire) ;
2. decisions a prendre (eventId a mapper sur des produits Commerce, champs manquants) ;
3. questions ouvertes eventuelles.
