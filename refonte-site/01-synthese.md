# Synthese de l'existant

## Lecture rapide

Le site actuel est un petit site vitrine transactionnel ancien, construit sur Joomla 3, dont le contenu editorial est limite mais dont la valeur metier repose sur trois briques principales :

- la presentation des offres de baptemes et cours ULM ;
- la reservation / achat en ligne historique via `DT Register` ;
- la confiance commerciale construite par la galerie photo, la page de contact et les elements de reassurance.

## Chiffres cles

- 16 articles
- 14 categories
- 125 entrees de menu
- 39 modules
- 292 extensions
- 39 utilisateurs
- 1 fiche contact
- 4004 inscriptions historiques dans `DT Register`
- 250 evenements `JEvents`
- 4 categories `PhocaGallery`
- 65 images `PhocaGallery`

## Fonctionnalites visibles et utiles a la refonte

- Accueil avec slider / storytelling (`RokStories`)
- Navigation principale
- Pages editoriales : tarifs, avion / ULM, FAQ, mentions legales, partenaires, localisation
- Galerie photo par categories
- Formulaire de contact public
- Page "Nous trouver" avec carte Google Maps embarquee
- Vente historique en ligne de bons / seances
- Paiement en ligne mis en avant dans la communication
- Sitemap HTML

## Constat de cadrage

- Le volume de contenu est faible : la refonte peut raisonnablement repartir d'un inventaire manuel page par page.
- Le volume de donnees metier lie a la reservation est au contraire important : il faut traiter la reprise ou l'archivage de `DT Register` comme un sujet a part.
- Le site depend d'un empilement ancien RocketTheme / Gantry / Rok* qui ne doit pas etre reconduit tel quel.
- Plusieurs fonctions visibles ont deja necessite des correctifs legacy et certaines restent fragiles : cela ouvre la voie a une refonte pragmatique plutot qu'a une migration a l'identique.

## Decision de refonte a instruire

La question structurante n'est pas "comment refaire le theme", mais :

- que garde-t-on du parcours de reservation ;
- que migre-t-on de l'historique client / commande ;
- que requalifie-t-on en simple site vitrine moderne ;
- quels contenus et medias justifient une reprise selective.
