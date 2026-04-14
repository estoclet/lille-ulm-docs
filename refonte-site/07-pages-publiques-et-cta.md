# Pages publiques et CTA

## Vue d'ensemble

Pages publiques principales relevees :

- `/`
- `/nos-offres.html`
- `/location-ulm.html`
- `/nos-ulm.html`
- `/galerie-photo.html`
- `/nous-trouver.html`
- `/nous-contacter.html`
- `/faq.html`
- `/mentions-legales.html`
- `/partenaires.html`
- `/plan-de-site.html`
- `/agenda`
- `/register.html`

## Constat SEO rapide

Les metadonnees sont heterogenes :

- quelques pages ont un titre et une description specifique ;
- beaucoup de pages reutilisent la meme meta description generique ;
- certains intitulés publics ne sont pas propres (`contact`, `register`) ;
- la page partenaires contient des liens annuaire datés et peu qualitatifs ;
- les URLs sont propres mais restent marquees par l'heritage Joomla 3.

## Mapping par page

### Accueil `/`

- titre : `Lille ULM Nord Baptême de l'air`
- fonction : page d'atterrissage commerciale
- contenus cles :
  - baseline de marque
  - slider d'accroche
  - bloc tarifs
  - video Facebook
  - bloc paiement securise
- CTA :
  - aller vers les tarifs
  - consulter les offres

### Nos offres `/nos-offres.html`

- titre : `Lille ULM : Nos offres`
- description specifique : oui
- fonction : page commerciale centrale
- contenus cles :
  - presentation des baptemes et initiations
  - rappel depart Bondues
  - description du parcours d'achat
  - reassurance paiement
- CTA detects :
  - achat seance 15 min `eventId=10`
  - achat seance 30 min `eventId=18`
  - achat seance 1h `eventId=17`
  - achat seance 1h30 `eventId=11`
  - achat cours 45 min `eventId=15`
  - achat 6 lecons `eventId=12`

### Location ULM `/location-ulm.html`

- titre : `Location ULM`
- fonction : page commerciale secondaire
- contenus cles :
  - promesse "Louez la liberté"
  - mise en avant de l'aerodrome de Bondues
  - mise en avant de l'ULM TeamEurostar
  - offres de location 1h, 2h, 3h, 4h, 10h
- point d'attention :
  - il faut verifier si ces offres doivent exister encore dans la cible

### Nos ULM `/nos-ulm.html`

- titre : `Nos ULM`
- description specifique : oui
- fonction : page de reassurance technique
- contenus cles :
  - ULM TeamEurostar
  - arguments securite / confort / fiabilite
  - caracteristiques de l'appareil
  - mention d'un second appareil "Moto du Ciel"

### Galerie `/galerie-photo.html`

- titre : `Lille ULM: Nos photos lors de baptêmes de l'air`
- fonction : galerie de preuve sociale / projection
- contenus cles :
  - categories pilote / appareil / cockpit / atterrissage
- point d'attention :
  - brique visible importante meme si l'implementation actuelle est fragile

### Nous trouver `/nous-trouver.html`

- titre : `Lille ULM NORD`
- description specifique : oui
- fonction : localisation
- contenus cles :
  - aerodrome de Bondues
  - carte Google Maps embarquee

### Nous contacter `/nous-contacter.html`

- titre : `contact`
- fonction : prise de contact
- contenus cles :
  - telephone affiche
  - formulaire BreezingForms
  - reCAPTCHA invisible
- champs :
  - nom
  - email
  - telephone
  - objet
  - message

### FAQ `/faq.html`

- titre : `Lille ULM: FAQ`
- fonction : reponse aux objections
- point d'attention :
  - une extraction complete du contenu reste a faire pour qualifier les questions reellement utiles

### Mentions legales `/mentions-legales.html`

- titre : `Mentions légales`
- fonction : conformite legale

### Partenaires `/partenaires.html`

- titre : `Partenaires`
- fonction actuelle :
  - essentiellement une page de liens annuaires / backlinks
- recommandation :
  - forte candidate a la suppression, a la reecriture ou a la relegation hors navigation principale

## Defauts de surface a corriger en refonte

- page `register` exposee dans le menu principal ;
- page contact mal titree ;
- duplication de meta descriptions ;
- logique de CTA eparpillee entre contenus, menus caches et composants tiers ;
- page partenaires peu qualitative ;
- footer encombre de liens faibles herites d'un SEO ancien.
