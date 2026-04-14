# SEO, URLs et redirections

## URLs publiques utiles a conserver ou rediriger

Pages prioritaires :

- `/`
- `/nos-offres.html`
- `/location-ulm.html`
- `/nos-ulm.html`
- `/galerie-photo.html`
- `/nous-trouver.html`
- `/nous-contacter.html`
- `/faq.html`
- `/mentions-legales.html`
- `/plan-de-site.html`
- `/partenaires.html`

Sous-pages galerie visibles dans le sitemap :

- `/galerie-photo/lavion.html`
- `/galerie-photo/le-pilote.html`
- `/galerie-photo/en-direct-du-cockpit.html`
- `/galerie-photo/latterrissage.html`

URL technique exposee :

- `/register.html`

## Qualite SEO actuelle

Constats :

- certaines pages ont un titre et une description specifiques ;
- beaucoup reutilisent une meta description generique ;
- la page contact a un titre faible (`contact`) ;
- la page partenaires est principalement une page de liens externes d'un SEO ancien ;
- la page `register` est visible dans le sitemap public alors qu'elle ne devrait probablement pas l'etre.

## Table `jh3_redirect_links`

La table contient `10389` lignes, mais l'echantillon le plus frequemment appele est compose surtout de :

- scans automatiques ;
- tentatives sur WordPress, Drupal, Magento, etc. ;
- fichiers techniques inexistants ;
- probes de securite.

Conclusion :

- cette table ne peut pas etre reprise telle quelle comme source de redirections SEO ;
- il faut en extraire uniquement les vraies URLs legacy du site ;
- le reste releve du bruit d'exploitation.

## Sitemap HTML actuel

Le sitemap `OSMap` publie :

- le menu principal ;
- le menu secondaire ;
- les sous-pages de galerie ;
- la page `register`.

Cela donne une bonne base pour la liste des URLs publiques a traiter dans la refonte.

## Recommandations

1. Constituer une liste blanche des URLs legacy utiles.
2. Ignorer la majorite de `jh3_redirect_links` sauf preuves contraires.
3. Prevoir une redirection ou suppression explicite de `/register.html`.
4. Reecrire les metas des pages clefs dans la cible.
5. Decider si la page `Partenaires` doit etre :
   - supprimee ;
   - noindex ;
   - ou transformee en vraie page de partenariats.
