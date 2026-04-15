# Agent task pack - Migration contenus editoriaux Joomla vers Drupal

## Statut
ready

## Agent cible

codex

## Type de travail

migration

## Issue GitHub liee

#38

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-013-reprise-selective-des-donnees-joomla.md
- refonte-site/12-contenus-a-reprendre-ou-non.md
- refonte-site/07-pages-publiques-et-cta.md
- refonte-site/04-inventaire-contenus.md
- refonte-site/14-arborescence-cible.md

## Pre-requis

Aucun pre-requis bloquant. Le type `node.type.page` existe deja dans la config exportee.

## Objectif

Creer les nodes Drupal de type `page` correspondant aux pages editoriales a reprendre depuis Joomla, avec leur contenu skeleton issu de l'audit, leur URL alias cible, et leur statut `draft` (non publies).

## Livrable attendu

Nodes `page` crees en `draft` pour chaque page ci-dessous, avec :
- titre propre ;
- corps HTML minimal avec les informations cles issues de l'audit ;
- URL alias selon l'arborescence cible ;
- metatitle et metadescription si le module `metatag` est disponible.

Pages a creer :

| Titre cible          | URL alias cible         | Source audit                          |
|----------------------|-------------------------|---------------------------------------|
| Nos offres           | /offres                 | 04-inventaire-contenus.md section "Nos offres" |
| Initiation au pilotage | /offres/initiation    | 04-inventaire-contenus.md section "Location ULM" |
| Nos ULM              | /nos-ulm                | 04-inventaire-contenus.md section "Nos ULM" |
| Nous trouver         | /nous-trouver           | 04-inventaire-contenus.md section "Nous trouver" |
| Nous contacter       | /nous-contacter         | 07-pages-publiques-et-cta.md section "Nous contacter" |
| FAQ                  | /faq                    | 04-inventaire-contenus.md section "FAQ" |
| Mentions legales     | /mentions-legales       | contenu standard |
| Galerie              | /galerie                | page structure uniquement, sans media |

Pages a ne pas creer :
- register
- Partenaires
- articles techniques Joomla

## Fichiers a lire

- refonte-site/04-inventaire-contenus.md
- refonte-site/07-pages-publiques-et-cta.md
- refonte-site/12-contenus-a-reprendre-ou-non.md
- refonte-site/14-arborescence-cible.md
- framework-refonte-drupal-ia/decisions/ADR-013-reprise-selective-des-donnees-joomla.md

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/
- refonte-site/

## Contraintes

Cote app (dans le depot lille-ulm-drupal-app), lire avant de coder :
`config/sync/node.type.page.yml` (champs disponibles), `config/sync/` pour verifier si `metatag` est configure.

- Creer les nodes via un module `lille_ulm_seed_content` avec `hook_install`, ou via des commandes drush documentees. Privilegier le module si le volume le justifie.
- Tous les nodes doivent etre en statut `draft` (non publies) — le gestionnaire les finalisera.
- Le corps HTML doit contenir les informations cles issues de l'audit, pas un lorem ipsum.
- Les URL alias doivent suivre l'arborescence cible de `refonte-site/14-arborescence-cible.md`.
- Ne pas creer de nouveau type de contenu — utiliser `page` existant.
- Si `metatag` n'est pas disponible, ne pas l'activer — noter comme `decision a prendre`.
- Ne pas migrer les contenus "Remerciement", "register", "Partenaires".

## En cas de blocage ou d'ambiguite

Si une information manque ou est contradictoire :

1. ne pas trancher a la place de l'humain ;
2. marquer le point comme `decision a prendre` dans la sortie ;
3. continuer sur les points non bloques ;
4. lister les blocages en fin de sortie dans "questions ouvertes".

Ne pas creer de nouveau fichier source de verite pour combler un vide.

## Verification attendue

- `drush en lille_ulm_seed_content` (ou equivalent) s'execute sans erreur.
- Les 8 nodes existent en base, statut `draft`, avec URL alias correct.
- Aucun node publie involontairement.
- `drush config:export` ne produit pas d'erreur de schema.

## Definition de fin

- 8 nodes crees en draft dans DDEV.
- URL alias conformes a l'arborescence cible.
- Commentaire de cloture poste sur l'issue #38.
- Statut de ce pack passe a `done`.

## Sortie courte a produire

Un commentaire d'issue listant :
1. faits confirmes (nodes crees, URLs) ;
2. decisions a prendre (contenus a completer, metatag, page Location ULM a confirmer) ;
3. questions ouvertes eventuelles.
