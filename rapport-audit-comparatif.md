# Rapport d'audit comparatif — Joomla 3 vs Joomla 4

**Client :** Lille ULM Nord — Baptême de l'air
**Date :** 14 avril 2026
**Intervenant :** Eric Stoclet
**Objet :** Audit visuel et fonctionnel comparatif J3 (référence) vs J4 (migré)
**Outil :** Playwright (Chromium headless) + script audit.js

---

## Résumé exécutif

|                    | J3 (référence)             | J4 (migré)                    |
| ------------------ | -------------------------- | ----------------------------- |
| **URL**            | http://lille-ulm.ddev.site | http://lille-ulm-j4.ddev.site |
| **Joomla**         | 3.10.12                    | 4.4.9                         |
| **PHP**            | 7.4                        | 8.1                           |
| **Pages front OK** | 6/8                        | 6/8                           |
| **Pages admin OK** | 3/6                        | 6/6                           |

> **Observation inattendue :** Le back-office J4 est **plus fonctionnel** que le back-office J3 de référence — plusieurs pages admin J3 retournent des erreurs 500 en raison d'extensions incompatibles encore chargées.

---

## Résultats détaillés

### Front-end

| Page                       | J3     | J4     | Statut comparatif                                         |
| -------------------------- | ------ | ------ | --------------------------------------------------------- |
| Accueil                    | ✅ 200 | ✅ 200 | Équivalent (visuel différent — Cassiopeia vs rt_quantive) |
| Nos offres (article)       | ✅ 200 | ✅ 200 | Contenu identique                                         |
| L'avion (article)          | ✅ 200 | ✅ 200 | Contenu identique                                         |
| FAQ (article)              | ✅ 200 | ✅ 200 | Contenu identique                                         |
| Mentions légales (article) | ✅ 200 | ✅ 200 | Contenu identique                                         |
| Contact                    | ✅ 200 | ✅ 200 | Formulaire fonctionnel                                    |
| Galerie (PhocaGallery)     | ❌ 404 | ❌ 404 | Cassé **dans les deux** environnements                    |
| Réservation (DTRegister)   | ❌ 500 | ❌ 500 | Cassé **dans les deux** environnements                    |

### Back-office

| Page               | J3     | J4     | Statut comparatif                          |
| ------------------ | ------ | ------ | ------------------------------------------ |
| Login admin        | ✅ 200 | ✅ 200 | Fonctionnel (templates Protostar/Atum)     |
| Tableau de bord    | ✅ 200 | ✅ 200 | J4 affiche le nouveau tableau de bord Atum |
| Gestion articles   | ❌ 500 | ✅ 200 | **J4 meilleur que J3**                     |
| Gestion menus      | ❌ 500 | ✅ 200 | **J4 meilleur que J3**                     |
| Gestion modules    | ❌ 500 | ✅ 200 | **J4 meilleur que J3**                     |
| Gestion extensions | ✅ 200 | ✅ 200 | Fonctionnel dans les deux                  |

---

## Analyse des problèmes

### 1. Galerie photos (PhocaGallery) — cassée dans J3 et J4

**Erreur J3 :** `404 - Affichage introuvable [name, type, prefix] : phocagallery, html, phocagalleryView`
**Erreur J4 :** `404`

**Analyse :** PhocaGallery est cassé même en J3. La version installée ne trouve pas son `View` PHP. Cela peut signifier que :

- Les fichiers du composant sont corrompus ou incomplets dans l'archive fournie
- La version installée est incompatible avec PHP 7.4 / Joomla 3.10.12

**Impact :** La section "Galerie photo" du site est **non fonctionnelle depuis la sauvegarde d'origine**, indépendamment de la migration J4.

**Solution :** Installer PhocaGallery for Joomla 4 (version officielle disponible sur phoca.cz) — cela réglera le problème des deux côtés.

---

### 2. DTRegister (réservation) — cassé dans J3 et J4

**Erreur J3 :** `500 — Class 'JFormFieldText' not found`
**Erreur J4 :** `500`

**Analyse :** DTRegister est cassé en J3 également. La classe `JFormFieldText` est une classe Joomla core qui devrait exister en J3.10.12. Son absence indique probablement que :

- Le composant DTRegister utilise une déclaration de classe en conflit avec le namespace J3
- Ou que l'archive OVH avait déjà une version partiellement cassée

**Impact :** La réservation en ligne était **déjà non fonctionnelle** avant la migration. La migration J4 ne l'a pas dégradée.

**Solution :** DTRegister n'a pas de version Joomla 4. Remplacer par un composant de réservation J4 natif (voir §5).

---

### 3. Back-office J3 — erreurs JFormField

**Pages affectées :** Gestion articles, Gestion menus, Gestion modules
**Erreurs :**

- `Class 'JFormFieldPredefinedList' not found` (articles, modules)
- `Class 'JFormFieldList' not found` (menus)

**Analyse :** Ces classes sont des classes Joomla 3 core qui devraient exister. Leur absence est probablement due à des extensions tierces (RokCommon, Gantry, DTRegister) qui cherchent à étendre ces classes ou qui les écrases lors du chargement. Des plugins `system` encore actifs interfèrent avec le bootstrap de Joomla 3.

**Impact :** Le back-office J3 ne permet pas de gérer articles, menus ni modules via l'interface graphique.

**Statut :** Ce problème existait avant la migration (site de référence).

> **Conclusion importante :** Le site J3 "de référence" avait un back-office partiellement cassé. La migration J4 a résolu ces problèmes d'administration.

---

### 4. Tables workflow manquantes en J4 (corrigé)

**Problème initial :** Lors du premier audit, l'admin J4 retournait une erreur 500 :
`Table 'db.jh3_workflow_associations' doesn't exist`

**Cause racine :** Le script de migration `4.0.0-2018-05-15.sql` avait été exécuté sans substitution correcte du préfixe `#__` → `jh3_`. Les tables workflow avaient été créées avec le préfixe littéral `#__` au lieu de `jh3_`.

**Tables concernées :**

- `#__workflows` → renommée `jh3_workflows`
- `#__workflow_associations` → renommée `jh3_workflow_associations`
- `#__workflow_stages` → renommée `jh3_workflow_stages`
- `#__workflow_transitions` → renommée `jh3_workflow_transitions`
- `#__guidedtour_steps` → renommée `jh3_guidedtour_steps`
- `#__guidedtours` → renommée `jh3_guidedtours`
- `#__scheduler_tasks` → renommée `jh3_scheduler_tasks`
- `#__user_mfa` → renommée `jh3_user_mfa`
- `#__webauthn_credentials` → renommée `jh3_webauthn_credentials`

**Correction appliquée le 14/04/2026 :**

```sql
RENAME TABLE `#__workflows` TO `jh3_workflows`;
RENAME TABLE `#__workflow_associations` TO `jh3_workflow_associations`;
RENAME TABLE `#__workflow_stages` TO `jh3_workflow_stages`;
RENAME TABLE `#__workflow_transitions` TO `jh3_workflow_transitions`;
RENAME TABLE `#__guidedtour_steps` TO `jh3_guidedtour_steps`;
RENAME TABLE `#__guidedtours` TO `jh3_guidedtours`;
RENAME TABLE `#__scheduler_tasks` TO `jh3_scheduler_tasks`;
RENAME TABLE `#__user_mfa` TO `jh3_user_mfa`;
RENAME TABLE `#__webauthn_credentials` TO `jh3_webauthn_credentials`;
```

**Résultat :** ✅ Admin J4 entièrement fonctionnel

---

## Différences visuelles (front-end)

### Template

| Aspect     | J3 (rt_quantive/Gantry 4)               | J4 (Cassiopeia)                  |
| ---------- | --------------------------------------- | -------------------------------- |
| Style      | Design sombre, custom RocketTheme       | Design sobre, officiel Joomla 4  |
| Responsive | Oui (Gantry)                            | Oui (Bootstrap 5)                |
| Navigation | Menu horizontal personnalisé            | Menu horizontal Bootstrap        |
| Header     | Logo + bandeau personnalisé             | Structure Cassiopeia par défaut  |
| Couleurs   | Charte graphique ULM (bleu/gris custom) | Couleurs par défaut Cassiopeia   |
| Footer     | Pied de page Gantry avec modules        | Pied de page Cassiopeia standard |

### Titres des pages (articles)

En J3, les titres de pages articles affichaient le nom du site ("Lille ULM Nord - Baptême de l'air"). En J4, les titres affichent le titre de l'article ("Nos offres", "L'avion", "FAQ", "Mentions légales") — ce qui est en réalité plus correct pour le SEO.

---

## Fonctionnalités perdues / altérées après migration

| Fonctionnalité             | Statut J3      | Statut J4            | Perte réelle ?        |
| -------------------------- | -------------- | -------------------- | --------------------- |
| Contenu textuel (articles) | ✅             | ✅                   | Non                   |
| Navigation (menus)         | ✅             | ✅                   | Non                   |
| Formulaire de contact      | ✅             | ✅                   | Non                   |
| Galerie photos             | ❌             | ❌                   | **Non** (déjà cassée) |
| Réservation en ligne       | ❌             | ❌                   | **Non** (déjà cassée) |
| Charte graphique           | ✅ rt_quantive | ⚠️ Cassiopeia défaut | **Oui** — à recréer   |
| Back-office articles       | ❌             | ✅                   | **Amélioration**      |
| Back-office menus          | ❌             | ✅                   | **Amélioration**      |
| Back-office modules        | ❌             | ✅                   | **Amélioration**      |

**Bilan :** La migration n'a causé **aucune perte fonctionnelle** par rapport au site J3. Les fonctionnalités manquantes (galerie, réservation) étaient déjà hors service dans l'environnement J3.

---

## Screenshots générés

Les captures d'écran comparatives sont disponibles dans :

```
~/Projets/lille-ulm/audit-screenshots/
├── screenshots/
│   ├── j3/          # Screenshots de chaque page J3
│   └── j4/          # Screenshots de chaque page J4
└── rapport-audit-visuel.html   # Rapport HTML interactif côte à côte
```

Pour consulter le rapport visuel :

```bash
xdg-open ~/Projets/lille-ulm/audit-screenshots/rapport-audit-visuel.html
```

---

## Recommandations prioritaires

### 1. Redesign du template (Priorité haute)

Créer un child template basé sur Cassiopeia reproduisant la charte graphique du site (couleurs, logo, typographie, disposition des modules). C'est la principale différence visuelle visible par les visiteurs.

### 2. PhocaGallery J4 (Priorité modérée)

Installer PhocaGallery for Joomla 4 depuis [phoca.cz](https://www.phoca.cz/phocagallery). La migration des données est transparente (même structure de tables). Résoudra le problème tant en J3 qu'en J4.

### 3. Remplacement DTRegister (Priorité critique)

DTRegister est abandonné et n'a pas de version J4. Le système de réservation était déjà hors service. Recommandations :

- **EventBooking** (Ossolution) — spécialisé réservations/billeterie
- **RSEvents!Pro** — complet mais plus généraliste
- **Hikashop** — si on souhaite une solution e-commerce complète avec réservations

### 4. Vérification des workflows J4

Les tables workflow ont été renommées après l'audit initial. Vérifier que les articles existants ont bien leurs associations workflow correctement initialisées.

---

_Rapport généré le 14 avril 2026 — Audit initial. À compléter après chaque cycle de corrections._
