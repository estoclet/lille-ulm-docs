# ADR-016 - Modele minimal de reservation de creneau

## Contexte

Le besoin de reservation de creneaux est confirme.

Un premier arbitrage a deja ete valide :

- la selection du creneau doit se faire **pendant l'achat** ;
- le gestionnaire doit pouvoir agir ensuite sur une reservation deja datee ;
- la meteo peut aider a decider si un creneau reserve doit etre maintenu ou reporte.

Il faut maintenant borner un modele simple, compatible avec Commerce, sans recreer un agenda legacy complet.

## Decision

Le modele cible initial retient les principes suivants :

- seules les offres marquees comme **reservables** demandent un creneau ;
- l'acheteur choisit son creneau **pendant le parcours d'achat** ;
- le creneau retenu est rattache a la **ligne de commande**, pas a la commande globale ;
- la reservation devient definitive lorsque la commande est **placee** ;
- une protection temporaire doit eviter qu'un meme creneau soit choisi en parallele pendant un checkout ;
- le gestionnaire peut ensuite **reporter** ou **reaffecter** une reservation si les conditions l'imposent.

Le premier niveau d'interface cible est une **selection guidee de disponibilites**, pas un agenda public generique de type `JEvents`.

## Pourquoi ce choix

- la ligne de commande est le bon niveau quand une meme commande peut contenir plusieurs achats ;
- une offre cadeau, une offre reservable et une offre non reservable peuvent coexister plus facilement ;
- la selection pendant l'achat reduit la friction apres paiement ;
- la reservation definitive a la commande placee evite de traiter un simple panier comme une reservation certaine ;
- la selection guidee repond au besoin metier sans imposer un vrai moteur evenementiel public.

## Objets minimaux a couvrir

### Offre reservable

- propriete simple sur l'offre ;
- permet de distinguer les offres qui demandent un creneau de celles qui n'en demandent pas ;
- garde ouverte une exception future pour certains bons cadeaux.

### Creneau

- ressource metier date / heure geree cote serveur ;
- ouverte ou fermee par le gestionnaire ;
- associee aux offres ou categories d'offres concernees si necessaire ;
- capacite minimale initiale : **1 reservation par creneau**.

### Reservation

- rattachement du creneau choisi a la ligne de commande ;
- etat coherent avec la commande ;
- historique plus riche possible plus tard, mais non obligatoire au tout premier lot.

## Regles minimales

- un creneau indisponible ne doit pas pouvoir etre reserve une seconde fois ;
- la source de verite des disponibilites reste cote serveur ;
- une commande abandonnee ne doit pas bloquer indefiniment un creneau ;
- le gestionnaire doit pouvoir voir les reservations a venir et agir dessus simplement ;
- un report doit mettre a jour la reservation sans perdre le lien avec l'achat ;
- la meteo reste une aide a la decision de report, pas une automatisation autonome au premier lot.

## Consequences

- le modele Commerce doit desormais prevoir un rattachement de creneau sur la ligne de commande ;
- une logique de protection temporaire puis de confirmation a la commande placee sera necessaire ;
- le back-office devra proposer une gestion simple des disponibilites, reservations et reports ;
- une fonctionnalite meteo pourra ensuite se brancher sur des reservations deja datees, ce qui lui donne une vraie valeur operationnelle.
