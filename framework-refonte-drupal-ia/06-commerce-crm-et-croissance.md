# Commerce, CRM et croissance

## Intention

Le futur site doit servir la croissance, pas seulement publier du contenu.

## Piliers

1. **Acquisition** : pages d'offres, formulaires, CTA, SEO
2. **Conversion** : tunnel clair, rassurance, paiement, bons cadeaux
3. **Fidelisation** : relances, offres, suivi client, campagnes
4. **Pilotage** : tableaux de bord et indicateurs

## Si Drupal Commerce est retenu

Le modele minimum doit couvrir :

- offres / produits
- commandes
- clients
- paiements
- coupons / promotions
- statuts de traitement
- preuve d'achat controlee
- export simple

Base minimale cible :

- offre = produit / variation Commerce ;
- achat = commande ;
- cadeau = donnees bornees rattachees a la commande ou a la ligne de commande ;
- justificatif = identifiant et statut de verification rattaches a l'achat.

## Creneaux et disponibilites

Besoin metier confirme :

- le gestionnaire ouvre des creneaux date/heure ;
- une commande doit pouvoir reserver un creneau parmi ces disponibilites ;
- un creneau reserve devient indisponible.

Doctrine de base :

- la source de verite des disponibilites reste cote serveur ;
- la prevention du double booking est obligatoire ;
- le besoin doit etre reconstruit dans Drupal, pas reconduit via `JEvents` ;
- le modele cible doit articuler Commerce et reservation sans surimposer un agenda legacy public ;
- la selection du creneau est recommandee pendant l'achat, puis confirmee lorsque la commande est placee ;
- la reservation doit etre portee par la ligne de commande pour rester compatible avec plusieurs achats ;
- le gestionnaire doit pouvoir reporter une reservation, notamment en fonction des conditions meteo.

## Bons cadeaux

Sujet a traiter explicitement :

- bon nominatif ou non ;
- date de validite ;
- code unique ;
- reemission possible ou non ;
- annulation / remboursement ;
- suivi d'utilisation ;
- relance avant expiration.

Doctrine de base :

- une prestation peut etre **offrable** ou non ;
- le cadeau reste rattache a une vraie commande ;
- il ne doit pas etre traite comme un simple coupon promotionnel ;
- le gestionnaire doit pouvoir suivre son statut simplement.

## Justificatif terrain

Sujet a traiter explicitement :

- format de justificatif remis apres achat ;
- identifiant unique difficilement falsifiable ;
- controle simple et rapide par le pilote ;
- preuve scannable si pertinent (ex : QR code) ;
- statut apres controle ou consommation ;
- gestion des cas deja utilise / invalide / annule.

Doctrine de base :

- la source de verite doit rester cote serveur ;
- le QR code est privilegie comme acces rapide au controle, pas comme preuve autonome ;
- le pilote doit voir un statut tres simple ;
- la verification doit pouvoir marquer l'usage ou la consommation.

Piste contrib a evaluer :

- une solution de type **ticketing / billetterie** peut etre pertinente si elle couvre emission + scan + controle plus simplement que notre modele borne ;
- elle ne doit pas etre retenue si elle impose une logique evenementielle trop lourde pour une prestation Lille ULM.

## CRM raisonnable

Eviter de transformer Drupal en monstre.

Le niveau 1 cible peut rester simple :

- fiche client utile ;
- historique de commandes ;
- source du lead ;
- segmentation basique ;
- relances automatiques ou semi-automatiques.

## Automatisations utiles

- email de confirmation ;
- relance panier / commande inachevee si pertinent ;
- relance avant expiration du bon ;
- relance client ancien ;
- notification interne sur nouvelle vente.

## KPIs a suivre

- leads recus
- ventes par offre
- taux de transformation
- commandes non finalisees
- bons proches d'expiration
- clients repetitifs
- chiffre d'affaires par periode

## Principe d'evolution

Commencer simple :

1. ventes et suivi
2. segmentation client
3. automatisation
4. experimentation marketing

Pas l'inverse.
