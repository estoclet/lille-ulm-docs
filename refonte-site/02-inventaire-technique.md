# Inventaire technique

## Socle

- CMS : Joomla 3.10.12
- Projet DDEV : `lille-ulm`
- URL locale : `http://lille-ulm.ddev.site`
- PHP : 7.4
- Base : MariaDB 11.8
- Prefixe principal : `jh3_`
- SEO Joomla : `sef=1`, `sef_rewrite=1`, `sef_suffix=1`
- Editeur par defaut : `JCE`
- Captcha : `recaptcha_invisible`
- Compression gzip : active
- Cache Joomla : desactive

## Template et front

- Template front actif historique : `rt_quantive`
- Framework : Gantry 4
- Bibliotheques RocketTheme detectees :
  - `gantry`
  - `rokcommon`
  - `rokbox`
  - `rokgallery`
  - `rokstories`
  - `roknavmenu`
  - `rokcandy`

Le front charge encore des ressources anciennes :

- Mootools
- Gantry CSS / JS
- CSS compiles RocketTheme
- JCE content CSS
- RokBox
- RokStories

## Extensions principales installees

### Coeur metier / front public

- `com_content`
- `com_contact`
- `com_breezingforms`
- `com_dtregister`
- `com_phocagallery`
- `com_jevents`
- `com_osmap`
- `com_search`
- `com_finder`

### Maintenance / administration / tiers

- `com_akeeba`
- `com_extplorer`
- `com_watchfulli`
- `com_jce`
- `com_xmap`
- `com_weblinks`
- extensions RocketTheme / Gantry multiples

## Modules front observes

Modules publies cote site :

- `mod_menu` : menu principal, menu secondaire
- `mod_custom` : slogan, bloc tarifs, bloc paiement
- `mod_wrapper` : carte Google Maps, video Facebook
- `mod_rokstories` : slider / mise en avant accueil

Positions front utilisees :

- `header-b`
- `position-6`
- `showcase-a`
- `mainbottom-a`
- `mainbottom-b`
- `mainbottom-c`
- `copyright`

## Pages et dependances techniques associees

- Accueil : `com_content` + `mod_rokstories` + modules custom
- Nos tarifs : article `com_content` avec CTA vers `DT Register`
- Galerie photo : `com_phocagallery`
- Nous contacter : `com_breezingforms`
- Nous trouver : article `com_content` + `mod_wrapper` Google Maps
- Plan de site : `com_osmap`

## Base de donnees : signaux techniques importants

- Tables principales prefixees en `jh3_`
- Presence de tables residuelles prefixees en `jos_`
- Fort volume de tables `DT Register`
- Presence de tables `PhocaGallery`, `JEvents`, `OSMap`, `RokGallery`
- Historique important dans `jh3_dtregister_user`

## Risques techniques structurants

- Socle Joomla 3 obsolete
- Template Gantry 4 non reconductible
- Dependances RocketTheme nombreuses
- Formulaire BreezingForms ancien
- Composant `DT Register` non viable pour une cible moderne sans arbitrage fonctionnel
- Heritage de plusieurs couches d'extensions et de migrations successives
