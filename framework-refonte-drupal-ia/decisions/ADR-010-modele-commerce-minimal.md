# ADR-010 - Modele Commerce minimal pour offres, cadeaux et justificatifs

## Contexte

Le projet a deja retenu :

- Drupal Commerce en perimetre sobre ;
- une logique cadeau rattachee a une vraie commande ;
- un justificatif terrain verifie cote serveur.

Il faut maintenant borner le **modele minimal** pour ne pas disperser la mise en oeuvre.

Le socle applicatif actuel contient le package Drupal Commerce, mais n'active pas encore tous les sous-modules utiles au modele cible.

## Decision

Le modele cible minimal s'appuie sur les briques Drupal Commerce suivantes :

- `commerce_store`
- `commerce_product`
- `commerce_order`
- `commerce_payment`
- `commerce_checkout`
- `commerce_cart`
- `commerce_number_pattern`

`commerce_promotion` reste optionnel au lot initial, a activer seulement si un vrai besoin de promotions apparait.

## Objets a suivre

### Offre

- portee par un **produit Commerce** ;
- avec au moins une variation vendable ;
- champs metier simples : duree, prix, offrable ou non, texte court de rassurance.

### Commande

- source de verite transactionnelle ;
- rattachee a l'acheteur ;
- porte le statut de paiement et les elements achetes.

### Achat cadeau

- ne devient pas une entite autonome par defaut ;
- reste rattache a la commande et/ou a la ligne de commande ;
- porte quelques donnees metier bornees : beneficiaire, message, identifiant unique, statut cadeau.

### Justificatif terrain

- rattache a l'achat effectif ;
- identifiant unique non devinable ;
- statut de verification / consommation ;
- acces scannable si pertinent.

Le projet ne cree pas de nouvelle entite custom tant que les champs portes par la commande ou la ligne de commande suffisent.

Dans le cadrage actuel, cadeau et justificatif doivent vivre **sur la ligne de commande**.

## Statuts minimaux

### Cote commande

- brouillon / panier ;
- en attente de paiement ;
- payee ;
- annulee ;
- remboursee si besoin reel.

### Cote cadeau

- non applicable ;
- a emettre ;
- emis ;
- utilise ;
- expire ;
- annule.

### Cote justificatif

- valide ;
- deja utilise ;
- annule ;
- expire ;
- invalide.

## Regles de modelisation

- la commande reste la racine metier ;
- le cadeau est une propriete d'un achat, pas un monde parallele ;
- le justificatif est verifie cote serveur, pas par simple inspection visuelle ;
- tout nouveau custom doit d'abord prouver qu'un champ ou un sous-module Commerce ne suffit pas.

## Consequences

- l'activation future des sous-modules Commerce devra suivre ce modele ;
- les premiers types de produits pourront rester peu nombreux ;
- le back-office gestionnaire pourra se concentrer sur offres, commandes, cadeaux et statuts ;
- les futurs travaux d'implementation sauront mieux ou s'arretent les champs et ou commencerait, seulement si necessaire, un petit custom.
