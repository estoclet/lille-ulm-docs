# ADR-019 - Architecture du thème et des composants SDC

## Contexte

La refonte nécessite un thème Drupal 11 qui :

- implémente les design tokens ADR-018 (`#00aace`, `#ffe600`, Inter) ;
- permet la composition éditoriale via Layout Builder (ADR-007) ;
- expose des composants réutilisables pour le gestionnaire ;
- reste maintenable sans expertise front-end avancée.

## Issue liée

`#43`

## Décision

### Thème de base : Radix 6.x

Radix 6.x est retenu comme thème parent pour `lille_ulm_theme`.

Raisons :

- base Bootstrap 5 alignée avec les composants ui_suite_bootstrap ;
- starterkit complet (SCSS, JS, Twig, SDC) prêt à être spécialisé ;
- compatible Drupal 11 core (`^10.3 || ^11`) ;
- intégration Layout Builder et SDC de première classe.

### Sous-thème : `lille_ulm_theme`

Créé depuis `radix_starterkit`, tous les fichiers renommés.

Fichiers clés :

| Fichier | Rôle |
|---------|------|
| `src/scss/base/_variables.scss` | Bootstrap overrides + tokens Sass (`$primary`, `$warning`, Inter) |
| `src/scss/base/_elements.scss` | CSS custom properties `:root` + `.btn-primary` dégradé |
| `build/css/main.style.css` | CSS compilé, versionné dans le repo |
| `components/*/` | Composants SDC du projet |

### Compilation SCSS

Laravel Mix (webpack) est incompatible avec Node 20 (ProgressPlugin API).
La compilation utilise dart-sass standalone :

```bash
npm run sass:build
# = sass src/scss/main.style.scss build/css/main.style.css \
#     --load-path=node_modules --style=compressed --no-source-map
```

Le CSS compilé est **versionné** dans le dépôt (`build/css/main.style.css`).
Cela évite de dépendre d'un environnement Node pour déployer.

Conséquence : modifier le SCSS nécessite de relancer `npm run sass:build` et committer.

### Modules contrib activés

| Module | Version | Rôle |
|--------|---------|------|
| `radix` | ^6 | Thème parent Bootstrap 5 |
| `ui_suite_bootstrap` | 5.2.0 | Bibliothèque de composants Bootstrap pour SDC |
| `layout_builder_styles` | ^2 | Classes CSS sur les sections Layout Builder |
| `layout_builder_restrictions` | ^3 | Restriction de la palette de blocs par display |
| `section_library` | ^2 | Templates de sections réutilisables |

### Composants SDC du projet

Groupe `Lille ULM`, dans `web/themes/custom/lille_ulm_theme/components/` :

| Composant | ID SDC | Usage |
|-----------|--------|-------|
| Hero plein écran | `lille_ulm_theme:hero-full` | Home, pages catégorie |
| Carte offre | `lille_ulm_theme:offer-card` | Home, listing /offres |
| Bandeau de section | `lille_ulm_theme:section-band` | Étapes, rassurance, valeurs |
| Bandeau contact | `lille_ulm_theme:contact-strip` | Footer de page, page contact |

Chaque composant contient : `.component.yml` (props + slots), `.twig`, `.css`.
Le CSS est auto-chargé par le système SDC de Drupal core.

### Layout Builder

Activé avec overrides sur :

- `node.page.default`
- `commerce_product.default.default`

`layout_builder_restrictions` limite la palette à :
Content fields, Product fields, Commerce, Inline blocks, Lists (Views), Forms, Webform.

## Pourquoi ce choix

- Radix évite d'écrire un thème Drupal 11 de zéro tout en restant transparent
- Le CSS versionné simplifie le déploiement (pas de build step en CI)
- Les composants SDC sont la primitive éditoriale principale (ADR-007) — ils n'utilisent que les tokens ADR-018

## Alternatives écartées

- **Olivero** comme base : trop opinioné, peu de contrôle sur la structure HTML
- **Bootstrap Barrio** : moins bien intégré Layout Builder que Radix 6
- **Laravel Mix** : incompatible Node 20 (ProgressPlugin), remplacé par dart-sass CLI
- **gin_lb** : incompatible Drupal 11 + gin_toolbar 3.x, exclu

## Conséquences

- tout nouveau composant SDC va dans `components/` avec les 3 fichiers requis
- `npm run sass:build` doit être relancé après chaque modification SCSS, et le CSS commité
- les templates Twig spécifiques aux types de contenu vont dans `templates/`
- `layout_builder_styles` permet d'ajouter des variantes visuelles sans créer un composant entier

## Impact IA

- fichiers à relire : `ADR-018-charte-graphique-et-design-tokens.md`, `ADR-007-composition-editoriale-low-code.md`
- lots concernés : theming, composants SDC, templates Twig commerce
- risques : ne pas dupliquer les tokens dans les composants — pointer vers `_variables.scss`
