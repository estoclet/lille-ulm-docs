# ADR-001 - Retenir Drupal Commerce en version sobre

## Contexte

Le projet ne vise pas seulement un site vitrine.

L'activite Lille ULM repose sur :

- des offres a vendre ;
- des bons cadeaux / cartes cadeaux ;
- un besoin de suivi simple des commandes ;
- un objectif de croissance et de fidelisation.

Le legacy `DT Register` prouve l'existence d'un besoin transactionnel, mais pas d'un besoin de gros e-commerce.

Issue liee :

- `#1 Arbitrer Drupal Commerce ou non`

## Decision

Retenir **Drupal Commerce**, mais avec un perimetre initial volontairement sobre :

- catalogue d'offres ;
- commandes ;
- paiements ;
- bons cadeaux / cartes cadeaux ;
- achat pour soi ou pour offrir ;
- justificatif d'achat verifiable ;
- statuts de traitement simples ;
- fiche client legere.

Le projet ne cherche pas a reproduire un back-office marchand complexe.

## Alternatives ecartees

- simple site vitrine + formulaires sans logique de commande ;
- reconduction d'un mecanisme legacy proche de `DT Register` ;
- plateforme e-commerce plus lourde que le besoin reel.

## Consequences

- le modele de donnees doit integrer commandes, clients et logiques de cadeau ;
- le modele de donnees doit aussi prevoir un justificatif de vente controlable sans ambiguite ;
- la page `Nos offres` devient un vrai point d'entree commercial ;
- les decisions sur paiement, confirmations et statuts doivent etre specifees tot ;
- le back-office gestionnaire doit rester rassurant malgre la couche Commerce.

## Impact IA

- fichiers a relire : `00-initialisation-projet.md`, `06-commerce-crm-et-croissance.md`
- lots concernes : cadrage business, architecture Drupal, parcours business, back-office gestionnaire
- risques de duplication : ne pas redecrire cette decision dans tous les briefs ; y faire reference
