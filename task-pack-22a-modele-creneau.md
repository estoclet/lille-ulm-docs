# Agent task pack - Modele de donnees reservation de creneau

## Statut
done

## Agent cible

codex

## Type de travail

implementation

## Issue GitHub liee

#22

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-015-reservation-de-creneaux.md
- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/decisions/ADR-010-modele-commerce-minimal.md

## Repo cible

Repo applicatif attendu : `../lille-ulm-drupal-app/` depuis ce repo docs
(voir `README.md` et `framework-refonte-drupal-ia/00-initialisation-projet.md`).
Codex doit etre lance depuis la racine de ce depot.
Les fichiers ADR (sources de verite) se trouvent dans ce repo documentaire.

## Contexte de l'existant (fait observe - a lire avant toute implementation)

Le module custom `web/modules/custom/lille_ulm_commerce/` existe deja et contient :
- logique cadeau (field_is_gift, field_recipient_name, field_recipient_email, field_gift_message) ;
- generation de token de justificatif (field_purchase_token, index unique en base) ;
- references a `commerce_bat` pour la reservabilite : `lille_ulm_commerce_order_item_is_bookable()`
  utilise `commerce_bat.availability_manager` et des champs `field_cbat_rental_date` et
  `field_cbat_num_days` sur la ligne de commande.

Le module contrib `commerce_bat` est installe dans `web/modules/contrib/commerce_bat/`
(compatible Drupal ^10 || ^11, dependances : `bat`, `commerce`, `commerce_cart`, `commerce_order`).

## Objectif

Implémenter la structure de données minimale permettant :

1. de marquer une offre comme réservable ;
2. de gérer des créneaux date/heure côté serveur ;
3. de rattacher un créneau choisi à la ligne de commande ;
4. de protéger temporairement un créneau pendant le checkout et de le confirmer à la commande placée ;
5. de libérer automatiquement un créneau si la commande est abandonnée.

La question de fond à trancher d'abord (voir "En cas de blocage") : s'appuyer sur `commerce_bat`
déjà en place, ou implémenter un module slot custom minimal en remplacement ?

## Livrable attendu

- champ booleen `field_is_bookable` (ou equivalent) sur le type de produit Commerce cible,
  coherent avec l'existant ou en remplacement propre de la logique `commerce_bat` ;
- entite ou objet `slot` (creneau) : date/heure, capacite initiale 1, statut ouvert/ferme/reserve ;
- champ de reference creneau sur la ligne de commande (`commerce_order_item`) ;
- logique de verrou temporaire a la selection du creneau : expiration configurable (defaut : 30 min) ;
- event subscriber qui confirme la reservation quand la commande passe en statut `placed` ;
- event subscriber qui libere le creneau si la commande est annulee ou abandonnee ;
- configuration exportable (config YAML) pour tout ce qui peut l'etre.

## Fichiers a lire

- ../lille-ulm-drupal-app/web/modules/custom/lille_ulm_commerce/lille_ulm_commerce.module
- ../lille-ulm-drupal-app/web/modules/custom/lille_ulm_commerce/lille_ulm_commerce.install
- ../lille-ulm-drupal-app/web/modules/custom/lille_ulm_commerce/lille_ulm_commerce.info.yml
- ../lille-ulm-drupal-app/web/modules/contrib/commerce_bat/commerce_bat.info.yml
- framework-refonte-drupal-ia/decisions/ADR-015-reservation-de-creneaux.md
- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/decisions/ADR-010-modele-commerce-minimal.md
- framework-refonte-drupal-ia/04-architecture-drupal-cible.md

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/
- docs/

## Contraintes

- Drupal 11 + DDEV ;
- un creneau ne peut pas etre reserve deux fois simultanement (prevention double booking obligatoire) ;
- la source de verite des disponibilites reste cote serveur, jamais cote client ;
- code custom uniquement si aucun contrib ne couvre exactement le besoin ; la recherche contrib
  doit etre documentee avant tout code custom ;
- capacite initiale du creneau : 1 reservation par creneau ;
- ne pas implementer d'interface gestionnaire dans ce pack (c'est le pack 22b) ;
- ne pas implementer de fonctionnalite meteo dans ce pack ;
- configuration exportable, pas de contenu seed ;
- ne pas casser la logique cadeau et justificatif deja en place dans lille_ulm_commerce.

## En cas de blocage ou d'ambiguite

Point de decision critique avant toute implementation :

`commerce_bat` est deja installe et partiellement integre dans le module custom.
Deux voies sont possibles :

A. Construire sur `commerce_bat` : evite la duplication, mais `commerce_bat` impose
   un modele BAT (availability calendar) potentiellement plus lourd que le besoin reel
   (un seul creneau = 1 reservation). Documenter les contraintes imposees par ce modele.

B. Implementer un module slot custom minimal : plus simple, mieux aligne sur ADR-016
   (creneau = ressource metier simple), mais necessite de retirer ou d'ignorer les
   references `commerce_bat` existantes dans lille_ulm_commerce.module.

Si la voie B est choisie, signaler explicitement quels champs et fonctions
de lille_ulm_commerce.module devront etre mis a jour dans un suivi (pas dans ce pack).

Si aucune voie n'est clairement superieure : marquer 'decision a prendre' et
presenter les deux options avec leurs consequences dans la sortie.

## Verification attendue

- un creneau ouvert peut etre selectionne et rattache a une ligne de commande ;
- un creneau selectionne est verrouille et n'apparait plus disponible pour un autre acheteur ;
- le verrou expire si la commande reste en panier au-dela du delai configure ;
- la reservation est confirmee quand la commande passe en `placed` ;
- la reservation est liberee si la commande est annulee ou abandonnee ;
- les structures sont exportees en config YAML ;
- la logique cadeau et justificatif existante n'est pas cassee.

## Definition de fin

La structure est installable dans DDEV, les cas de la section "Verification attendue" sont
tous reproductibles manuellement ou via test, la config est exportee et versionnee.

## Sortie courte a produire

1. faits confirmes : modules Commerce actives, briques existantes reutilisees, voie retenue (A ou B)
2. propositions : entites, champs, event subscribers implementes
3. questions ouvertes : arbitrages non resolus (notamment impact sur commerce_bat si voie B)
4. fichiers modifies : liste des fichiers crees ou modifies dans le repo applicatif
