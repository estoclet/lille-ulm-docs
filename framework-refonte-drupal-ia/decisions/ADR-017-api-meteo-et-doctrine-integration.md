# ADR-017 - Choix API météo et doctrine d'intégration

## Contexte

L'indicateur météo par réservation (feature-brief-meteo-aide-decision.md) nécessite une
source de données externe. Deux options crédibles existent : Open-Meteo (libre, sans compte)
et l'API AROME de Météo-France (compte requis). Le gestionnaire doit rester le seul
décisionnaire ; le site n'automatise ni annulation ni report (ADR-016).

Issue de suivi : #21

## Décision

**API par défaut : Open-Meteo** — gratuit, sans clé API, open-source, données AROME
haute résolution via WMO, granularité horaire, couverture Hauts-de-France correcte.

**API alternative configurable : API AROME Météo-France** — si le gestionnaire dispose
d'un compte, il peut basculer via une option de configuration back-office (Drupal config).
La bascule ne nécessite pas de redéploiement.

**Seuils retenus** (validés — marqués `fait observé` sauf mention) :

| Variable | Seuil "défavorable" | Statut |
|---|---|---|
| Vent moyen | > 20 km/h | fait observé (abaissé de 25) |
| Rafales | > 35 km/h | fait observé |
| Précipitations | > 0.5 mm/h | fait observé |
| Visibilité | < 5 km | fait observé |
| Plafond nuageux | < 500 m | hypothèse validée gestionnaire |

Proxy plafond nuageux (Open-Meteo ne fournit pas de hauteur exacte) :
`cloud_cover_low > 75 %` → considéré comme indicatif d'un plafond < 500 m.
Ce proxy doit être confirmé en recette par le gestionnaire.

**Localisation fixe** : secteur Bondues / Lille — coordonnées GPS codées en configuration
Drupal, pas de saisie libre par l'utilisateur.

**Cache** : réponse mise en cache 15 minutes (config). Pas de webhook ni de flux temps-réel.

## Pourquoi ce choix

Open-Meteo couvre le besoin sans friction d'inscription. Son modèle de données (AROME WMO)
offre la précision locale requise pour les ULM légers (vent, rafales, précipitations,
couverture nuageuse basse). La configurabilité vers AROME Météo-France préserve la
possibilité d'une montée en précision si le gestionnaire ouvre un compte.

## Alternatives écartées

- **Seule Open-Meteo sans option bascule** : trop rigide si le gestionnaire veut AROME direct.
- **Seule AROME Météo-France** : nécessite un compte et une clé API, bloque le démarrage.
- **Automatisation du report sur seuil** : explicitement exclue — contredit ADR-016.

## Conséquences

- Un module Drupal custom minimal gère l'appel API, le cache (15 min) et le rendu de l'indicateur.
- La config Drupal expose : coordonnées GPS, choix d'API, clé AROME (optionnelle), seuils.
- L'indicateur s'affiche dans la vue gestionnaire des réservations (livrable de 22b).
- Les seuils sont des valeurs de départ ; le gestionnaire les valide avant mise en production.
- Un ADR de révision sera produit si Open-Meteo modifie son modèle de données ou ses conditions.
- Ce lot est indépendant de 22a et 22b côté données, mais dépend de 22b côté surface d'affichage.
