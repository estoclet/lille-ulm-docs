# Feature brief - Meteo : aide a la decision de report

## Statut

cadrage termine - ADR a produire avant implementation

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
- parametrage des seuils par le gestionnaire (seuils fixes en premiere version) ;
- affichage cote client public.

## Donnees minimales necessaires

| Variable | Seuil indicatif "defavorable" | Source |
|---|---|---|
| Vent moyen | > 25 km/h | fait observe : contrainte ULM legere |
| Rafales | > 35 km/h | fait observe |
| Precipitations | > 0.5 mm/h | fait observe |
| Visibilite | < 5 km | fait observe |
| Plafond nuageux | < 300 m | hypothese - a confirmer avec le gestionnaire |

Les seuils sont des valeurs de depart. Ils doivent etre valides par le gestionnaire avant mise en production.

## API retenue (proposition)

**Open-Meteo** (hypothese - a confirmer dans un ADR) :

- gratuit, sans cle API, open-source ;
- donnees AROME (modele Meteo-France haute resolution) disponibles ;
- granularite horaire, precision locale correcte pour le secteur Lille ;
- variables disponibles : vent, precipitations, visibilite, couverture nuageuse.

Alternative a evaluer : API Meteo-France officielle (AROME direct, necessite inscription).

## Positionnement roadmap

- **Ne bloque pas 22a ni 22b** : independant du modele de donnees reservation.
- **Depend de 22b** : l'indicateur meteo s'affiche dans la vue gestionnaire des reservations (livrable de 22b).
- **Lot recommande** : apres validation de 22b, en parallele ou juste apres le lot qualite.
- **Priorite** : utile mais non critique au lancement ; peut etre reporte sans impacter le MVP.

## Questions ouvertes (decisions a prendre)

1. Validation des seuils meteo avec le gestionnaire (fait observe ou hypothese a confirmer ?).
2. Choix definitif de l'API : Open-Meteo vs Meteo-France (necessite un ADR).
3. Frequence de rafraichissement : a la demande (requete HTTP au chargement de la vue) ou cache court (15 min) ?
4. Notification acheteur en cas de report : email manuel par le gestionnaire ou email automatique ? Hors perimetre premier lot mais a cadrer avant 22b.
5. Faut-il un ecran dedie "suivi meteo des reservations" ou un widget dans la vue existante ?

## ADR a produire avant implementation

Un ADR "Choix API meteo et doctrine d'integration" doit etre produit avant tout code. Il doit couvrir :

- API retenue et raison du choix ;
- modele de donnees minimal (cache, frequence) ;
- emplacement dans le back-office ;
- doctrine de non-automatisation (reaffirmer ADR-016).
