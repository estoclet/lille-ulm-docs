# ADR-006 - Demarrer l'aide gestionnaire avec le core Help

## Contexte

Le projet doit integrer une aide exploitable par un gestionnaire non technicien directement dans le back-office Drupal.

La doctrine projet impose :

1. core d'abord ;
2. contrib ensuite ;
3. custom en dernier recours.

Le socle actuel confirme deja :

- module core `help` actif ;
- route `/admin/help` disponible ;
- bloc `Help` deja place dans le theme admin Gin ;
- role `gestionnaire` a completer pour acceder a cette aide.

## Decision

Le premier niveau d'aide integree du projet repose sur le **core Help**.

La base retenue est :

- pages d'aide accessibles via `/admin/help` ;
- bloc d'aide contextuelle deja present dans l'admin Gin ;
- permission `access help pages` accordee au role `gestionnaire`.

Le projet ne retient pas, a ce stade, de module contrib d'aide plus riche tant qu'un besoin concret ne le justifie pas.

## Pourquoi ce choix

- solution deja presente et verifiee ;
- aucun custom requis ;
- faible cout de maintenance ;
- compatible avec l'objectif de langage simple et d'aide embarquee progressive ;
- laisse la porte ouverte a un contrib plus riche plus tard si les limites deviennent reelles.

## Ce que cela couvre

- un point d'entree d'aide visible dans l'administration ;
- une base contextuelle sur les ecrans admin couverts par le core ou les modules actifs ;
- un premier niveau d'autonomie pour le gestionnaire.

## Ce que cela ne couvre pas encore

- tutoriels metier pas a pas specifiques a Lille ULM ;
- aides redigees sur mesure pour chaque ecran critique ;
- parcours guides plus riches.

Ces besoins devront d'abord faire l'objet d'une nouvelle recherche core/contrib avant toute implementation custom.

## Consequences

- le role `gestionnaire` doit garder l'acces aux pages d'aide ;
- le helper local d'installation doit reproduire ce droit ;
- les futures aides metier pourront etre ajoutees par couches successives sans changer la doctrine de base.
