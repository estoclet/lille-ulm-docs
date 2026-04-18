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

La toolbar doit raconter la meme histoire que le tableau de bord :

- memes mots ;
- memes points d'entree utiles ;
- pas de proliferation de rubriques Drupal natives incomprehensibles pour le
  gestionnaire.

Pour le role `gestionnaire`, la navigation `Lille ULM` doit devenir l'entree
principale en toolbar. Une entree generique de type `Administration` ne doit pas
venir concurrencer ce repere metier.

Par coherence, les points d'entree Drupal generiques doivent eux aussi retomber
sur les reperes Lille ULM quand ils concernent le gestionnaire :

- `/admin` doit renvoyer vers le tableau de bord Lille ULM ;
- `/admin/help` doit renvoyer vers l'aide metier Lille ULM.

Les autres onglets toolbar doivent etre reduits au strict necessaire :

- `Retour au site` ;
- le menu de compte utilisateur ;
- aucun autre onglet natif Drupal ou Commerce si son sens n'est pas evident pour
  le gestionnaire.

En pratique, cela implique deux regles de rendu :

- le tray `Lille ULM` doit reprendre les memes rubriques que le tableau de bord
  (`Actions rapides`, `Pages cles`, `Blocs cles`, `Contenus`, `Commerce`,
  `Pilotage`) ;
- l'aside `Admin Toolbar` natif doit etre masque pour le role `gestionnaire`,
  sinon il reintroduit des entrees Drupal/Commerce concurrentes et parfois en
  anglais.

## Socle initial livre

Premier niveau concret a maintenir dans le produit :

- un tableau de bord `gestionnaire` sous `/admin/lille-ulm` ;
- une entree toolbar `Lille ULM` coherente avec ce tableau de bord ;
- une entree `Actions rapides` pour creer une page, une offre ou un media sans
  passer par les listes Drupal ;
- une entree `Pages cles` avec acces direct a l'accueil, au contact, a la page
  localisation, a la FAQ et a la galerie ;
- une entree `Blocs cles` avec acces direct au hero de la home et au bandeau
  contact ;
- trois entrees de lecture simples : `Contenus`, `Commerce`, `Pilotage` ;
- une entree `Offres actives` avec acces direct aux offres publiees actuellement
  vendues en ligne ;
- des liens utiles vers pages et contenus, medias, aide, commandes, offres,
  creneaux, meteo, formulaires ;
- un role `gestionnaire` qui peut acceder a ces ecrans sans basculer en profil
  administrateur technique.

Ce socle est volontairement court. Chaque nouvelle fonctionnalite doit ensuite
ajouter son propre point d'entree utile dans ce tableau de bord ou dans la
navigation admin existante, sans casser les reperes deja appris.

## Perimetre d'audit UX/UI gestionnaire

Quand le lot back-office sera considere comme suffisamment stabilise, l'audit
UX/UI devra couvrir au minimum, en desktop et en mobile :

- le tableau de bord `/admin/lille-ulm` ;
- la toolbar finale visible par le role `gestionnaire` ;
- la liste `Pages et contenus` ;
- la creation et l'edition d'une page ;
- l'edition des blocs cles (hero, bandeau contact) ;
- la liste des commandes ;
- la liste des offres, la creation d'une offre et l'edition d'une offre ;
- la liste des creneaux ;
- l'ecran meteo ;
- la liste des medias et l'ajout d'un media ;
- la liste des formulaires ;
- la page d'aide accessible au gestionnaire.

L'objectif n'est pas seulement de verifier que chaque page est accessible, mais
de confirmer que le gestionnaire comprend quoi faire sans connaissance Drupal
prealable.

Avant de lancer l'audit complet, il faut verrouiller deux prealables :

- verifier que chaque surface cible est bien accessible au role `gestionnaire` ;
- valider une chaine de captures desktop et mobile sur des ecrans reels.

Le socle minimum verifie a ce stade couvre deja :

- tableau de bord et aide Lille ULM ;
- liste des contenus, creation de page et edition de page ;
- edition des blocs cles ;
- listes commandes, offres, creneaux, medias et formulaires ;
- creation d'offre, ajout de media et ecran meteo.

La chaine de capture locale a deja ete validee sur le tableau de bord et sur la
page d'aide, en desktop et en mobile. Le reste de l'audit doit reutiliser cette
meme logique de preuve visuelle.

## Constats du premier audit visuel

Les captures desktop et mobile montrent que le socle Lille ULM devient lisible
sur le tableau de bord, l'aide, les listes de contenus, les medias et le bandeau
contact. La logique par cartes et liens directs fonctionne, et le gestionnaire
peut reperer rapidement ses entrees utiles sans comprendre Drupal.

Les premiers irritants UX/UI visibles sont toutefois deja clairs :

- en mobile, les captures prises avec la navigation ouverte montrent qu'il faut
  aussi verifier chaque ecran en etat `contenu visible`, pas seulement en etat
  `menu ouvert` ;
- plusieurs listes Commerce restent trop brutes pour un gestionnaire non
  drupaliste : le nettoyage des actions locales natives a deja supprime
  `Commerce inbox`, `Add product` et `Create a new order`, puis les listes
  Produits et Commandes ont ete relabellisees en francais avec un repere de
  retour `Retour au back-office Lille ULM` ;
- la navigation restait encore incoherente tant que le tray Lille ULM et
  l'`Admin Toolbar` natif racontaient deux histoires differentes ; le tray doit
  donc reprendre les memes rubriques que le tableau de bord et le menu natif
  etre neutralise pour le gestionnaire ;
- la creation et l'edition d'une page ont deja ete resserrees autour de
  l'essentiel avec un repere Lille ULM, moins de sections techniques et un
  historique interne replie, mais le rendu reste encore tres minimaliste ;
- le hero a encore des champs de lien assez techniques, mais il est maintenant
  resserre autour du titre, du sous-titre, de l'image de fond, des deux CTA et
  d'un historique interne simplifie ;
- l'ajout de media a ete nettoye autour du fichier a importer et de la
  publication, avec un repere Lille ULM et sans les sections auteur/version
  inutiles au gestionnaire ;
- meme quand les parcours deviennent clairs, le back-office reste trop triste
  et sans ame si on laisse Gin brut : il faut une couche visuelle plus
  chaleureuse sur les titres, reperes de retour, cartes et aides contextuelles.

Trois blocages critiques sont deja observes dans ce premier audit :

- creation d'offre impossible car Commerce affiche `Products can't be created
  until a store has been added` ;
- liste des creneaux en erreur fatale `Object of class Drupal\\Core\\Url could not
  be converted to string` ;
- ecran meteo pollue par des warnings `Array to string conversion`.

Ordre de correction recommande apres cet audit :

1. corriger tous les ecrans en erreur ou bloques ;
2. retirer les libelles anglais et les reperes Drupal/Commerce inutiles ;
3. ajouter du guidage metier sur les formulaires encore trop nus ;
4. donner une identite visuelle plus chaleureuse aux ecrans gestionnaire sans
   casser Gin ;
5. refaire une passe de captures mobiles sur le contenu reel des pages, menu
   referme.

Les trois blocages techniques du premier audit ont deja ete leves :

- la liste des creneaux s'affiche de nouveau ;
- l'ecran meteo ne remonte plus de warnings ;
- la creation d'offre remarche apres remise en place d'un store par defaut et
  des droits de lecture minimaux sur le store.

Depuis, une passe de coherence navigation + apparence a aussi ete ajoutee :

- le tray `Lille ULM` reprend maintenant les memes familles d'actions que le
  tableau de bord ;
- l'`Admin Toolbar` natif est masque pour le role `gestionnaire` ;
- une premiere couche visuelle rend les pages moins froides : fond admin plus
  doux, header/breadcrumb plus incarnes, cartes Lille ULM plus vivantes et
  aides contextuelles mieux mises en valeur.

Une deuxieme passe visuelle commence aussi a donner plus d'ame aux ecrans du
quotidien :

- des bandeaux d'introduction contextualises apparaissent en tete des pages
  clefs ;
- ces bandeaux redonnent un ton editorial simple a des ecrans auparavant tres
  froids, comme les Offres ou l'ajout de media ;
- chaque bandeau rappelle le sens de la page et propose des raccourcis utiles
  plutot qu'un simple titre technique.

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

Quand cela aide vraiment un gestionnaire non technicien, cette aide peut aussi
inclure des captures d'ecran utiles :

- centrees sur les reperes visuels et les actions a faire ;
- limitees aux ecrans critiques ;
- relues en version desktop et mobile.

Le choix de la base d'aide integree est documente dans `decisions/ADR-006-aide-gestionnaire-backoffice.md`.

## Documentation gestionnaire integree

La documentation gestionnaire ne doit pas vivre seulement hors du site.

Elle doit etre :

- integree dans le back-office Drupal (page d'aide, aides contextuelles, liens "comment faire") ;
- accessible depuis les ecrans utiles ;
- maintenue a jour en permanence avec le produit reel ;
- redigee en langage simple, sans jargon Drupal (expliquer ou cliquer, quoi verifier apres une action).

Quand une page d'aide integree existe, elle doit rester courte mais actionnable :

- quelques reperes de lecture ;
- des liens directs vers les ecrans utiles ;
- pas de documentation longue qui remplace la clarte de l'interface.

Si une aide doit exister des le premier deploiement, elle fait partie du **seed content initial** : courte, stable, identique entre environnements, sans code custom si possible.

Le projet doit d'abord rechercher un mecanisme core/contrib adapte (voir ADR-006) avant toute documentation admin custom.
