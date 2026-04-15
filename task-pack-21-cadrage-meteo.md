# Agent task pack - Cadrage fonctionnalite meteo

## Statut
done

## Agent cible

claude

## Type de travail

cadrage

## Issue GitHub liee

#21

## Source de verite

- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/decisions/ADR-015-reservation-de-creneaux.md

## Objectif

Cadrer la fonctionnalite meteo pour qu'elle soit utile au gestionnaire et lisible cote client, sans devenir une application aeronautique autonome.

L'ancrage metier est explicite : la meteo sert a aider le gestionnaire a decider si un creneau reserve doit etre maintenu ou reporte. Ce perimetre est retenu comme seul niveau d'integration au premier lot (ADR-016).

Le cadrage doit produire :

1. une definition du perimetre de valeur concret (ce que la meteo change vraiment pour le gestionnaire) ;
2. une evaluation du niveau de criticite metier (bloquant, utile, nice-to-have) ;
3. les donnees minimales necessaires (API, frequence, granularite geographique) ;
4. le positionnement dans la roadmap par rapport au lot reservation.

## Livrable attendu

Un document de cadrage court (< 120 lignes) separant :

1. faits confirmes : ce que le besoin meteo impose comme contrainte reelle ;
2. propositions : perimetre retenu, donnees minimales, interface gestionnaire minimale ;
3. questions ouvertes : arbitrages non resolus (choix d'API, niveau d'alerte, notification acheteur) ;
4. positionnement roadmap : avant, pendant ou apres le lot reservation (22a/22b).

Si le cadrage conclut a un ADR necessaire, le mentionner explicitement sans le rediger dans ce pack.

## Fichiers a lire

- framework-refonte-drupal-ia/decisions/ADR-016-modele-minimal-reservation-de-creneau.md
- framework-refonte-drupal-ia/decisions/ADR-015-reservation-de-creneaux.md
- framework-refonte-drupal-ia/08-plan-de-lots.md

## Fichiers a ne pas toucher

- framework-refonte-drupal-ia/decisions/
- task-pack-22a-modele-creneau.md
- task-pack-22b-backoffice-creneaux.md

## Contraintes

- ne pas concevoir une application meteo autonome : la meteo est une aide a la decision humaine, pas une automatisation ;
- ne pas proposer d'integration temps-reel ou de notifications push au premier lot ;
- ne pas inventer de contraintes aeronautiques : se limiter au besoin operationnel du gestionnaire Lille ULM ;
- marquer explicitement hypothese, fait observe, decision a prendre ou risque ;
- ne pas creer de nouveau fichier source de verite sans le signaler comme proposition.

## Verification attendue

- le cadrage distingue clairement ce qui est un besoin confirme et ce qui est une hypothese ;
- le perimetre est suffisamment borne pour qu'un pack d'implementation puisse en deriver ;
- le positionnement roadmap est explicite (bloquant avant 22a, parallelisable, ou reportable apres) ;
- aucune decision structurante n'est prise implicitement.

## Definition de fin

Un document de cadrage valide par l'humain, utilisable comme base pour un ADR si necessaire et pour un task pack d'implementation ulterieur. L'issue #21 est mise a jour avec le resultat.

## Sortie courte a produire

1. faits confirmes : besoin metier reel, contraintes connues
2. propositions : perimetre retenu, donnees minimales, interface gestionnaire
3. questions ouvertes : API, niveau d'alerte, notification acheteur, timing roadmap
4. fichiers modifies ou a produire : document de cadrage et/ou ADR si besoin
