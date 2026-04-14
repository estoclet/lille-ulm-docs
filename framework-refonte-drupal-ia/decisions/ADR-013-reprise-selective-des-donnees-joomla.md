# ADR-013 - Reprendre selectivement les donnees Joomla 3

## Contexte

Le site source Joomla 3 porte plusieurs familles de donnees :

- contenus editoriaux ;
- medias ;
- URLs et signaux SEO ;
- historique transactionnel `DT Register` ;
- agenda `JEvents` ;
- donnees issues de composants et modules legacy.

Le besoin de reprise existe, mais le futur site Drupal ne doit pas devenir une recopie structurelle du legacy.

## Decision

La strategie retenue est une **reprise selective par lots**, avec trois traitements possibles pour chaque famille de donnees :

- **migration** vers Drupal si la donnee reste utile dans la cible ;
- **archivage** si la donnee doit rester consultable sans vivre dans Drupal ;
- **abandon assume** si la donnee ne sert ni l'usage cible, ni le SEO, ni une obligation metier.

## Regles

- ne jamais migrer un composant Joomla "tel quel" ;
- partir des objets cibles Drupal, pas des tables legacy ;
- documenter explicitement pour chaque lot : source, cible, traitement, justification ;
- privilegier une migration one-shot au moment du cutover ;
- n'ouvrir un besoin de delta que si la bascule du legacy est durablement decalee ;
- exclure par defaut les assets et donnees purement techniques Joomla.

## Priorites de reprise

### Priorite 1 - A migrer quasi certainement

- pages publiques encore utiles ;
- informations de contact et de localisation ;
- medias metier utiles ;
- URLs critiques et redirections SEO.

### Priorite 2 - A trier puis migrer partiellement

- galerie et visuels marketing ;
- messages transactionnels utiles comme base de reconstruction ;
- certains contenus support ou FAQ ;
- quelques donnees de catalogue ou d'offres si elles evitent une ressaisie inutile.

### Priorite 3 - A archiver par defaut

- historique `DT Register` ;
- historiques de paiement legacy ;
- pages de remerciement anciennes ;
- donnees `JEvents` si aucun usage cible n'est confirme.

### Priorite 4 - A ne pas reprendre sauf preuve contraire

- modules RocketTheme / Gantry ;
- assets techniques Joomla ;
- pages techniques `register` ;
- reliquats d'annuaires, favoris, weblinks ;
- mecanismes internes des composants legacy.

## Doctrine par source legacy

### Contenus Joomla natifs

- reprendre ce qui sert encore conversion, reassurance, information pratique ou SEO ;
- reecrire plutot que recopier lorsque le volume editorial reste faible.

### `PhocaGallery`

- reprendre les images source utiles ;
- exclure les miniatures generees ;
- faire un tri editorial avant import.

### `DT Register`

- ne pas migrer le moteur ;
- archiver l'historique complet par defaut ;
- n'envisager une migration applicative que pour des donnees encore actives dans la cible, par exemple des bons encore valides ou des obligations SAV / comptables confirmees.

### `JEvents`

- ne pas migrer par defaut ;
- ne reprendre que si un usage public ou interne concret est confirme.

### Modules et composants secondaires

- reprendre seulement les contenus qu'ils exposent, jamais leur structure technique ;
- reclasser chaque source dans une cible Drupal simple : contenu, media, redirection, archive.

## Sortie attendue pour chaque lot

- source Joomla ;
- volume estime ;
- cible Drupal ou hors Drupal ;
- traitement retenu : migrer / archiver / abandonner ;
- point bloquant eventuel ;
- responsable de validation metier.

## Consequences

- la migration devient un chantier de qualification, pas un simple export/import ;
- le legacy peut etre eteint sans imposer sa structure a Drupal ;
- les composants `DT Register` et `JEvents` restent des sources a lire, pas des briques a reconduire ;
- les obligations historiques doivent etre validees tres tot pour eviter une surprise tardive.
