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

Une troisieme passe visuelle peut maintenant etre consideree comme engagee :

- chaque grande famille de pages peut recevoir une ambiance plus distincte
  (`Contenus`, `Commerce`, `Media`, `Pilotage`) au lieu d'un rendu uniforme ;
- les titres, bandeaux et tableaux gagnent en relief avec des accents de couleur
  coherents par domaine ;
- les listes du quotidien paraissent moins ternes des qu'on assume cette
  logique de sections visuelles plutot qu'un admin monochrome.

Une quatrieme passe devient ensuite pertinente sur les formulaires :

- les ecrans d'edition ne doivent plus donner l'impression d'un empilement brut
  de champs ;
- les blocs de formulaire, les zones repliables et les barres d'actions peuvent
  prendre un rendu plus editorial et plus doux sans nuire a la lecture ;
- cette couche est particulierement utile sur l'edition de page, le hero et les
  medias, qui restaient encore visuellement tres plats.

Le tableau de bord et l'aide meritent aussi un soin visuel propre, car ils
donnent le ton de tout le back-office :

- leurs sections peuvent porter un sous-repere court et une ambiance plus
  marquee selon la famille d'action ;
- cela evite l'effet "grille uniforme" et aide a distinguer plus vite ce qui
  releve de l'edition, du commerce, du pilotage ou des acces rapides ;
- ce traitement est pertinent tant que le rendu reste sobre et ne concurrence
  pas la lisibilite des liens.

### Audit cible des pages d'edition de node

Les captures et le HTML rendu sur `node/add/page` et `node/10/edit` montrent
que la base UX s'est nettement assainie :

- intro contextuelle claire ;
- repere Lille ULM court et utile ;
- historique interne replie ;
- zone d'actions ramenee a `Enregistrer` et `Apercu`.

Mais l'UI des formulaires node garde encore plusieurs faiblesses visibles :

- le champ titre sort sans vrai libelle visible et repose surtout sur son
  placeholder ; sur une page vide ou chargee vite, cela affaiblit la hierarchie
  visuelle du formulaire ;
- le corps principal garde une UI de CKEditor tres dominante ; la barre
  d'outils, le select `Basic HTML` et le lien `A propos des formats de texte`
  prennent encore trop de place par rapport au geste editorial attendu d'un
  gestionnaire ;
- le champ `Contenu principal` n'apparait pas comme un bloc editorial fort : il
  est precede d'un wrapper technique de resume et d'un libelle parasite
  `Modifier le resume`, ce qui brouille la lecture ;
- la creation et l'edition tombent tres vite sur une pile verticale de cartes
  semblables ; le rendu est plus joli qu'avant, mais la progression visuelle
  reste monotone quand on descend dans la page ;
- les actions `Enregistrer` et `Apercu` ont encore un poids graphique trop
  proche ; l'action principale ressort mieux qu'avant mais l'oeil ne comprend pas
  encore instantanement quelle action clot normalement le parcours ;
- sur petit ecran, l'intro, le repere et l'editeur produisent encore une
  longue colonne avant d'atteindre la barre d'actions, ce qui fatigue la lecture
  du formulaire.

Conclusion de cet audit cible :

- l'UX de fond est correcte ;
- l'UI a ete assainie ;
- mais les pages node n'ont pas encore le niveau de finition visuelle d'une
  interface editoriale vraiment premium et rassurante.

Depuis cet audit cible, une passe corrective a ete ajoutee sur les pages node :

- les titres `Basic page` ont ete nettoyes cote rendu pour ne plus remonter dans
  les pages d'ajout et d'edition ;
- les formulaires page affichent maintenant des reperes visibles
  `Titre de la page`, `Contenu principal` et `Mode d edition`, meme quand le
  theme admin ne rend pas correctement les labels Drupal ;
- `Modifier le resume` disparait de l'ecran gestionnaire ;
- `Basic HTML` et `Full HTML` sont reformules en `Edition standard` et
  `Edition avancee`, avec une aide plus douce ;
- le bouton `Apercu` retombe visuellement en secondaire ;
- l'editeur principal prend un rendu plus editorial, moins brut et mieux
  hierarchise ;
- la meme passe inclut enfin un vrai resserrement mobile sur les formulaires,
  les bandeaux d'introduction, les barres d'actions, le dashboard et le tray
  toolbar.

Une passe equivalente est aussi devenue necessaire sur les formulaires d'offre
Commerce (`/product/add/default`, `/product/*/edit`) :

- l'ajout ne doit plus remonter comme `Ajouter product` ;
- l'edition doit assumer une lecture metier `Modifier l offre ...` ;
- les champs clefs doivent ressortir visiblement (`Nom de l offre`, `Duree`,
  `Phrase de reassurance`, `Ordre d affichage`, `Description de l offre`) ;
- la meta secondaire Commerce ne doit pas concurrencer la lecture principale ;
- l'aide CKEditor et les formats de texte doivent etre reformules comme sur les
  pages node (`Edition standard`, `Edition avancee`) ;
- les ecrans d'offre doivent toujours porter la tonalite visuelle `Commerce`,
  y compris en edition, sans retomber par erreur dans la famille `Contenus`.

Une passe du meme ordre reste utile sur la liste des commandes
(`entity.commerce_order.collection`) :

- les filtres ne doivent pas rester comme des champs nus sans repere visible ;
- l'action de masse doit etre compréhensible sans vocabulaire Drupal/Commerce
  anglais (`Supprimer la commande`, `Debloquer la commande`) ;
- le bouton de ligne principal gagne a etre lu comme une action claire
  (`Ouvrir`) plutot qu'un verbe generique ;
- les etats de commande meritent un rendu immediatement scannable avec une
  pastille et une couleur, pas seulement du texte dans une cellule ;
- la colonne client doit aider a distinguer vite le nom et l'email ;
- en mobile, filtres et actions de masse doivent se replier en pile sans
  casser la lecture du tableau.

La liste des creneaux (`entity.lille_ulm_reservation_slot.collection`) demande
elle aussi une lecture metier explicite :

- le titre de page ne doit pas remonter comme `Entites Creneaux de reservation` ;
- les filtres doivent etre lisibles sans supposer la connaissance du formulaire
  (`Statut`, `Du`, `Au`) ;
- l'action principale de ligne peut rester `Modifier`, mais le split button doit
  annoncer clairement `Plus d actions` ;
- les statuts de creneau gagnent a etre scannables avec une pastille simple
  (`Ouvert`, `Reserve`, `Ferme`) ;
- l'historique des reports ne doit pas dupliquer la date en anglais et en
  francais dans la meme cellule ;
- en mobile, les filtres doivent se replier en pile propre plutot qu'en ligne
  compacte et fragile.

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
