# ADR-015 - Reservation de creneaux parmi des disponibilites gerees par le gestionnaire

## Contexte

Le projet ne doit pas seulement vendre une prestation.

Le besoin metier confirme est le suivant :

- le gestionnaire choisit les creneaux date/heure qu'il rend disponibles ;
- l'acheteur reserve un creneau parmi ces disponibilites ;
- un creneau reserve n'est plus disponible pour une autre reservation.

Le site cible doit donc couvrir un vrai besoin de **reservation de creneau**, sans reconduire `JEvents` comme moteur vivant.

## Decision

Le projet doit integrer une **reservation de creneau** dans le parcours cible.

Doctrine retenue :

- les disponibilites sont ouvertes par le gestionnaire ;
- la reservation porte sur un creneau date/heure explicite ;
- un creneau reserve devient indisponible ;
- le besoin doit etre reconstruit dans Drupal, pas migre a l'identique depuis `JEvents` ;
- l'agenda public legacy n'est pas la cible fonctionnelle.

## Regles minimales

- le creneau est une ressource metier, pas un simple texte libre ;
- la source de verite des disponibilites doit rester cote serveur ;
- la prevention du double booking est obligatoire ;
- le back-office doit permettre au gestionnaire d'ouvrir, fermer et suivre les creneaux ;
- la reservation doit s'articuler avec la commande et non vivre dans un systeme parallele.

## Suite du cadrage

Le premier modele cible detaille est documente dans :

- `ADR-016-modele-minimal-reservation-de-creneau.md`

Il fixe comme direction initiale :

- reservation pendant l'achat ;
- portage sur la ligne de commande ;
- offres reservables seulement si elles sont explicitement marquees comme telles ;
- selection guidee de disponibilites plutot qu'un agenda public generique ;
- possibilite de report ulterieur par le gestionnaire.

## Consequences

- le projet a maintenant un besoin agenda / disponibilites confirme ;
- `JEvents` reste une source legacy eventuelle, pas une brique cible ;
- le modele Commerce devra s'articuler avec des disponibilites et une logique anti-conflit ;
- un lot dedie de modelisation et d'implementation devient necessaire.
