# ADR-005 - Seed content initial minimal et contrib-first

## Contexte

Le projet distingue maintenant clairement :

- la configuration Drupal versionnee ;
- les contenus editoriaux ordinaires ;
- les contenus de demarrage utiles au premier deploiement.

Le besoin exprime est de juger si certains contenus doivent etre industrialises pour le premier passage en preprod puis en production.

Le projet suit une doctrine **low-code-first** :

1. verifier le core Drupal ;
2. verifier les modules contrib ;
3. n'envisager du custom qu'en dernier recours.

## Decision

Le projet retient une doctrine de **seed content minimal**.

Seuls doivent etre versionnes comme seed content les contenus qui remplissent simultanement ces criteres :

1. indispensables au tout premier deploiement ;
2. stables ou faiblement evolutifs ;
3. identiques d'un environnement a l'autre ;
4. penibles ou risques a recreer manuellement ;
5. distincts de la configuration Drupal.

## Perimetre cible

Peuvent entrer dans ce perimetre :

- taxonomies de reference necessaires au fonctionnement ;
- contenus d'aide back-office utiles des le premier jour ;
- quelques contenus structurels si le site en depend pour etre lisible ou exploitable ;
- eventuels exemples strictement utiles au parcours gestionnaire.

Ne doivent pas entrer dans ce perimetre :

- contenus marketing courants ;
- offres, textes commerciaux et visuels amenes a bouger souvent ;
- actualites ;
- commandes, clients, leads, soumissions de formulaires ;
- medias alimentes au fil de l'eau ;
- tout contenu editorial simple a saisir manuellement sans risque.

## Mise en oeuvre recommandee

### Ordre de recherche

1. utiliser la configuration Drupal standard pour tout ce qui releve de la structure ;
2. etudier un module contrib adapte pour les contenus de demarrage ;
3. ne pas partir sur une mecanique lourde de synchronisation cross-environnements sans besoin reel.

### Piste privilegiee

Pour ce projet, la piste privilegiee est :

- **configuration core** pour la structure ;
- **module contrib de type Default Content** pour les rares contenus entities a versionner ;
- **aides integrees** via mecanisme core/contrib dedie avant toute solution custom.

### Pistes ecartees a ce stade

- synchronisation continue de contenus entre environnements ;
- outillage lourd type deploiement editorial multi-sites ;
- industrialisation de masse de contenus editoriaux ordinaires.

## Premiere doctrine projet

Au stade actuel, la recommandation est de **ne pas seed-er les pages editoriales ordinaires**.

La premiere cible plausible se limite a :

- taxonomies de reference si elles deviennent necessaires ;
- aide gestionnaire embarquee si elle doit exister des la premiere mise en ligne ;
- eventuels contenus structurels strictement necessaires au bon fonctionnement du parcours initial.

## Consequences

- le depot reste sobre ;
- la frontiere configuration / contenu reste claire ;
- le projet evite de figer inutilement des contenus marketing ;
- le besoin de seed content reste pilote par la valeur de deploiement, pas par confort technique.

## Impact IA

- toujours distinguer `config/sync` des contenus de demarrage ;
- ne jamais proposer de versionner massivement les nodes "par principe" ;
- documenter, pour chaque contenu candidat, pourquoi il doit exister avant intervention du gestionnaire.
