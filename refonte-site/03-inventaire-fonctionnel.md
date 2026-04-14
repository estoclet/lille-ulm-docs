# Inventaire fonctionnel

## Navigation principale

Entrees publiees observees dans `menu-principal` :

- Accueil
- Nos tarifs
- Location ULM
- Nos ULM
- Galerie photo
- Nous trouver
- Nous contacter
- FAQ
- `register` (entree technique exposee publiquement)

## Navigation secondaire / footer

- Mentions legales
- Plan de site
- Recommander ce site
- Partenaires

## Accueil

Fonctions observees :

- logo et baseline commerciale ;
- menu horizontal ;
- slider d'accroche `RokStories` avec deux messages promotionnels ;
- trois blocs de reassurance en bas de page :
  - consultation des tarifs ;
  - video Facebook embarquee ;
  - paiement securise en ligne.

Messages cles mis en avant :

- survol de Lille et du Nord ;
- offres "accessibles" ;
- achat du bon en ligne ;
- prise de rendez-vous ensuite par telephone ;
- paiement securise via Credit Agricole.

## Parcours commercial

Le parcours visible reconstitue est le suivant :

1. L'utilisateur consulte la page "Nos tarifs".
2. Il choisit une offre.
3. Il clique sur "Achetez le bon en ligne".
4. Il est redirige vers une page `DT Register`.
5. Le site indique ensuite de fixer la date par telephone avec un code de confirmation.

## Offres identifiees

Offres visibles dans les menus et les contenus :

- Bapteme de l'air - seance de 15 min
- Bapteme de l'air - seance de 30 min
- Bapteme de l'air - seance de 1 heure
- Bapteme de l'air - seance de 1h30
- Cours de pilotage - seance de 45 min
- 6 lecons de pilotage de 40 mn
- Une entree de test existe aussi dans les donnees

Prix observes dans la page "Nos tarifs" ou dans les tables de tarification :

- 49,90 EUR
- 99,90 EUR
- 145 EUR
- 179,90 EUR
- 249,90 EUR
- 590 EUR

## Reservation / historique clients

Ce n'est pas une fonctionnalite anecdotique :

- 4004 inscriptions historiques detectees dans `jh3_dtregister_user`
- 250 evenements `JEvents`
- plusieurs entrees de menu cache ou techniques dediees a des pages d'inscription

Hypothese raisonnable :

- `DT Register` porte les transactions / inscriptions ;
- `JEvents` sert de support d'agenda ou de planification associee a l'activite ;
- la logique metier complete doit etre requalifiee avant toute refonte.

## Formulaire de contact

Page publique `Nous contacter` :

- composant `BreezingForms`
- formulaire `ff_form1`
- champs obligatoires :
  - nom
  - adresse e-mail
  - telephone
  - objet
  - message
- protection par reCAPTCHA invisible
- message de soumission ajax / page suivante

Coordonnees visibles :

- nom : Lille ULM
- email : `contact@bapteme-air-lille.fr`
- telephone : `06 09 635 635`
- adresse : Aerodrome de Lille Marcq

## Localisation

Page `Nous trouver` :

- article editorial avec titre "Lille ULM"
- sous-titre "Aerodrome de Bondues Nord (59)"
- carte Google Maps embarquee via `mod_wrapper`

## Galerie photo

Composant : `PhocaGallery`

Categories publiees :

- Le pilote
- Nos ULM
- En direct du cockpit
- Bonus : un atterrissage comme si vous y etiez!

Volume :

- 4 categories
- 65 images publiees

Usage attendu en refonte :

- rassurance visuelle ;
- projection dans l'experience ;
- preuve d'activite ;
- mise en valeur de l'appareil et du pilote.

## Sitemap et SEO

Fonctions observees :

- sitemap HTML via `OSMap`
- metadonnees remplies dans Joomla
- URLs SEF avec suffixe `.html`
- maillage de base via menus et CTA internes

## Fonctions potentiellement obsoletes ou secondaires

- "Recommander ce site" en `mailto:`
- lien "Ajouter ce site aux favoris" depublication
- composant `Weblinks`
- `XMap` en doublon de `OSMap`
- `RokGallery` installe mais sans fichiers exploites
