# Back-office gestionnaire

## Objectif

Le gestionnaire n'est pas un technicien. Le back-office doit donc etre :

- guide ;
- propre ;
- rassurant ;
- limite aux actions utiles.

## Principe

Le gestionnaire ne doit pas voir "Drupal brut". Il doit voir :

- ses contenus ;
- ses pages ;
- ses ventes ;
- ses clients ;
- ses formulaires ;
- ses taches du jour.

## Roles cibles

### Gestionnaire

- modifier pages et contenus ;
- voir ventes et leads ;
- gerer medias ;
- lancer actions simples.

### Responsable commercial

- suivre commandes ;
- voir clients ;
- appliquer promotions ;
- suivre statuts.

### Administrateur technique

- configuration ;
- modules ;
- dev ;
- maintenance.

## Moment de creation du role gestionnaire

Le role `gestionnaire` doit etre cree :

1. juste apres l'installation Drupal ;
2. apres l'activation du socle admin utile ;
3. avant la construction des premieres fonctionnalites metier.

Il ne faut pas attendre la fin du projet.

Sinon :

- les parcours sont testes avec un compte trop puissant ;
- les permissions deviennent un rattrapage tardif ;
- la documentation gestionnaire ne colle plus au reel.

## Strategie de permissions

Le role `gestionnaire` doit partir avec des droits minimaux.

Puis, a chaque nouvelle fonctionnalite :

1. ajouter seulement les permissions necessaires ;
2. tester le parcours avec un compte `gestionnaire` ;
3. documenter ce que le gestionnaire peut faire ;
4. eviter les permissions trop larges "en attendant".

## Compte de test

Le projet doit maintenir un vrai compte de test `gestionnaire`.

Ce compte sert a :

- valider les ecrans visibles ;
- verifier le vocabulaire du back-office ;
- controler que la documentation embarquee correspond aux permissions reelles.

## Principes UX admin

1. un menu court ;
2. des labels metier ;
3. des formulaires ranges par logique humaine ;
4. des aides contextuelles breves ;
5. des tableaux de bord orientes action.

## Ecrans quotidiens a prevoir

- tableau de bord du jour
- nouvelles ventes
- commandes a traiter
- bons en attente
- clients a relancer
- demandes de contact
- pages principales du site
- medias recents

## Doctrine d'edition

Chaque page doit etre modifiable par :

- ajout / retrait / reordonnancement de blocs ;
- remplacement des textes ;
- remplacement des visuels ;
- edition des CTA ;
- sans ouvrir 12 formulaires differents.

## Regles de simplification

- masquer les champs inutiles ;
- renommer les types et labels avec du vocabulaire metier ;
- preconfigurer les layouts ;
- limiter les variantes ;
- fournir des pages d'exemple duplicables.

## Aides integrees

- textes d'aide courts dans les formulaires ;
- composants "bon usage" ;
- previsualisation ;
- documentation courte liee aux pages critiques.

## Documentation gestionnaire integree

La documentation gestionnaire ne doit pas vivre seulement hors du site.

Elle doit etre :

- integree dans le back-office Drupal ;
- accessible depuis les ecrans utiles ;
- maintenue a jour en permanence avec le produit reel ;
- redigee en langage simple, sans jargon Drupal.

Si une aide back-office doit exister des le premier deploiement, elle peut faire partie du **seed content initial**.

Dans ce cas, elle doit rester :

- courte ;
- stable ;
- identique entre environnements ;
- gerable sans code custom si possible.

## Regles de redaction

La documentation visible par le gestionnaire doit :

- expliquer ou cliquer ;
- expliquer ce que l'on voit a l'ecran ;
- expliquer quoi verifier apres une action ;
- eviter tout vocabulaire technique inutile ;
- ne jamais supposer que le gestionnaire connait Drupal.

## Format recommande

Preferer une documentation courte et embarquee :

- page d'aide d'accueil ;
- aides contextuelles sur les ecrans importants ;
- liens "comment faire" depuis les vues critiques ;
- captures et formulations metier si cela aide vraiment.

Le projet doit d'abord rechercher un mecanisme core/contrib adapte avant toute documentation admin custom.
