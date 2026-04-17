# Back-office gestionnaire

## Objectif

Le gestionnaire n'est pas un technicien et ne connait pas Drupal. Le back-office
doit donc etre :

- guide ;
- propre ;
- rassurant ;
- limite aux actions utiles.
- comprehensible sans formation Drupal.

## Principe

Le gestionnaire ne doit pas voir "Drupal brut". Il doit voir :

- ses contenus ;
- ses pages ;
- ses ventes ;
- ses clients ;
- ses formulaires ;
- ses taches du jour.

Le back-office gestionnaire ne doit pas se reduire a une seule page de type
`/admin/content`. Un usage quotidien e-commerce demande plusieurs points d'entree
simples, orientes action et accessibles sans connaissances Drupal.

## Architecture modulaire

Le back-office doit etre compose de briques activables et extensibles au fil des
fonctionnalites :

- socle de navigation admin clair ;
- tableau de bord d'accueil ;
- ecrans metier par domaine : contenus, medias, commandes, clients, formulaires,
  meteo, creneaux ;
- widgets ou raccourcis ajoutables sans refonte globale.

Regle :

1. ajouter un ecran utile quand une nouvelle fonctionnalite apparait ;
2. reutiliser d'abord core + contrib ;
3. accepter une couche low-code si le contrib seul ne suffit pas ;
4. garder une navigation stable meme quand le perimetre grandit ;
5. eviter un back-office monolithique ou une page unique surchargee.

## Socle contrib a privilegier

Base deja coherente dans ce projet :

- Gin pour l'interface admin ;
- Admin Toolbar pour une navigation courte et rapide ;
- Media Library pour les medias ;
- Webform pour les formulaires ;
- Drupal Commerce pour les ecrans commandes / produits / clients.

Pistes contrib a investiguer prioritairement selon le besoin reel :

- un tableau de bord admin composable a partir de blocs et de Views ;
- un module de dashboard commerce si sa compatibilite et sa maintenance sont solides ;
- Views Bulk Operations pour les actions de masse simples ;
- Workbench Access seulement si la segmentation des acces editoriaux devient
  necessaire.

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

La recette UX/UI du back-office ne doit pas se limiter a une verification
fonctionnelle. Chaque page destinee au gestionnaire doit etre relue sur
screenshots :

- en desktop ;
- en mobile ;
- avec une attention specifique a la lisibilite, a la hierarchie visuelle et a la
  clarte des actions.

## Principes UX admin

1. un menu court ;
2. des labels metier ;
3. des formulaires ranges par logique humaine ;
4. des aides contextuelles breves ;
5. des tableaux de bord orientes action.

## Socle initial livre

Premier niveau concret a maintenir dans le produit :

- un tableau de bord `gestionnaire` sous `/admin/lille-ulm` ;
- trois entrees de lecture simples : `Contenus`, `Commerce`, `Pilotage` ;
- des liens utiles vers pages et contenus, medias, aide, commandes, offres,
  creneaux, meteo, formulaires ;
- un role `gestionnaire` qui peut acceder a ces ecrans sans basculer en profil
  administrateur technique.

Ce socle est volontairement court. Chaque nouvelle fonctionnalite doit ensuite
ajouter son propre point d'entree utile dans ce tableau de bord ou dans la
navigation admin existante, sans casser les reperes deja appris.

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

Exemples prioritaires :

- le bloc hero de la home doit exposer dans un seul formulaire le titre, le
  sous-titre, l'image, le CTA principal et le CTA secondaire ;
- le bandeau contact doit exposer l'accroche, les horaires, le numero tel: et le
  numero affiche ;
- dans les deux cas, les champs techniques parasites ne doivent pas etre visibles
  pour le gestionnaire.

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

Le choix de la base d'aide integree est documente dans `decisions/ADR-006-aide-gestionnaire-backoffice.md`.

## Documentation gestionnaire integree

La documentation gestionnaire ne doit pas vivre seulement hors du site.

Elle doit etre :

- integree dans le back-office Drupal (page d'aide, aides contextuelles, liens "comment faire") ;
- accessible depuis les ecrans utiles ;
- maintenue a jour en permanence avec le produit reel ;
- redigee en langage simple, sans jargon Drupal (expliquer ou cliquer, quoi verifier apres une action).

Si une aide doit exister des le premier deploiement, elle fait partie du **seed content initial** : courte, stable, identique entre environnements, sans code custom si possible.

Le projet doit d'abord rechercher un mecanisme core/contrib adapte (voir ADR-006) avant toute documentation admin custom.
