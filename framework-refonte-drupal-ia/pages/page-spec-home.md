# Page spec - Home

## Objectif de la page

Capter l'attention en moins de 3 secondes, transmettre l'emotion du vol en ULM,
et emmener directement vers les offres ou le contact.

## Public cible

- visiteur decouvrant Lille ULM pour la premiere fois ;
- proche cherchant une idee de cadeau experience ;
- prospect qui compare avant d'acheter.

## Blocs autorises

- hero plein ecran avec photo aerienne ;
- accroche courte et promesse metier ;
- apercu des offres principales (3 a 4 cards) ;
- bandeau de rassurance (valeurs cles) ;
- apercu galerie photos ;
- bloc contact humain visible ;
- CTA final vers les offres.

## CTA principaux

- decouvrir nos offres (vers /offres) ;
- nous appeler (lien tel:) ;
- offrir une experience (vers /offres avec filtre cadeau si applicable).

## Sections Layout Builder

| Section | Verrouillee | Modifiable gestionnaire |
|---------|-------------|------------------------|
| Hero | oui | titre, sous-titre, image de fond, 2 CTA |
| Apercu offres | non | offres affichees (ordre, nombre) |
| Bandeau rassurance | non | 3 a 4 messages courts, icones |
| Galerie apercu | non | photos selectionnees |
| Contact strip | oui | telephone, horaires |

## Champs modifiables par le gestionnaire

- titre hero et accroche ;
- image hero (Media) ;
- textes de rassurance ;
- offres mises en avant ;
- photos de galerie ;
- numero de telephone et horaires de contact.

## Contraintes SEO

- H1 unique sur la page, axe sur "bapteme de l'air ULM Lille" ;
- metadata title et description dediees ;
- image hero avec attribut alt renseigne ;
- page non dupliquee avec /offres.

## Contraintes accessibilite

- image hero avec texte alternatif ou aria-hidden si purement decorative ;
- CTA avec intitules explicites (pas "cliquez ici") ;
- contraste texte sur hero >= 4,5:1 (overlay sombre sur photo) ;
- navigation clavier possible sur toutes les cards.

## Variantes autorisees

- hero avec video en fond (option future, non prioritaire) ;
- mise en avant d'une offre saisonniere dans le hero ;
- bandeau promotionnel au-dessus du hero (ex : bon cadeau fetes).

## Composants relies

- hero-full (SDC) ;
- offer-card (SDC) ;
- section-band (SDC) ;
- gallery-grid (Vue Media) ;
- contact-strip (SDC).

## Source de verite

- ADR-018-charte-graphique-et-design-tokens.md
- ADR-007-composition-editoriale-low-code.md
- briefs/feature-brief-parcours-offres-vente.md
