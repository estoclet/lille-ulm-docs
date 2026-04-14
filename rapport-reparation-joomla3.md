# Rapport de réparation Joomla 3

**Site :** `~/Projets/lille-ulm/www`
**Date :** 14 avril 2026
**Objectif :** remettre le site Joomla 3 en état de fonctionnement avant retransfert FTP

## Point technique important

Le site actif utilise le préfixe de tables `jh3_`.

Les tables `jos_` coexistent encore dans la base, mais ne pilotent pas le front réellement servi par DDEV. Toute correction SQL doit donc viser `jh3_` en priorité.

## Symptôme initial

Le front principal chargeait, mais plusieurs fonctionnalités critiques tombaient en erreur :

- pages `DT Register` en erreur `Class 'JFormFieldText' not found`
- plus largement, les classes legacy Joomla `JFormFieldText` et `JFormFieldList` n'étaient plus résolues

## Cause identifiée

Le problème ne venait pas d'un fichier manquant dans `DT Register`, mais d'une compatibilité legacy cassée au niveau du core Joomla :

- `JFormHelper::loadFieldClass('text')` renvoyait `false`
- `JFormHelper::loadFieldClass('list')` renvoyait `false`
- les classes `JFormFieldText` et `JFormFieldList` n'étaient pas chargées

Concrètement, le `FormHelper` chargeait d'abord les classes namespacées modernes (`Joomla\\CMS\\Form\\Field\\TextField`) sans recréer les alias legacy attendus par les extensions anciennes.

Cela cassait notamment :

- `DT Register`
- potentiellement toute extension Joomla 3 encore basée sur `JFormField*`

## Correctif appliqué

Fichier modifié :

- [libraries/src/Form/FormHelper.php](/home/eric/Projets/lille-ulm/www/libraries/src/Form/FormHelper.php)

Correction :

- ajout d'un pont de compatibilité dans `loadClass()`
- quand une classe namespacée est trouvée, création de l'alias legacy correspondant via `class_alias()`
- retour de la classe legacy si elle existe

## Vérifications effectuées

### Vérification des classes

Après patch :

- `JFormHelper::loadFieldClass("text")` => `JFormFieldText`
- `JFormHelper::loadFieldClass("list")` => `JFormFieldList`
- `class_exists("JFormFieldText")` => `1`
- `class_exists("JFormFieldList")` => `1`

### Vérification syntaxique

- `php -l libraries/src/Form/FormHelper.php` : OK

### Vérification fonctionnelle publique

Routes testées avec succès HTTP 200 :

- `/`
- `/register.html`
- `/bapteme-de-l-air-seance-de-15-min.html?...eventId=10`
- `/galerie-photo.html`
- `/galerie-photo/lavion.html`
- `/nous-contacter.html`
- `/plan-de-site.html`
- `/agenda`

### Constats fonctionnels après correction

- `DT Register` rend de nouveau ses pages et formulaires
- `PhocaGallery` rend de nouveau les catégories et les images
- le sitemap HTML fonctionne
- le formulaire de contact charge correctement
- l'URL `/agenda` répond désormais en `200 OK` et affiche le calendrier JEvents public

## Point particulier : agenda / événement

Initialement, les routes agenda testées n'étaient pas cassées techniquement, mais renvoyaient vers un écran de connexion quand elles étaient appelées via l'item de menu public.

Cause :

- dans la table active `jh3_menu`, l'item `Agenda` (`id = 22`) avait `access = 2`
- l'URL `/agenda` redirigeait alors vers `/component/users/?view=login&Itemid=27`

Correctif :

- l'item `jh3_menu.id = 22` a été réaligné sur le niveau public du site (`access = 1`)
- la route `/agenda` sert maintenant bien JEvents côté front

Conclusion :

- l'agenda public est de nouveau opérationnel ;
- l'item `Evenement` (`id = 175`) reste en accès restreint et peut être laissé tel quel tant qu'il n'est pas exposé au parcours public.

## Correctif complémentaire : notices d'administration

Des notices PHP parasites apparaissaient dans le back-office :

- `Undefined variable: dataAttribute` dans les layouts Joomla de champs de liste

Fichiers modifiés :

- [layouts/joomla/form/field/list.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/list.php)
- [layouts/joomla/form/field/groupedlist.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/groupedlist.php)
- [layouts/joomla/form/field/list-fancy-select.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/list-fancy-select.php)

Correction :

- ajout d'une initialisation défensive de `$dataAttribute` via `?? ''`

Résultat validé par screenshots :

- écran `Articles` propre
- écran `Menus` propre
- écran `Modules` propre

## Correctif complémentaire : réouverture du tunnel DT Register

Le composant `DT Register` ne plantait plus, mais restait inutilisable publiquement car les offres publiées étaient considérées comme expirées.

Cause identifiée :

- les vraies offres publiques sont stockées dans `jh3_dtregister_group_event`
- les offres publiées `10`, `11`, `12`, `15`, `17`, `18` portaient encore des dates métier historiques
- plusieurs `dtend` étaient en 2025, donc dépassés au 14 avril 2026
- la logique interne de `DT Register` calcule aussi un état `future_event` à partir de `startdate + starttime`
- certaines valeurs `starttime` étaient incohérentes avec `dtstarttime`, ce qui injectait le message public `DT_START_TIME_GREATER_THEN_CURRENT_DATE`

Correctifs appliqués en base active `jh3_` :

- extension des dates de fin en 2030 :
  - `10` -> `2030-04-30`
  - `11` -> `2030-11-20`
  - `12` -> `2030-11-20`
  - `15` -> `2030-04-09`
  - `17` -> `2030-04-09`
  - `18` -> `2030-04-10`
- alignement des `cut_off_date` sur ces nouvelles échéances
- remise des `startdate` au `2026-04-14` avec `starttime = 00:00:00` pour sortir l'état `future_event`
- conservation d'un `dtstart` technique distinct pour laisser les offres publiquement reservables
- réalignement ciblé des horaires pour supprimer l'avertissement public parasite

Résultat validé :

- `register.html` liste de nouveau les offres
- les pages d'offres `15 min`, `30 min`, `45 min` ne retombent plus sur une liste vide
- le message `DT_START_TIME_GREATER_THEN_CURRENT_DATE` n'apparaît plus dans le tunnel public
- le formulaire one-page progresse jusqu'au panier

## Audit complémentaire du tunnel DT Register

L'audit Playwright ciblé du tunnel a confirmé le comportement suivant :

- la page one-page `register.register&eventId=10` charge correctement ;
- le formulaire visible à piloter est `individual_*`, pas `billing_*` ;
- le bouton `Suivant` crée bien une ligne de panier et mène à l'étape `Mon Panier` avec total `49.90 EUR` ;
- l'étape paiement expose au moins le moyen `Joomlart_Paylater` avec l'option `Chèque ou virement`.

Correctif appliqué ensuite :

- ajout d'une garde défensive dans [plugins/system/ja_payment/tmpl/form.php](/home/eric/Projets/lille-ulm/www/plugins/system/ja_payment/tmpl/form.php) pour ne parcourir les `issuer` `Mollie` que si la configuration est présente et de type tableau.

Résultat :

- les notices PHP `Mollie` n'apparaissent plus dans le HTML rendu de l'étape paiement ;
- le sélecteur `Mollie` est désormais rendu vide proprement quand aucune configuration exploitable n'est chargée ;
- la syntaxe PHP du template corrigé est valide via `ddev exec php -l`.

Conclusion intermédiaire :

- le tunnel est redevenu parcourable côté front jusqu'au panier ;
- l'étape paiement n'injecte plus de notices visibles, mais le passage complet jusqu'à une soumission finale reste encore à valider si vous voulez homologuer le tunnel en bout en bout.

## Correctif complémentaire : redirection finale DT Register en DDEV

Le parcours `Paylater` allait désormais jusqu'a la confirmation, mais retombait ensuite sur une URL absolue de production :

- `http://www.bapteme-air-lille.fr/remerciement.html`

Cause identifiée :

- les offres publiques actives `jh3_dtregister_group_event.slabId IN (10, 11, 12, 15, 17, 18)` portaient encore `pay_later_redirect_url` et `thanks_redirect_url` vers l'ancien domaine absolu ;
- en DDEV, cette redirection externe empêchait de valider localement la page de fin de parcours.

Correctif appliqué :

- réalignement des URLs de retour sur le chemin local existant `/remerciement.html` dans la table active `jh3_dtregister_group_event` pour les offres publiques concernées.

Résultat validé :

- le formulaire one-page se remplit avec les champs visibles `individual[FIELD][...]` ;
- l'étape `Paylater` accepte l'option `Chèque ou virement` ;
- la soumission finale aboutit désormais sur `http://lille-ulm.ddev.site/remerciement.html`.

## Correctif complémentaire : vidéo d'accueil

Le bloc `Vidéo` de l'accueil pointait vers un embed YouTube obsolète :

- URL morte : `https://www.youtube.com/embed/ivqPSB-kJdk`
- symptôme visible : encart `Video non disponible` sur la page d'accueil

Correctif appliqué :

- adaptation ciblée de [modules/mod_wrapper/tmpl/default.php](/home/eric/Projets/lille-ulm/www/modules/mod_wrapper/tmpl/default.php)
- quand le module wrapper rencontre cet ancien embed YouTube précis, il rend désormais l'embed Facebook fourni :
  - `https://www.facebook.com/LilleULM/videos/2247570525258144/`
  - via `https://www.facebook.com/plugins/video.php?...`

Résultat :

- le bloc `Vidéo` de l'accueil ne retombe plus sur un média mort ;
- l'accueil sert maintenant directement la vidéo Facebook `LilleULM` dans le module existant, sans modifier la configuration du module en base.

## Correctif complémentaire : reCAPTCHA contact en DDEV

L'anomalie rouge/blanche visible sur la page `Nous contacter` ne venait pas du plugin captcha Joomla actif, mais des clés reCAPTCHA propres au formulaire `BreezingForms`.

Cause identifiée :

- le formulaire `contact` (`jh3_facileforms_forms.id = 1`) embarque sa propre paire `pubkey` / `privkey` dans `template_areas` ;
- en environnement `*.ddev.site`, cette clé n'est pas autorisée côté Google et provoque l'erreur visuelle `Invalid domain for site key`.

Correctif appliqué :

- ajout d'un override strictement local au runtime DDEV dans :
  - [administrator/components/com_breezingforms/libraries/crosstec/classes/BFQuickMode.php](/home/eric/Projets/lille-ulm/www/administrator/components/com_breezingforms/libraries/crosstec/classes/BFQuickMode.php)
  - [components/com_breezingforms/facileforms.process.php](/home/eric/Projets/lille-ulm/www/components/com_breezingforms/facileforms.process.php)
- sur `localhost`, `127.0.0.1` et `*.ddev.site`, BreezingForms bascule vers les clés de test publiques Google pour l'affichage et la vérification serveur ;
- hors environnement local, les clés métier existantes restent inchangées.

Résultat :

- la page `Nous contacter` ne charge plus la clé invalide en DDEV ;
- l'anomalie visuelle parasite liée à reCAPTCHA n'est plus reproduite sur l'instance locale ;
- le comportement de production reste préservé.

## Nettoyage des données de test

L'audit du tunnel a créé des lignes temporaires dans la table `jh3_dtregister_billing` avec l'email de test `audit.dtregister@example.test`.

Contrôle avant purge :

- `jh3_dtregister_user` : `0` ligne
- `jh3_dtregister_user_field_values` : `0` ligne
- `jh3_dtregister_member_field_values` : `0` ligne
- `jh3_dtregister_billing` : `2` lignes temporaires

Nettoyage effectué :

- suppression des lignes `jh3_dtregister_billing` portant l'email `audit.dtregister@example.test`
- contrôle après purge : `0` ligne restante
- après le retest post-correctif `Mollie`, les 2 nouvelles lignes temporaires recréées dans `jh3_dtregister_billing` ont aussi été supprimées ; contrôle final : `0` ligne restante
- après la validation finale du parcours `Paylater`, les nouvelles lignes de test recréées dans `jh3_dtregister_billing` ont aussi été supprimées ; contrôles finaux :
  - `jh3_dtregister_billing` : `0`
  - `jh3_dtregister_user` : `0`
  - `jh3_dtregister_user_field_values` : `0`
  - `jh3_dtregister_member_field_values` : `0`

## Stabilisation complémentaire en cours : écrans d'édition admin utiles au métier

Une nouvelle passe de stabilisation a été engagée pour rouvrir les écrans d'édition les plus utiles au gestionnaire :

- édition d'article Joomla ;
- édition de module Joomla ;
- édition de lien de menu Joomla ;
- édition d'offre `DT Register`.

### Symptômes de départ

Les écrans ci-dessus tombaient sur plusieurs fatals de compatibilité legacy, notamment :

- `Call to undefined method Joomla\CMS\Form\Field\ComponentlayoutField::getDatabase()`
- `Call to undefined method Joomla\CMS\Form\Field\CalendarField::getDatabase()`
- `Call to undefined method Joomla\CMS\Application\AdministratorApplication::getInput()`

### Correctifs déjà appliqués

Des ponts de compatibilité ont été ajoutés dans le core local pour rétablir des accesseurs encore attendus par une partie du code legacy :

- [libraries/src/Form/FormField.php](/home/eric/Projets/lille-ulm/www/libraries/src/Form/FormField.php)
  - ajout d'un accesseur `getDatabase()` renvoyant `JFactory::getDbo()`
- [libraries/src/Application/CMSApplication.php](/home/eric/Projets/lille-ulm/www/libraries/src/Application/CMSApplication.php)
  - ajout d'un accesseur `getInput()` renvoyant `$this->input`

Des champs Joomla trop récents pour ce socle ont ensuite été réalignés sur une écriture SQL compatible avec la couche base de données legacy :

- [libraries/src/Form/Field/ComponentlayoutField.php](/home/eric/Projets/lille-ulm/www/libraries/src/Form/Field/ComponentlayoutField.php)
- [libraries/src/Form/Field/ModulelayoutField.php](/home/eric/Projets/lille-ulm/www/libraries/src/Form/Field/ModulelayoutField.php)
- [libraries/src/Form/Field/RulesField.php](/home/eric/Projets/lille-ulm/www/libraries/src/Form/Field/RulesField.php)

Correction :

- suppression des dépendances directes à `Joomla\Database\ParameterType` dans ces champs ;
- remplacement des `bind()` problématiques par des clauses construites avec valeurs nettoyées / castées.

L'autoload Composer local a aussi été complété pour réexposer le namespace moderne base de données attendu par une partie du core hybride :

- [libraries/vendor/composer/autoload_real.php](/home/eric/Projets/lille-ulm/www/libraries/vendor/composer/autoload_real.php)
  - ajout du mapping PSR-4 `Joomla\\Database\\ -> libraries/vendor/joomla/database/src`

Enfin, plusieurs layouts de champs ont été durcis pour éviter les notices qui polluaient ou interrompaient le rendu admin :

- [layouts/joomla/form/field/radio/buttons.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/radio/buttons.php)
- [layouts/joomla/form/field/time.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/time.php)
- [layouts/joomla/form/field/calendar.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/calendar.php)

### État fonctionnel observé à ce stade

- l'édition d'un lien de menu s'ouvre de nouveau ;
- l'édition d'une offre `DT Register` s'ouvre de nouveau ;
- les écrans d'édition article et module ne tombent plus sur les premiers fatals `getDatabase()` / `getInput()` ;
- ils restent cependant bloqués plus loin sur le layout moderne des permissions, désormais identifié précisément :
  - `Call to undefined method Joomla\CMS\Document\HtmlDocument::getWebAssetManager()`
  - fichier concerné : [layouts/joomla/form/field/rules.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/rules.php)

### Note de méthode

Le debug Joomla a été activé temporairement en local dans [configuration.php](/home/eric/Projets/lille-ulm/www/configuration.php) pour faire remonter les exceptions silencieuses `Erreur: 0` et isoler la vraie cause restante sur les écrans article/module.

Une fois le diagnostic obtenu, la configuration a été remise à son état normal :

- `debug = 0`
- `error_reporting = default`

## Ce qui n'a pas été nécessaire

À ce stade, aucune réinstallation externe d'extension n'a été nécessaire pour remettre les fonctionnalités publiques principales en service.

Le problème principal venait du chargement des classes legacy, pas d'une absence manifeste de fichiers dans :

- `com_dtregister`
- `com_phocagallery`
- `com_jevents`
- `com_breezingforms`

## Recommandation avant FTP

Avant retransfert :

1. retester en navigateur réel :
   - accueil
   - page offres
   - une page `DT Register`
   - galerie
   - contact
   - agenda
2. traiter les blocs encore dégradés :
   - validation métier du tunnel `DT Register` maintenant rouvert techniquement mais encore basé sur des dates artificiellement prolongées

Note sur la page contact :

- le formulaire charge du reCAPTCHA via BreezingForms ;
- l'anomalie visuelle DDEV venait bien d'un refus de domaine Google reCAPTCHA sur `lille-ulm.ddev.site` ;
- un override local DDEV vers les clés de test Google est maintenant en place, sans impact sur le domaine public.
3. transférer au minimum :
    - [libraries/src/Form/FormHelper.php](/home/eric/Projets/lille-ulm/www/libraries/src/Form/FormHelper.php)
    - [layouts/joomla/form/field/list.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/list.php)
    - [layouts/joomla/form/field/groupedlist.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/groupedlist.php)
    - [layouts/joomla/form/field/list-fancy-select.php](/home/eric/Projets/lille-ulm/www/layouts/joomla/form/field/list-fancy-select.php)
    - [plugins/system/ja_payment/tmpl/form.php](/home/eric/Projets/lille-ulm/www/plugins/system/ja_payment/tmpl/form.php)
    - [modules/mod_wrapper/tmpl/default.php](/home/eric/Projets/lille-ulm/www/modules/mod_wrapper/tmpl/default.php)
    - [administrator/components/com_breezingforms/libraries/crosstec/classes/BFQuickMode.php](/home/eric/Projets/lille-ulm/www/administrator/components/com_breezingforms/libraries/crosstec/classes/BFQuickMode.php)
    - [components/com_breezingforms/facileforms.process.php](/home/eric/Projets/lille-ulm/www/components/com_breezingforms/facileforms.process.php)

Si tu veux, la prochaine étape peut être :

- préparer une checklist de retransfert FTP propre ;
- ou produire un diff minimal des fichiers à remettre en ligne.

## Tentative contrôlée de mises à jour métier dans DDEV

Une tentative limitée aux extensions les plus utiles au gestionnaire a été réalisée dans l'instance DDEV, sans toucher à la mise à jour coeur Joomla proposée vers `4.4.14`.

Cette mise à jour coeur n'a pas été tentée car il s'agit d'une migration majeure depuis `Joomla 3.10.12`, très risquée sur ce socle hybride et susceptible d'écraser les correctifs de compatibilité locale déjà appliqués.

### Extensions métier testées

- `JEvents`
  - version installée avant test : `3.6.80`
  - résultat : mise à jour réussie via l'installateur Joomla
  - version observée après test : `3.6.82.1` sur le composant et ses plugins / bibliothèques associés ; le package remonte `3.6.82.2`
- `DT Register`
  - version installée avant test : `4.2.6`
  - résultat : échec dans l'installateur Joomla
  - message observé : `Échec de l'extraction du fichier : download.php_element_com_dtregister_version_4.2.9_type_component_coreVersion_j30`
  - état après test : reste en `4.2.6`
- `JCE Pro`
  - version installée avant test : `2.9.20`
  - résultat : mise à jour non applicable en l'état
  - messages observés :
    - téléchargement manuel demandé ;
    - clé d'abonnement requise (`Subscription Key`)
  - état après test : reste en `2.9.20`

### Effets fonctionnels observés après test

- `JEvents` ouvre désormais un `JEvents Dashboard` plus moderne, avec compteurs et alertes de configuration ;
- le dashboard `JEvents` signale que les calendriers ne sont pas correctement configurés et propose aussi une mise à jour des collations SQL propres à ses tables ;
- l'édition d'une offre `DT Register` reste accessible ;
- l'édition d'article et de module reste bloquée sur la même erreur core Joomla :
  - `Call to undefined method Joomla\CMS\Document\HtmlDocument::getWebAssetManager()`

### Conclusion pratique

Les mises à jour métier disponibles ne débloquent pas, à ce stade, les écrans Joomla article/module encore indisponibles au gestionnaire.

Le seul changement utile constaté est la modernisation du back-office `JEvents`, qui améliore la lisibilité de l'écran agenda mais ne corrige pas le verrou principal des éditions profondes Joomla.

### Analyse ciblée de l'échec de mise à jour `DT Register`

L'échec de mise à jour `DT Register` n'est pas lié, à ce stade, à un problème de permissions locales sur le dossier temporaire Joomla ni à un défaut générique d'extraction ZIP :

- le dossier `tmp/` est bien accessible en lecture / écriture ;
- l'espace disque est suffisant ;
- l'installateur Joomla a bien réussi, dans la même session, à extraire et appliquer la mise à jour `JEvents`.

L'URL de mise à jour déclarée par Joomla pour `DT Register` renvoie bien un XML valide :

- `http://update.joomlart.com/service/tracking/j30/com_dtregister.xml`

mais l'URL de téléchargement réelle :

- `http://update.joomlart.com/service/download.php?element=com_dtregister&version=4.2.9&type=component&coreVersion=j30`

ne renvoie pas une archive ZIP ; elle renvoie un document `application/json` contenant l'erreur suivante :

```json
{"from":"JoomlArt Updater Service","to":"","content":{"error":"Response from JoomlArt Updater Service: Your account does not have enough permission to take this action! ...","response":null}}
```

Joomla enregistre alors cette réponse JSON telle quelle dans `tmp/download.php_element_com_dtregister_version_4.2.9_type_component_coreVersion_j30`, puis tente de l'extraire comme une archive, ce qui explique le message visible dans l'interface :

- `Échec de l'extraction du fichier : download.php_element_com_dtregister_version_4.2.9_type_component_coreVersion_j30`

### Conclusion sur la faisabilité

Dans l'état actuel, cette mise à jour ne peut pas passer via l'installateur natif Joomla :

- aucune preuve de compte `JoomlArt` autorisé n'a été trouvée dans la configuration locale ;
- le composant `JA Extension Manager` recommandé par JoomlArt pour gérer les identifiants et téléchargements n'est pas installé ici ;
- le serveur amont refuse explicitement l'action pour défaut de permission.

En revanche, elle pourrait probablement passer si l'on dispose :

1. d'un compte `JoomlArt` encore autorisé à télécharger cette version de `DT Register` ;
2. soit d'un téléchargement manuel du package `4.2.9` depuis l'espace client puis d'une installation locale ;
3. soit d'une configuration correcte de `JA Extension Manager` avec des identifiants valides, si ce canal est encore compatible avec ce produit.

Sans cet accès fournisseur, relancer la mise à jour dans Joomla reproduira simplement le même échec.
