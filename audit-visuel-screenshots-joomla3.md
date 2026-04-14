# Audit visuel par screenshots

Date: 2026-04-14

Source des captures:
- rapport HTML: [/home/eric/Projets/lille-ulm/audit-screenshots/j3-audit-2026-04-14/rapport-j3-audit.html](/home/eric/Projets/lille-ulm/audit-screenshots/j3-audit-2026-04-14/rapport-j3-audit.html)
- dossier screenshots: [/home/eric/Projets/lille-ulm/audit-screenshots/j3-audit-2026-04-14/screenshots](/home/eric/Projets/lille-ulm/audit-screenshots/j3-audit-2026-04-14/screenshots)

Acces administration utilise pour l'audit:
- login: `bapteme`
- mot de passe: `GcmuV3463VV5qq`

## Synthese

Le site public Joomla 3 est globalement affichable et coherent visuellement. Quatre anomalies techniques visibles ont ete corrigees pendant cet audit:

- les `Notice: Undefined variable: dataAttribute` en administration ont disparu apres correction defensive des layouts Joomla `list.php`, `groupedlist.php` et `list-fancy-select.php`;
- le menu public `Agenda` ouvre de nouveau le calendrier JEvents au lieu de rediriger vers un login;
- le bloc video casse de l'accueil ne pointe plus vers l'ancien embed YouTube mort `ivqPSB-kJdk` et charge maintenant la video Facebook `https://www.facebook.com/LilleULM/videos/2247570525258144/`;
- la page contact n'utilise plus sa cle reCAPTCHA invalide en environnement `*.ddev.site`, grace a un override local de BreezingForms vers les clefs de test Google.

Il reste toutefois plusieurs anomalies visibles importantes avant retransfert FTP:

- plusieurs pages sont tres datees ou pauvres visuellement: FAQ, mentions legales, partenaires, plan de site.

## Pages publiques

### Accueil

- Etat visuel: page chargee correctement, charte graphique complete, slider visible, blocs d'appel principaux visibles.
- Etat visuel final: le bloc `Video` ne retombe plus sur l'ancien embed YouTube casse; il charge maintenant la video Facebook fournie par `LilleULM`.
- Defauts visibles restants: item `register` affiche seul sous le menu principal, ce qui donne l'impression d'un reliquat de navigation.
- Observation produit: l'argumentaire est axe sur les prix et le paiement securise, avec un design tres ancien mais fonctionnel.

### Nos offres

- Etat visuel: page lisible, grille des offres bien visible, CTA bleus `Achetez le bon en ligne`.
- Defauts visibles: contenu tres dense, hierarchie faible, footer tres proche du contenu; formulation et presentation anciennes.
- Observation produit: page toujours exploitable comme vitrine, mais elle depend ensuite d'un tunnel casse cote disponibilites.

### Location ULM

- Etat visuel: page chargee correctement, grandes images presentes, grille des offres de location visible.
- Defauts visibles: mise en page longue et statique, forte densite de texte, lien discret `Accès à l'agenda et paiement` peu mis en valeur.

### Nos ULM

- Etat visuel: page chargee correctement, images presentes, contenu long mais lisible.
- Defauts visibles: densite textuelle elevee, mise en page vieillissante, faible mise en avant des actions.

### Galerie photo

- Etat visuel: page d'index Phoca Gallery correcte, categories visibles, navigation exploitable.
- Defauts visibles: forte vacuite visuelle sous le bloc galerie; branding `Powered by Phoca Gallery` tres present.

### Galerie - Nos ULM

- Etat visuel: miniatures visibles, pagination visible, aucune casse majeure.
- Defauts visibles: premiere tuile de retour tres pauvre visuellement; plusieurs vignettes portent des titres techniques ou tronques; ergonomie ancienne.

### Galerie - Le pilote

- Etat visuel: galerie exploitable, miniatures chargees.
- Defauts visibles: page tres vide avec seulement quatre vignettes; usage faible de l'espace.

### Galerie - En direct du cockpit

- Etat visuel: galerie exploitable, miniatures chargees, pagination visible.
- Defauts visibles: nombreux titres techniques de fichiers; presentation peu editorialisee.

### Galerie - L'atterrissage

- Etat visuel: galerie exploitable, miniatures chargees.
- Defauts visibles: page encore plus vide que les autres sous-categories; faible valeur percue.

### Nous trouver

- Etat visuel: page chargee correctement, Google Maps embarque visible.
- Defauts visibles: page quasi vide en dehors de la carte; dependance forte a l'embed externe; contenu contextuel minimal.

### Nous contacter

- Etat visuel: formulaire visible et utilisable, coordonnees presentes.
- Etat visuel final: le formulaire ne charge plus la cle reCAPTCHA invalide sur `*.ddev.site`, donc l'anomalie rouge/blanche parasite n'est plus reproduite en DDEV.
- Defauts visibles restants: icones d'adresse et telephone semblent cassees ou absentes; page tres pauvre editorialement.

### FAQ

- Etat visuel: page chargee correctement, contenu lisible.
- Defauts visibles: page tres courte, typographie petite, aspect faible confiance; contenu date.

### Mentions legales

- Etat visuel: page chargee correctement.
- Defauts visibles: mentions legales manifestement obsoletes, reference a HOB France Services et OVH; presentation minimale.

### Partenaires

- Etat visuel: page chargee correctement.
- Defauts visibles: page ressemble a une ferme de liens/annuaires; forte vacuite; aucune valeur commerciale claire.
- Decision recommandee: ne pas conserver en l'etat.

### Plan de site

- Etat visuel: page chargee correctement.
- Defauts visibles: structure sommaire, indentation tres rustique, lien `register` expose publiquement comme une page de premier niveau.

## Pages transactionnelles

### DT Register - register

- Etat initial: la page ne fatal plus, mais affichait soit un message de fermeture, soit une liste vide.
- Correctif applique: réouverture technique des offres publiques via la table active `jh3_dtregister_group_event`, avec prolongation des dates de fin en 2030 et remise en cohérence des dates de début.
- Etat final: la page liste de nouveau les offres `15 min`, `30 min`, `45 min`, `1 heure`, `1h30` et `6 leçons`.
- Defaut restant: logique métier encore artificielle, car ces dates ont été prolongées pour remise en service technique et non reconstruites depuis un planning réel.

### DT Register - offres 15 min, 30 min, 45 min

- Etat initial: les trois captures montraient une liste vide, avec un bandeau d'erreur `End time less then today`.
- Cause identifiee: `dtend` historiques en 2025 et incoherences `starttime` / `dtstarttime`.
- Correctif applique:
  - dates de fin poussees en 2030 sur les offres publiees;
  - `cut_off_date` réalignées;
  - `startdate` repositionnees au 14 avril 2026 avec `starttime = 00:00:00` pour sortir de l'etat `future_event`;
  - `dtstart` laisse sur une borne technique de disponibilite.
- Etat final: les pages n'affichent plus la liste vide ni la clé parasite `DT_START_TIME_GREATER_THEN_CURRENT_DATE`; elles retombent sur une liste peuplée d'offres avec CTA d'inscription actif.
- Defaut restant: la logique temporelle reste artificielle, car elle sert une remise en service technique et non un planning reconstruit métier.

### DT Register - audit du tunnel one-page

Source:
- captures dediees: [/home/eric/Projets/lille-ulm/lille-ulm-docs/dtregister-flow-audit-2026-04-14](/home/eric/Projets/lille-ulm/lille-ulm-docs/dtregister-flow-audit-2026-04-14)

Constat capture par capture:
- `01-register-list.png`: la liste publique des offres est visible et les parcours ne sont plus fermes.
- `02-onepage-initial.png`: la page one-page checkout charge correctement avec les etapes `S'inscrire`, `Details`, `Paiement`.
- `03-individual-filled.png`: le formulaire visible exploitable est bien `individual_*`, pas `billing_*`; les champs attendus sont prenom, nom, code postal, email, telephone, prenom du beneficiaire, nom du beneficiaire.
- `04-after-suivant.png`: le bouton `Suivant` fonctionne et amene au panier `Inscription a un evenement: Mon Panier`, avec une ligne de panier coherente et un total de `49.90 EUR`.

Defauts visibles a l'etape paiement:
- la progression fonctionne jusqu'au panier, donc le tunnel n'est pas casse des la premiere etape;
- les notices PHP du bloc `Mollie` identifiees pendant l'audit ont ete corrigees ensuite dans `plugins/system/ja_payment/tmpl/form.php`; le HTML rendu ne les affiche plus;
- le moyen `Joomlart_Paylater` est present, avec l'option `Cheque ou virement`.

Impact:
- le composant est de nouveau parcourable jusqu'au panier;
- l'etape paiement n'injecte plus de notices visibles apres correctif defensif sur `Mollie`;
- post-audit, le parcours `Paylater` a aussi ete valide localement jusqu'a `/remerciement.html` apres realignement des URLs absolues de retour sur le chemin local existant.

### Agenda via menu protege

- Etat initial: redirection vers un ecran de connexion frontal avec message `Veuillez d'abord vous identifier`.
- Cause identifiee: l'item actif etait dans la table `jh3_menu`, pas `jos_menu`, avec `access = 2`.
- Correctif applique: l'item `jh3_menu.id = 22` a ete repasse au niveau public du site.
- Etat final: capture regenee validee, l'URL `/agenda` affiche bien le calendrier JEvents.

### Agenda JEvents direct

- Etat visuel: calendrier JEvents charge correctement, barres d'outils visibles, grille mensuelle affichee.
- Defauts visibles: calendrier vide a la date capturee; integration visuelle moyenne.
- Conclusion: le composant fonctionne, c'est surtout le routage/menu public qui est mal configure.

## Administration

### Login administration

- Etat visuel: page de connexion Joomla standard propre et exploitable.
- Defauts visibles: aucun blocage visuel notable.

### Administration - Articles

- Etat visuel final: liste des articles chargee apres connexion, sans `Notice` visible apres correctif.
- Correctif applique: initialisation defensive de `$dataAttribute` dans les layouts Joomla concernes.

### Administration - Menus

- Etat visuel final: ecran charge correctement, sans `Notice` visible.

### Administration - Modules

- Etat visuel: ecran charge correctement.
- Etat visuel final: ecran charge correctement, sans `Notice` visible.
- Observation utile: les modules cle visibles existent bien encore (`JEvents`, `DT Register`, `Menu secondaire`, `Video`, `Paiement sécurisé en ligne`).

## Conclusion operationnelle avant FTP

Le site est de nouveau navigable et administrable, avec agenda public repare, back-office nettoye de ses notices visibles, et tunnel `DT Register` reouvert jusqu'au panier. Il n'est toutefois pas encore "totalement operationnel" au sens metier/public.

Les points a corriger avant retransfert devraient etre traites dans cet ordre:

- investiguer le message d'erreur parasite visible sur la page contact;
- verifier les medias casses ou manquants sur la page contact et la video d'accueil;
- valider metier les nouvelles echeances `2030` du tunnel `DT Register`, qui remettent le composant en service mais restent un correctif technique conservatoire.

Note technique importante:
- la base active du site utilise le prefixe `jh3_`; les tables `jos_` coexistent mais ne pilotent pas le front actif. Toute correction SQL future doit viser d'abord `jh3_`.
