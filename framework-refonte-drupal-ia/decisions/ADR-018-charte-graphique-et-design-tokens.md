# ADR-018 - Charte graphique et design tokens derives du logo SVG

## Contexte

Le gestionnaire a fourni un logo SVG Inkscape (`logo_Lille-ULM.svg`).
Ce logo constitue la seule source de verite graphique existante a ce stade.

Elements observes dans le fichier SVG :

- Wordmark "Lille" : `sans-serif Bold`, 22,7 px, couleur `#00aace`
- Wordmark "ULM" : `sans-serif Bold`, 16,7 px, couleur `#00aace`
- Silhouette ULM vectorielle avec degrede `#00aace` (debut) vers `#ffe600` (fin)
- Contour blanc (`stroke: #ffffff`) sur le texte et la silhouette
- Fond SVG transparent / blanc selon usage
- Dimensions : environ 70,6 mm x 34,2 mm

La silhouette est entierement vectorielle et reutilisable comme actif decoratif.

## Issue liee

`#43`

## Decision

Les design tokens du projet sont derives directement du logo :

### Couleurs

| Token | Valeur | Usage |
|-------|--------|-------|
| `--color-primary` | `#00aace` | Liens, icones, accents principaux |
| `--color-accent` | `#ffe600` | CTA secondaires, badges, highlights |
| `--color-cta-start` | `#00aace` | Debut du degrede CTA principal |
| `--color-cta-end` | `#ffe600` | Fin du degrede CTA principal |
| `--color-text` | `#1a1a2e` | Corps de texte (quasi-noir, pas pur) |
| `--color-bg` | `#ffffff` | Fond principal |
| `--color-bg-alt` | `#f4f8fa` | Fond sections secondaires |
| `--color-on-dark` | `#ffffff` | Texte et logo sur fonds sombres ou photos |

Le degrede `#00aace → #ffe600` est le signature graphique du projet.
Il s'applique : CTA principaux (`background: linear-gradient`), traits de soulignement actifs, indicateurs de progression checkout.

### Typographie

La police retenue est **Inter** (Google Fonts, open source).

Justification : correspondance directe avec le `sans-serif Bold` du logo.
Inter est la reference actuelle du `sans-serif` moderne neutre et lisible.

| Role | Graisse | Taille de base |
|------|---------|----------------|
| Display / Hero | Bold 700 | 48-64 px |
| Titre de section | SemiBold 600 | 28-36 px |
| Titre de carte | SemiBold 600 | 18-22 px |
| Corps | Regular 400 | 16 px |
| Caption / label | Medium 500 | 13-14 px |

### Usage du logo sur fonds sombres

Le contour blanc du SVG original confirme que le logo est prevu pour les fonds sombres.
Le hero plein-ecran sur photo aerienne est donc coherent avec l'identite visuelle.
La version "logo blanc" est obtenue directement en surchargeant `fill` et `stroke` via CSS.

### Silhouette ULM comme actif decoratif

La silhouette vectorielle est reutilisable dans le theme :

- favicon et touch icon (export PNG depuis SVG)
- fond de section en filigrane (opacity faible)
- separateur de section stylise
- icone de chargement / splash screen eventuel

## Pourquoi ce choix

- source unique de verite : le logo existant evite d'inventer une charte de toutes pieces
- coherence maximale entre logo imprime, logo web et interface
- le degrede est deja present dans le SVG : l'exploiter dans l'UI est naturel, pas decoratif arbitraire
- Inter est disponible gratuitement, performante en web, tres lisible sur mobile

## Alternatives ecartees

- Outfit : bon choix generique mais moins justifie que Inter par rapport au logo
- couleurs inventees independamment du logo : risque d'incoh erence entre supports
- palette monochrome cyan seule : perte de la dimension energetique du jaune

## Consequences

- le sous-theme Radix `lille_ulm_theme` definit ces tokens dans `_variables.scss` ou `tokens.css`
- tout composant SDC utilise uniquement ces tokens, jamais de valeurs hexadecimales en dur
- le CTA principal de chaque page porte le degrede `--color-cta-start → --color-cta-end`
- les fondations graphiques sont documentees ici ; toute evolution doit mettre a jour cet ADR

## Impact IA

- fichiers a relire : `ADR-007-composition-editoriale-low-code.md`, `pages/page-spec-nos-offres.md`
- lots concernes : theming, composants SDC, Layout Builder styles
- risques de duplication : ne pas redefinir les couleurs dans les fichiers de composants ; pointer vers cet ADR
