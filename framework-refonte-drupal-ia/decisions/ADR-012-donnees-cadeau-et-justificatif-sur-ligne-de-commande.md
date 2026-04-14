# ADR-012 - Porter les donnees cadeau et justificatif sur la ligne de commande

## Contexte

Le projet doit stocker :

- les informations cadeau ;
- l'identifiant de justificatif ;
- les statuts de suivi associes.

Il faut choisir ou vivent ces donnees :

- sur la commande ;
- ou sur la ligne de commande.

## Decision

Les donnees **cadeau** et **justificatif** vivent sur la **ligne de commande**.

La commande reste la racine transactionnelle, mais la ligne de commande porte les informations propres a chaque achat effectif.

## Pourquoi ce choix

- une commande peut contenir plusieurs achats ;
- toutes les lignes d'une meme commande ne sont pas necessairement offrables ;
- chaque ligne peut avoir son propre beneficiaire ;
- chaque ligne peut avoir son propre identifiant de justificatif ;
- le modele reste compatible avec une future verification ou consommation unitaire.

## Donnees minimales portees par la ligne

- beneficiaire ;
- email du beneficiaire si utile ;
- message cadeau ;
- statut cadeau ;
- identifiant de justificatif ;
- statut justificatif.

## Regle

Ne pas porter ces donnees au niveau commande tant qu'un vrai besoin transversal a toute la commande n'est pas etabli.

## Consequences

- la commande reste lisible ;
- le modele supporte mieux les cas multi-achats ;
- le futur back-office pourra suivre cadeau et justificatif a un niveau plus fin ;
- le projet evite de devoir redescendre plus tard d'un niveau commande vers un niveau ligne.
