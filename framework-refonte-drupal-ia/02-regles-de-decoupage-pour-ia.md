# Regles de decoupage pour IA

## Objectif

Claude, Codex et Copilot travaillent mieux si chaque fichier est :

- court ;
- stable ;
- monothematique ;
- facilement resumable.

## Regles de taille

- cible ideale : **120 lignes max**
- seuil de vigilance : **140 lignes**
- seuil de split obligatoire : **180 lignes**

## Regles de structure

Un dossier de travail IA ne doit pas contenir plus de :

- **1 index**
- **1 doc de contexte**
- **1 ou 2 specs**
- **1 ou 2 templates**

Si un sujet a besoin de plus, il faut le decouper par :

- domaine ;
- page ;
- lot ;
- decision.

## Regles de nommage

Utiliser des noms :

- explicites ;
- courts ;
- ordonnes numeriquement si la lecture a un sens ;
- sans ambiguites metier.

Exemples :

- `page-nos-offres.md`
- `feature-bons-cadeaux.md`
- `adr-003-commerce-ou-non.md`

## Task pack IA

Chaque tache donnee a un agent doit tenir dans un paquet de contexte limite :

1. objectif ;
2. perimetre ;
3. fichiers a lire ;
4. livrable attendu ;
5. contraintes.

L'agent ne doit pas recevoir "lis tout le dossier".

## Regle anti-bruit

Ne pas dupliquer la meme verite dans 6 fichiers.

Une verite source doit vivre :

- soit dans une spec ;
- soit dans une decision ;
- soit dans un registre.

Les autres fichiers doivent y renvoyer.

## Regle de split

Si un fichier melange :

- produit
- UX
- technique
- planning

alors il doit etre scinde.

## Regle d'iteration

Chaque iteration doit modifier de preference :

- un petit nombre de fichiers ;
- sur un seul sujet ;
- avec un impact facile a relire.

## Format conseille

Pour les IA, privilegier :

- markdown simple ;
- tableaux courts ;
- listes numerotees ;
- sections stables.

Eviter :

- prose longue ;
- captures noyees dans le texte ;
- annexes geantes ;
- comptes-rendus fleuves.
