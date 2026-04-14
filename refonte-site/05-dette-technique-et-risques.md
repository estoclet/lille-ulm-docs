# Dette technique et risques

## Dette technique constatee

### 1. Socle obsolete

- Joomla 3 en fin de vie
- PHP 7.4 sur l'environnement source
- nombreuses extensions anciennes

### 2. Dependance forte a RocketTheme / Gantry

- theme `rt_quantive`
- Gantry 4
- modules / plugins `rok*`
- rendu front fortement couple a cet ecosysteme

Cette couche ne doit pas etre consideree comme un actif a conserver tel quel.

### 3. Reservation historique complexe

`DT Register` n'est pas qu'un plugin :

- 4004 inscriptions historiques
- nombreuses tables applicatives
- menus specifiques
- tarification et parcours d'achat relies au site

Risque :

- perdre un historique commercial utile ;
- sous-estimer le besoin fonctionnel reel ;
- refaire un simple formulaire alors que le besoin est transactionnel.

### 4. Agenda / planification

`JEvents` contient 250 evenements.

Risque :

- si cet agenda pilote les sessions ou les disponibilites, la refonte doit traiter le sujet comme un besoin metier et non comme un contenu secondaire.

### 5. Formulaire de contact ancien

- `BreezingForms` 1.9.1
- logique JS historique
- reCAPTCHA invisible

Risque :

- maintenance difficile ;
- dette de compatibilite ;
- reprise fonctionnelle a simplifier.

### 6. Incoherence de base de donnees

- coexistence de tables `jh3_` et `jos_`
- traces de migrations / imports successifs

Risque :

- ambiguite sur la source de verite ;
- donnees orphelines ;
- reprise de donnees plus couteuse que prevu.

## Fonctions historiquement cassees ou encore fragiles

Les rapports existants indiquent notamment :

- la galerie front a deja ete en defaut selon l'environnement, mais elle repond de nouveau sur l'instance corrigee ;
- le tunnel `DT Register` a deja ete en erreur, puis a ete remis en service par correctifs legacy ;
- plusieurs ecrans d'administration Joomla 3 restent fragiles selon le contexte ;
- l'edition d'article et de module reste encore bloquee sur une incompatibilite `getWebAssetManager()`, meme si l'edition de menu et de prestation `DT Register` a ete rouverte.

Conclusion :

La refonte peut viser une rationalisation assumee sans exiger de parite parfaite avec un existant qui a deja demande des correctifs conservatoires et reste partiellement degrade.

## Vigilances pour le cadrage

- Distinguer les besoins reels de reservation des traces techniques historiques.
- Arbitrer la reprise ou l'archivage des 4004 inscriptions.
- Verifier les obligations legales autour des donnees clients conservees.
- Reprendre proprement les formulaires, emails, anti-spam et confirmations.
- Nettoyer l'arborescence fonctionnelle pour retirer les acces techniques exposes (`register`, menus cache, etc.).
