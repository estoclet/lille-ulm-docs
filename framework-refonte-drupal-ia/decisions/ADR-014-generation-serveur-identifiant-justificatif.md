# ADR-014 - Generer l'identifiant de justificatif cote serveur

## Contexte

Le projet a deja retenu :

- un justificatif verifie cote serveur ;
- un identifiant unique non devinable ;
- des donnees portees sur la ligne de commande ;
- une interdiction de saisie libre de cet identifiant par l'acheteur.

Il reste a borner **quand** et **comment** cet identifiant est cree.

## Decision

L'identifiant de justificatif est **genere cote serveur**, automatiquement, sur la **ligne de commande**, lorsque la commande est **placee**.

Le token :

- n'est pas saisi par l'acheteur ;
- n'est pas genere au simple stade panier ;
- doit etre difficile a deviner ;
- doit pouvoir servir plus tard de base a un lien de verification ou a un QR code.

## Pourquoi ce choix

- un panier ne vaut pas justificatif ;
- la commande placee est un premier point metier plus solide que l'ajout au panier ;
- cela prepare la suite sans figer trop tot la logique complete d'emission ;
- le projet garde la possibilite de lier plus tard la vraie validation a un evenement de paiement ou d'emission explicite.

## Regles

- generer un token aleatoire non devinable ;
- garantir son unicite pratique a l'echelle des lignes de commande ;
- ne pas exposer ce token en saisie sur les formulaires acheteur ;
- ne pas marquer automatiquement le justificatif comme `valide` tant que la regle d'emission finale n'est pas arretee ;
- considerer ce token comme un identifiant technique serveur, pas comme un document visuel.

## Consequences

- le support scannable pourra plus tard s'appuyer sur cet identifiant ;
- la page ou l'API de verification pourront etre ajoutees ensuite sans remettre en cause la structure ;
- le projet evite une emission prematuree de justificatif sur un panier non finalise ;
- le back-office peut afficher l'identifiant sans le laisser vivre comme une saisie libre.
