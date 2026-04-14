# ADR-009 - Justificatif d'achat controlable par verification serveur

## Contexte

Le client veut qu'un pilote puisse verifier rapidement sur le terrain qu'une prestation a bien ete achetee, sans se contenter d'un document facile a copier.

Le besoin porte sur :

- un justificatif simple a presenter ;
- un controle rapide pour le pilote ;
- un statut clair apres verification ;
- une compatibilite avec les achats pour soi et les achats a offrir.

## Decision

Le justificatif d'achat repose sur :

- un **identifiant unique non devinable** ;
- un **controle serveur** comme source de verite ;
- un **support scannable** de type QR code comme acces rapide privilegie.

Le QR code n'est pas considere comme une preuve suffisante en lui-meme.

Il doit simplement ouvrir ou transmettre un moyen de verifier en temps reel un statut cote serveur.

## Parcours cible

1. apres paiement, le systeme emet un justificatif ;
2. ce justificatif contient un identifiant unique et un acces scannable ;
3. le pilote scanne ;
4. il voit immediatement un statut simple ;
5. si besoin, il confirme l'usage ou la consommation.

## Statuts minimaux a afficher

- valide ;
- deja utilise ;
- annule ;
- expire ;
- introuvable / invalide.

## Regles de conception

- ne jamais baser la confiance sur un simple PDF ou une simple image ;
- la verification doit etre faisable en quelques secondes sur mobile ;
- le vocabulaire vu par le pilote doit etre tres simple ;
- la consommation doit laisser une trace exploitable par le gestionnaire ;
- la logique doit rester compatible avec un parcours cadeau.

## Piste low-code prioritaire

La piste a privilegier est :

- Drupal Commerce comme socle de vente ;
- module contrib de type QR code pour la generation du support scannable ;
- ajustement borne uniquement pour la page ou le flux de verification si le contrib ne couvre pas assez le besoin.

Le projet ne doit pas partir sur une solution de justificatif purement visuelle ou hors serveur.

## Consequences

- le back-office devra suivre le statut de verification / usage ;
- le pilote aura besoin d'un acces simple a l'ecran de controle ;
- le sujet est lie aux cadeaux, mais reste valable pour toute prestation achetee.
