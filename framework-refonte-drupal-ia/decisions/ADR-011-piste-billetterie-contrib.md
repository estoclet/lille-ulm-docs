# ADR-011 - Considerer la billetterie contrib comme une piste, pas comme un choix par defaut

## Contexte

Le projet doit pouvoir :

- emettre un support apres achat ;
- gerer les achats a offrir ;
- permettre un controle rapide sur le terrain ;
- rester low-code-first.

Des modules contrib de type **ticketing / billetterie** peuvent couvrir une partie de ce besoin, notamment quand ils apportent deja :

- emission d'un ticket ;
- QR code ;
- validation / consommation ;
- statuts simples.

## Decision

La billetterie contrib est une **piste d'evaluation prioritaire**, mais elle n'est pas retenue par defaut a ce stade.

La logique de reference reste :

- une commande Commerce comme source de verite ;
- un cadeau borne si l'achat est fait pour offrir ;
- un justificatif verifie cote serveur.

Une solution de billetterie contrib ne devra etre retenue que si elle remplit mieux ce besoin **sans** imposer une logique evenementielle trop lourde pour Lille ULM.

## Critere de choix

Une solution ticketing pourra etre retenue seulement si elle :

1. reste compatible avec Drupal 11 ;
2. s'integre proprement a Drupal Commerce ;
3. couvre l'emission et le controle plus simplement que notre modele borne ;
4. ne degrade pas la lisibilite du back-office ;
5. ne force pas un vocabulaire ou des concepts trop "evenementiels" si le besoin reel est une prestation achetee / offerte / controlee.

## Risque a eviter

Le projet ne doit pas adopter un module de billetterie uniquement parce qu'il gere des QR codes.

Le QR code n'est qu'un moyen d'acces rapide au controle.

Si la billetterie introduit trop d'objets, de workflows ou de contraintes qui ne servent pas Lille ULM, elle devra etre ecartee.

## Consequences

- la piste ticketing doit etre evaluee avant un custom trop vite decide ;
- mais elle ne doit pas renverser la doctrine cadeau / justificatif deja posee ;
- le ticket #14 devra garder cette comparaison explicite avant toute implementation applicative.
