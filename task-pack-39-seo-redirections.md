# Agent task pack - Redirections SEO depuis les URLs Joomla

## Statut
done

## Agent cible

codex

## Type de travail

migration

## Issue GitHub liee

#39

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-013-reprise-selective-des-donnees-joomla.md
- refonte-site/11-seo-urls-et-redirections.md

## Pre-requis

- task-pack-38-contenus-editoriaux.md en `done` — les URL alias cibles doivent exister avant de creer les redirections.

## Objectif

Creer dans Drupal les redirections 301 des URLs Joomla legacy vers les nouvelles URLs Drupal, et configurer le traitement explicite des URLs a ne pas rediriger.

## Livrable attendu

Redirections 301 creees (via entites `redirect` Drupal) pour la liste blanche ci-dessous.
Chaque redirection pointe vers l'URL alias Drupal cible existante.

| URL source (Joomla)                        | URL cible Drupal          |
|--------------------------------------------|---------------------------|
| /nos-offres.html                           | /offres                   |
| /location-ulm.html                         | /offres/initiation        |
| /nos-ulm.html                              | /nos-ulm                  |
| /galerie-photo.html                        | /galerie                  |
| /galerie-photo/lavion.html                 | /galerie                  |
| /galerie-photo/le-pilote.html              | /galerie                  |
| /galerie-photo/en-direct-du-cockpit.html   | /galerie                  |
| /galerie-photo/latterrissage.html          | /galerie                  |
| /nous-trouver.html                         | /nous-trouver             |
| /nous-contacter.html                       | /nous-contacter           |
| /faq.html                                  | /faq                      |
| /mentions-legales.html                     | /mentions-legales         |
| /plan-de-site.html                         | /                         |
| /partenaires.html                          | /                         |
| /register.html                             | /offres                   |

Traitement complementaire :
- `/register.html` redirige vers `/offres` (plus vers une page technique).
- Configurer `redirect.settings` pour retourner 404 sur les URLs hors liste blanche non gerees.

## Fichiers a lire

- refonte-site/11-seo-urls-et-redirections.md
- framework-refonte-drupal-ia/decisions/ADR-013-reprise-selective-des-donnees-joomla.md

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/
- refonte-site/

## Contraintes

Cote app (dans le depot lille-ulm-drupal-app), lire avant de coder :
`config/sync/redirect.settings.yml` et `config/sync/views.view.redirect.yml` (configuration existante du module redirect).

- Creer les redirections via un `hook_install` dans un module `lille_ulm_redirects`, ou via un fichier de config `config/install/` si le module redirect le supporte.
- Privilegier la config exportable (fichiers YAML) sur le code procedural pour faciliter le deploiement.
- Ne pas toucher a `jh3_redirect_links` — cette table contient 10 389 lignes dont la grande majorite est du bruit (scans, probes). Utiliser uniquement la liste blanche ci-dessus.
- Toutes les redirections sont en 301 (permanent).
- En cas de conflit (URL cible inexistante), marquer comme `decision a prendre` et continuer.

## En cas de blocage ou d'ambiguite

Si une information manque ou est contradictoire :

1. ne pas trancher a la place de l'humain ;
2. marquer le point comme `decision a prendre` dans la sortie ;
3. continuer sur les points non bloques ;
4. lister les blocages en fin de sortie dans "questions ouvertes".

Ne pas creer de nouveau fichier source de verite pour combler un vide.

## Verification attendue

- `drush en lille_ulm_redirects` (ou activation du module) s'execute sans erreur.
- Les 15 redirections existent dans la vue d'administration `/admin/config/search/redirect`.
- Une requete sur `/nos-offres.html` retourne un 301 vers `/offres`.
- `drush config:export` inclut les redirections sans erreur de schema.

## Definition de fin

- 15 redirections creees et testees en DDEV.
- Config exportee dans `config/install/` ou equivalente.
- Commentaire de cloture poste sur l'issue #39.
- Statut de ce pack passe a `done`.

## Sortie courte a produire

Un commentaire d'issue listant :
1. faits confirmes (redirections creees, test 301 valide) ;
2. decisions a prendre eventuelles (URLs cibles manquantes, sort de `/partenaires.html`) ;
3. questions ouvertes eventuelles.
