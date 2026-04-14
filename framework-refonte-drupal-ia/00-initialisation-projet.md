# Initialisation du projet

## But

Ce document pose le minimum utile pour lancer la refonte sans relire tout `refonte-site/`.

Il fixe :

- les faits de depart ;
- les priorites evidentes ;
- les arbitrages a ouvrir en premier.

## Sources d'entree

Sources detaillees a considerer comme base d'observation :

- `../refonte-site/01-synthese.md`
- `../refonte-site/02-inventaire-technique.md`
- `../refonte-site/03-inventaire-fonctionnel.md`
- `../refonte-site/05-dette-technique-et-risques.md`
- `../refonte-site/13-matrice-refonte-pages.md`

## Faits de depart

- le site source est un Joomla 3 ancien ;
- le front depend de Gantry 4 et de nombreuses briques RocketTheme ;
- le volume editorial est faible et peut etre reinstruit proprement ;
- la valeur metier est surtout dans les offres, le contact, la reassurance et l'historique de reservation ;
- le moteur transactionnel legacy ne doit pas etre reconduit tel quel.

## Signaux utiles a conserver

- promesse commerciale autour des baptemes et cours ULM ;
- ancrage local a Bondues / Lille ;
- telephone et contact humain visibles ;
- rassurance autour du paiement et de la securite ;
- galerie photo comme preuve d'activite ;
- page offres comme pivot commercial principal.

## Volumes a avoir en tete

- 16 articles ;
- 39 modules ;
- 125 entrees de menu ;
- 4004 inscriptions historiques `DT Register` ;
- 250 evenements `JEvents` ;
- 4 categories `PhocaGallery`.

## Pages prioritaires au demarrage

Priorite immediate de conception :

1. Accueil
2. Nos offres
3. Nous contacter
4. Nous trouver

Priorite secondaire rapide :

1. Nos ULM
2. Galerie photo
3. FAQ
4. Mentions legales

## Arbitrages a ouvrir tout de suite

1. vente en ligne maintenue ou non ;
2. Drupal Commerce necessaire ou non ;
3. reprise, archivage ou abandon de l'historique `DT Register` ;
4. role futur de `JEvents` : public, interne ou supprime ;
5. niveau de reprise des medias et des URLs SEO.

## Regle de depart

Ne pas chercher a reproduire Joomla.

Le projet doit repartir de besoins cibles :

- conversion ;
- gestion simple ;
- reprise selective ;
- conformite ;
- maintenabilite.

## Sorties attendues du cadrage initial

Le demarrage du projet doit produire rapidement :

- un ADR sur Commerce ou non ;
- un feature brief sur le parcours d'offre et de vente ;
- une page spec pour `Nos offres` ;
- une page spec pour `Contact` ;
- une decision sur l'archivage des donnees legacy.
