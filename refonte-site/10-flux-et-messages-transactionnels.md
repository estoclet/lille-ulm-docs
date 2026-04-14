# Flux et messages transactionnels

## Vue d'ensemble

Le site ancien ne se limite pas a afficher des offres. Il porte aussi des messages et etapes transactionnels explicites :

- achat du bon en ligne ;
- envoi d'une confirmation par email ;
- fourniture d'un bon cadeau ;
- generation d'un code de confirmation ;
- prise de rendez-vous ulterieure par telephone ;
- page de remerciement post-inscription.

## Flux explicite releve dans les contenus

Sur la page `Nos offres`, le parcours d'achat est formule noir sur blanc :

1. achat du bon en ligne ;
2. email de confirmation avec bon cadeau ;
3. prise de date par telephone avec code de confirmation ;
4. vol au depart de Bondues.

Ce flux est une information produit majeure. Il doit etre traite comme une specification metier, pas comme une simple phrase marketing.

## Pages et contenus lies au transactionnel

### CTAs vers DT Register

Les pages d'offres renvoient vers des URLs `DT Register` a base de `eventId`.

### Remerciements

Les articles `Remerciement` et `Remerciement ULM` suggerent un flux final de confirmation avec :

- message de remerciement ;
- modalite de paiement par cheque ;
- rappel de validite du bon ;
- canal de contact pour fixer le rendez-vous.

### Contact

Le site expose aussi un formulaire public `BreezingForms` independant du flux de reservation.

## Etat reel du front transactionnel

Apres correctifs legacy, les URLs de detail / inscription `DT Register` repondent de nouveau et le tunnel peut aller jusqu'a la page de remerciement.

En revanche, ce retour en service reste techniquement conservatoire :

- le moteur repose toujours sur un empilement legacy fragile ;
- plusieurs offres ont ete republiees avec des dates artificiellement prolongees jusqu'en 2030 ;
- cela ne change pas le besoin de requalifier le flux cible en refonte.

Conclusion :

- le flux commercial est encore decrit dans le contenu ;
- le moteur technique sous-jacent est de nouveau exploitable mais reste structurellement fragile ;
- la refonte doit separer le besoin cible du systeme historique legacy.

## Indices trouves dans les donnees

Dans `jh3_dtregister_user`, on observe :

- generation de `confirmNum` de type `DC-8545887` ;
- lignes recentes encore en 2024 ;
- colonnes client parfois nulles dans les lignes recentes ;
- `due_amount` souvent a `0.00` dans l'extrait recent.

Lecture :

- la donnee transactionnelle existe bien ;
- sa qualite et sa completude doivent etre auditees avant toute reprise.

## Ce que la cible devra decider

- simple formulaire de demande ;
- vente de bons cadeaux ;
- paiement en ligne ;
- generation automatique de confirmations ;
- back-office de suivi ;
- agenda de prise de rendez-vous ;
- conservation de l'historique existant.

## Recommandation

Documenter ce flux comme un lot produit autonome :

- objectif business ;
- etapes ;
- donnees necessaires ;
- emails / confirmations ;
- contraintes legales ;
- parcours SAV et prise de rendez-vous.
