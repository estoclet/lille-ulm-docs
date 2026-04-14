# ADR-008 - Traiter les prestations a offrir comme un parcours cadeau borne

## Contexte

Le client veut pouvoir vendre certaines prestations pour qu'elles soient offertes.

Le besoin ne se limite pas a un simple code promotionnel :

- il faut distinguer achat pour soi et achat a offrir ;
- il faut produire un support cadeau comprehensible ;
- il faut garder un back-office simple pour le gestionnaire ;
- il faut rester low-code-first autour de Drupal Commerce.

## Decision

Le projet traite les prestations a offrir comme un **parcours cadeau** borne, adosse a Drupal Commerce.

Regles retenues :

- une offre peut etre marquee comme **offrable** ou non ;
- la page `Nos offres` doit rendre visible le choix **pour soi / pour offrir** ;
- dans le premier parcours Commerce, ce choix est capture sur la **ligne de commande** des l'ajout au panier ;
- une offre offerte ne doit pas etre modelisee comme un simple coupon marketing ;
- le cadeau doit etre rattache a une commande reelle et a un identifiant unique ;
- la logique de verification terrain sera cadree a part, mais doit rester compatible avec ce parcours.

## Donnees minimales a prevoir

- acheteur ;
- beneficiaire / destinataire ;
- offre concernee ;
- statut cadeau ;
- identifiant unique ;
- date de validite si necessaire ;
- message cadeau optionnel.

L'email du destinataire peut rester optionnel tant qu'un envoi direct au beneficiaire n'est pas explicitement requis.

## Piste low-code prioritaire

La piste a privilegier est :

- Drupal Commerce comme socle ;
- module contrib de type **gift card / voucher** si sa compatibilite est validee ;
- petit ajustement borne seulement si la capture des informations cadeau ou la restitution du support l'exige.

Dans le cadrage actuel, le petit ajustement borne retenu consiste a :

- exposer un booléen `acheter pour offrir` sur le formulaire d'ajout au panier des seules offres offrables ;
- afficher alors les champs beneficiaire / email / message cadeau ;
- laisser les statuts cadeau hors saisie acheteur.

Le projet ne doit pas partir d'emblee sur un custom complet de logique cadeau.

## Statuts minimaux cibles

- achete ;
- emis ;
- utilise ;
- expire ;
- annule ;
- reemis si le besoin est confirme.

## Consequences

- toutes les offres ne sont pas necessairement offrables ;
- le back-office devra distinguer commande, cadeau emis et statut d'usage ;
- la logique cadeau doit rester lisible pour le gestionnaire et pour le pilote ;
- le sujet du justificatif scannable reste un ticket relie mais distinct.
