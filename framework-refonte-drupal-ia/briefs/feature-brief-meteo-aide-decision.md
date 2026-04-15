# Feature brief - Meteo : aide a la decision de report

## Statut

cadrage termine - ADR-017 produit

## Issue liee

#21

## Faits confirmes

- ADR-016 positionne explicitement la meteo comme aide a la decision de report, non comme automatisation.
- La fonctionnalite n'a de valeur operationnelle que si des reservations datees existent deja en base.
- Le gestionnaire est le seul decisionnaire : le site n'annule ni ne reporte jamais seul.
- Les baptemes et cours ULM sont en exterieur dans les Hauts-de-France : meteo locale critique (vent, pluie, visibilite, plafond nuageux).
- Localisation cible : secteur Bondues / Lille (coordonnees GPS fixes, pas de saisie libre).

## Perimetre retenu au premier lot

Une seule surface : **un indicateur meteo par reservation a venir**, visible dans la vue gestionnaire des reservations.

Ce que le gestionnaire voit, par reservation datee :

- date et heure de la reservation ;
- conditions prevues a J-1 et le jour J : vent (km/h, direction), precipitations (mm), visibilite (km), plafond nuageux (ft ou m) ;
- un indicateur de lisibilite simple : favorable / a surveiller / defavorable ;
- un lien vers la source externe pour approfondir.

Ce que le gestionnaire fait :

- il consulte l'indicateur ;
- il decide de maintenir ou de reporter via l'action de report existante (22b) ;
- il contacte l'acheteur si necessaire (hors perimetre de ce lot).

## Ce qui n'est pas dans ce lot

- notification automatique ou push a l'acheteur ;
- annulation automatique ;
- integration temps-reel ou webhook meteo ;
- ecran metier dedie au parametrage des seuils par le gestionnaire ;
- affichage cote client public.

## Donnees minimales necessaires

| Variable | Usage | Source de verite |
|---|---|---|
| Vent moyen | aide a la decision de maintien / report | ADR-017 |
| Rafales | aide a la decision de maintien / report | ADR-017 |
| Precipitations | aide a la decision de maintien / report | ADR-017 |
| Visibilite | aide a la decision de maintien / report | ADR-017 |
| Plafond nuageux / proxy `cloud_cover_low` | aide a la decision de maintien / report | ADR-017 |

Les seuils exacts, le proxy plafond nuageux et la doctrine de cache sont portes par
`decisions/ADR-017-api-meteo-et-doctrine-integration.md`.

## Doctrine d'integration retenue

`decisions/ADR-017-api-meteo-et-doctrine-integration.md` fixe :

- **Open-Meteo** comme API par defaut ;
- **AROME Meteo-France** comme alternative configurable ;
- un cache de 15 minutes ;
- une localisation fixe Bondues / Lille ;
- une doctrine stricte de non-automatisation du report.

## Positionnement roadmap

- **Ne bloque pas 22a ni 22b** : independant du modele de donnees reservation.
- **Depend de 22b** : l'indicateur meteo s'affiche dans la vue gestionnaire des reservations (livrable de 22b).
- **Lot recommande** : apres validation de 22b, en parallele ou juste apres le lot qualite.
- **Priorite** : utile mais non critique au lancement ; peut etre reporte sans impacter le MVP.

## Questions ouvertes (decisions a prendre)

1. Validation en recette des seuils et du proxy plafond nuageux avec le gestionnaire.
2. Niveau de detail exact du lien vers la source externe dans la vue gestionnaire.

## ADR produit

`decisions/ADR-017-api-meteo-et-doctrine-integration.md` couvre :

- API retenue (Open-Meteo par defaut, AROME configurable) ;
- modele de donnees minimal (cache 15 min) ;
- emplacement : vue gestionnaire des reservations (livrable de 22b) ;
- doctrine de non-automatisation (conforme ADR-016).
