# ADR-004 - Versionner la configuration Drupal et instruire a part le seed content

## Contexte

Le socle Drupal local est maintenant installe.

Le projet doit pouvoir rejouer proprement entre local, preprod et production :

- modules actives ;
- theme admin ;
- role `gestionnaire` ;
- permissions ;
- futures configurations metier.

En parallele, certains contenus de demarrage peuvent etre necessaires au premier deploiement :

- taxonomies utiles ;
- eventuels nodes de base ;
- aides embarquees ;
- autres contenus structurels.

Issue liee :

- `#7 Mettre en place la strategie de configuration exportable Drupal`

## Decision

Versionner la **configuration Drupal** via le mecanisme standard d'export/import dans :

- `config/sync/`

Ne pas melanger cette configuration avec les contenus editoriaux ordinaires.

Les contenus utiles au tout premier deploiement doivent etre traites comme un sujet distinct de **seed content** a instruire explicitement.

## Alternatives ecartees

- laisser la configuration vivre seulement en base locale ;
- utiliser la configuration Drupal pour "porter" des contenus editoriaux ordinaires ;
- reporter entierement la question des contenus initiaux sans la tracer.

## Consequences

- les modules actifs, roles et permissions deviennent exportables et versionnables ;
- le socle peut etre rejoue plus proprement sur d'autres environnements ;
- la question des contenus initiaux devient un arbitrage visible ;
- il faudra juger explicitement quels contenus valent la peine d'etre industrialises pour le premier deploiement.

## Impact IA

- fichiers a relire : `ADR-003-socle-applicatif-ddev.md`, `05-backoffice-gestionnaire.md`
- lots concernes : architecture Drupal, back-office gestionnaire, deploiement, recette
- risques de duplication : ne pas confondre configuration, contenu editorial et seed content
