# ADR-020 - Gateway de paiement en production

## Contexte

Drupal Commerce est configuré (store EUR, checkout flow, produits, commandes).
Aucune gateway de paiement n'est installée en dehors de `commerce_payment_example`
utilisée uniquement en DDEV pour valider le checkout.

Le legacy DT Register utilisait PayPal. Les 238 bons 2023-2024 ont des
`payment_type` : Paypal (majoritaire), At_door, NULL.

Le volume estimé : 100 à 300 transactions par an.

## Issue liée

`#44` (à créer)

## Decision

**En attente de choix client.**

Deux options retenues à arbitrer :

### Option A — Stripe

- module : `drupal/commerce_stripe` (maintenu, compatible Commerce 3.x)
- frais : 1,5 % + 0,25 € par transaction (carte EU)
- avantages : UX moderne, pas de redirection, dashboard clair, webhooks fiables
- prérequis : compte Stripe + clés API (test + production)

### Option B — PayPal (continuité legacy)

- module : `drupal/commerce_paypal` (Smart Payment Buttons ou Advanced)
- frais : 3,4 % + 0,35 € (standard) ou 1,9 % + 0,10 € (Pro avec abonnement)
- avantages : crédibilité reconnue par les clients, identique au legacy
- prérequis : compte PayPal Business existant ou à créer

## Pourquoi ce choix (à trancher)

Stripe est préférable si le client est prêt à créer un compte.
PayPal est préférable si le compte existant est réutilisable et que la continuité
rassure les acheteurs habituels.

Les deux sont compatibles avec Commerce 3.x et le modèle de commandes actuel.

## Alternatives écartées

- **HelloAsso** : orienté association / collecte, pas adapté à la vente de prestations
- **Virement bancaire seul** : incompatible avec l'objectif de conversion en ligne
- **Gateway bancaire française (Lyra/SystemPay)** : surcoût de setup disproportionné

## Consequences

- ajouter `drupal/commerce_stripe` ou `drupal/commerce_paypal` dans `composer.json`
- activer le module dans le deploy script
- créer la gateway en config exportable (ne pas stocker les clés dans le code — `.env`)
- supprimer `commerce_payment_example` du deploy de production
- documenter les clés attendues dans `.env.example`

## Impact IA

- fichiers à relire : `ADR-001-commerce-sobre.md`, `10-orchestrateur-v1.md`
- lots concernés : Lot 5 (parcours business), Lot 7 (recette gestionnaire)
- risque : ne pas committer les clés API dans le repo
