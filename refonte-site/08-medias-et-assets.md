# Medias et assets

## Vue d'ensemble

Le site contient a la fois :

- des medias metier utiles a reprendre ;
- des miniatures generees par `PhocaGallery` ;
- des assets techniques lies a Joomla et aux extensions ;
- quelques images specifiques au parcours commercial historique.

## Repartition observee dans `images/`

Volumes bruts releves par premier niveau :

- `phocagallery` : 264 fichiers image
- `stories` : 42 fichiers image
- `M_images` : 32 fichiers image
- `smilies` : 7 fichiers image
- `bon` : 5 fichiers image
- `banners` : 4 fichiers image
- `emailbon` : 2 fichiers image

## Lecture utile pour la refonte

Ces 264 fichiers `phocagallery` ne correspondent pas a 264 photos uniques :

- la base reference 65 images publiees ;
- le systeme genere plusieurs miniatures par image ;
- il faut distinguer les originaux des thumbs avant toute reprise.

## Galerie : repartition par sous-dossier

Sous `images/phocagallery/` :

- `avion` : 113 fichiers
- `vue` : 97 fichiers
- `atterrissage` : 36 fichiers
- `pilote` : 18 fichiers

Lecture :

- le dossier `avion` porte probablement le plus gros volume d'assets ;
- `vue` correspond au point fort experience / emotion ;
- `pilote` est faible en volume mais important en incarnation de marque.

## Medias marketing identifies hors galerie

### Home / vente

- `images/stories/IMG_0108.JPG`
- `images/stories/logo_credit_agricole.jpg`
- visuels du slider et de storytelling

### Video

- iframe Facebook embarquee :
  - `https://www.facebook.com/plugins/video.php?...2247570525258144...`

### Paiement / bons

- `images/paypal.png`
- `images/wire_transfer_eur_big.png`
- plusieurs visuels dans `images/bon/`
- plusieurs visuels dans `images/emailbon/`

Ces fichiers laissent supposer l'existence d'un dispositif de bon cadeau / confirmation visuelle a verifier lors d'une iteration dediee.

## Assets a faible valeur de reprise

- `M_images`
- `smilies`
- icones techniques `*_f2.png`
- visuels de banners techniques
- assets generiques Joomla / extensions

## Recommandations de reprise media

1. Exporter la liste des 65 images source referencees en base avant tout tri.
2. Ne pas reprendre les miniatures generees.
3. Qualifier les visuels marketing hors galerie :
   - home
   - paiement
   - bons cadeaux
   - email transactionnel
4. Isoler les images purement techniques et les exclure du futur DAM.

## Iteration suivante recommandee

- produire une matrice `fichier -> usage -> page -> conserver ?`
- verifier si la video Facebook actuelle doit etre reprise telle quelle, remplacee ou remontee proprement dans la cible
- relever les dimensions et poids des visuels repris
- etablir une liste courte des photos hero possibles pour la future UI
