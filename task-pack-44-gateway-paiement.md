# Agent task pack - Intégration gateway de paiement

## Statut

draft

## Agent cible

codex

## Type de travail

implementation

## Issue GitHub liée

#44

## Source de vérité

- framework-refonte-drupal-ia/decisions/ADR-020-gateway-paiement.md
- framework-refonte-drupal-ia/decisions/ADR-001-commerce-sobre.md

## Pré-requis

- Décision prise par le client : Stripe ou PayPal (voir ADR-020).
- Clés API disponibles (test + production).
- Issues #14-#17 terminées (types de commande Commerce en place).

## Objectif

Installer et configurer la gateway de paiement choisie pour que le checkout
Drupal Commerce soit fonctionnel en production.

## Livrable attendu

### 1. Dépendance Composer

Ajouter dans `composer.json` :
- Stripe : `drupal/commerce_stripe`
- ou PayPal : `drupal/commerce_paypal`

### 2. Activation dans le deploy script

Ajouter le module au `drush en` dans `scripts/deploy.sh`.

### 3. Config exportable

Fichier `config/sync/commerce_payment_gateway.*.yml` avec :
- plugin correct (stripe ou paypal_checkout)
- mode : `test` par défaut (basculé en `live` via variable d'env ou config override)
- clés API lues depuis l'environnement (ne pas coder en dur)

### 4. Documentation des variables d'env

Ajouter dans un fichier `.env.example` à la racine :
```
# Stripe
COMMERCE_STRIPE_SECRET_KEY=
COMMERCE_STRIPE_PUBLISHABLE_KEY=
# ou PayPal
COMMERCE_PAYPAL_CLIENT_ID=
COMMERCE_PAYPAL_SECRET=
```

### 5. Suppression de la gateway exemple

Retirer `commerce_payment_example` du deploy de production.
Le module peut rester disponible pour DDEV uniquement
(ne pas l'ajouter au `drush en` dans `deploy.sh`).

## Fichiers à lire

- framework-refonte-drupal-ia/decisions/ADR-020-gateway-paiement.md
- scripts/deploy.sh
- composer.json

## Fichiers cibles à produire ou modifier

- composer.json
- composer.lock
- scripts/deploy.sh
- config/sync/commerce_payment_gateway.*.yml
- .env.example (créer si absent)

## Fichiers à ne pas toucher

- framework-refonte-drupal-ia/
- web/modules/custom/

## Contraintes

- Aucune clé API ne doit apparaître dans le code ou la config exportée.
- La gateway doit fonctionner en mode `test` sur DDEV avant d'être passée en `live`.
- Le `drush en commerce_payment_example` existant en DDEV ne doit pas être commité
  dans deploy.sh (risque d'activer la gateway fictive en production).
- Lire `web/sites/default/settings.php` pour comprendre comment les variables
  d'env sont injectées dans la config Drupal.

## En cas de blocage ou d'ambiguïté

1. Ne pas choisir entre Stripe et PayPal — la décision appartient au client (ADR-020).
2. Si les clés de test ne sont pas disponibles, générer la config sans les clés
   et marquer `DECISION A PRENDRE` aux emplacements concernés.
3. Ne pas créer de nouveau type de commande ni modifier le checkout flow existant.

## Vérification attendue

- `composer install` sans erreur après ajout du module.
- En DDEV avec clés de test : un achat complet (ajout panier → checkout → paiement test)
  crée une commande en statut `completed` dans `/admin/commerce/orders`.
- La gateway exemple n'est pas présente dans la config exportée vers production.

## Définition de fin

- Module installé et gateway configurée en mode test.
- Achat de bout en bout validé en DDEV.
- Config exportée dans `config/sync/`.
- `.env.example` documenté.
- Commentaire de clôture posté sur l'issue #44.
- Statut de ce pack passé à `done`.

## Sortie courte à produire

Un commentaire d'issue listant :
1. gateway installée et testée (provider, version) ;
2. commande de test créée en statut `completed` (ID) ;
3. variables d'env requises en production.
