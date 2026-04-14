# Documentation de refonte du site Lille ULM

Cette documentation vise a cadrer la refonte du site Joomla 3 source situe dans `~/Projets/lille-ulm/www`.

Elle ne remplace pas les rapports deja presents a la racine (`rapport-migration-joomla4.md`, `rapport-audit-comparatif.md`), mais les complete par un inventaire utile a la conception d'une refonte.

## Perimetre analyse

- Site source : Joomla 3.10.12
- URL locale : `http://lille-ulm.ddev.site`
- Environnement : DDEV, PHP 7.4, MariaDB 11.8
- Template front : `rt_quantive` (RocketTheme / Gantry 4)
- Positionnement metier : baptêmes de l'air ULM, initiation au pilotage, location, galerie photo, contact

## Ce dossier contient

- [01-synthese.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/01-synthese.md)
- [02-inventaire-technique.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/02-inventaire-technique.md)
- [03-inventaire-fonctionnel.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/03-inventaire-fonctionnel.md)
- [04-inventaire-contenus.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/04-inventaire-contenus.md)
- [05-dette-technique-et-risques.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/05-dette-technique-et-risques.md)
- [06-pistes-de-refonte.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/06-pistes-de-refonte.md)
- [07-pages-publiques-et-cta.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/07-pages-publiques-et-cta.md)
- [08-medias-et-assets.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/08-medias-et-assets.md)
- [09-reprise-donnees-reservation.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/09-reprise-donnees-reservation.md)
- [10-flux-et-messages-transactionnels.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/10-flux-et-messages-transactionnels.md)
- [11-seo-urls-et-redirections.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/11-seo-urls-et-redirections.md)
- [12-contenus-a-reprendre-ou-non.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/12-contenus-a-reprendre-ou-non.md)
- [13-matrice-refonte-pages.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/13-matrice-refonte-pages.md)
- [14-arborescence-cible.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/14-arborescence-cible.md)
- [15-zoning-pages-cibles.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/15-zoning-pages-cibles.md)
- [journal-iterations.md](/home/eric/Projets/lille-ulm/lille-ulm-docs/refonte-site/journal-iterations.md)

## Methode

Cette premiere iteration a ete construite a partir de :

- l'arborescence du site source ;
- la configuration Joomla ;
- des requetes SQL sur la base locale DDEV ;
- le rendu HTML de plusieurs pages front ;
- les rapports de migration et d'audit deja produits.

Les prochaines iterations doivent completer cette base avec :

- captures ecran et inventaire visuel par page ;
- extraction des textes utiles a la requalification UX et SEO ;
- inventaire des medias a conserver ;
- inventaire des integrations externes et des flux emails ;
- arbitrage fonctionnel sur reservation, agenda et galerie.
