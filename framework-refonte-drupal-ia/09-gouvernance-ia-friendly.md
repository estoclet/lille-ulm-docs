# Gouvernance IA-friendly

## Finalite

Ce document fixe les regles qui gardent le framework :

- lisible par des IA ;
- stable dans le temps ;
- resistant a l'hallucination ;
- resistant au grossissement progressif.

## Regle 1 - Une verite = une maison

Chaque information critique doit avoir un **fichier maitre**.

Exemples :

- une decision structurante -> ADR ;
- une fonctionnalite -> feature brief ;
- une page -> page spec ;
- une tache d'agent -> task pack.

Les autres fichiers doivent resumer ou pointer, pas concurrencer.

## Regle 2 - Toute hypothese doit etre marquee

Les formulations suivantes doivent etre explicites :

- `fait observe`
- `hypothese`
- `decision a prendre`
- `a confirmer`

Une IA ne doit jamais transformer une probabilite en verite.

## Regle 3 - Budget de taille non negociable

- jusqu'a 140 lignes : acceptable ;
- entre 141 et 180 : a surveiller ;
- au dela de 180 : split obligatoire.

Le split doit suivre un axe simple :

- page ;
- domaine ;
- decision ;
- lot.

## Regle 4 - Pas de document fourre-tout

Un fichier ne doit pas melanger durablement :

- vision ;
- decision ;
- spec ;
- plan d'execution.

Si c'est le cas, il faut scinder.

## Regle 5 - Petite modification d'abord

Quand une info change :

1. modifier le fichier source ;
2. ajuster les renvois directs ;
3. ne pas rebalayer tout le framework sans raison.

## Regle 6 - Preuve minimale

Toute affirmation importante doit pouvoir reposer sur au moins un de ces appuis :

- observation documentee ;
- audit ;
- decision validee ;
- source externe fiable ;
- code ou configuration cible.

Si ce support n'existe pas, il faut ecrire `hypothese`.

## Regle 7 - Prompts bornes

Tout prompt agent doit contenir :

- le but ;
- le perimetre ;
- les fichiers a lire ;
- les fichiers a ne pas dupliquer ;
- le format de sortie.

## Regle 8 - Consolidation courte

Apres travail d'agent :

- consolider en peu de fichiers ;
- supprimer les repetitions ;
- garder seulement la version source.

## Regle 9 - Interdits explicites

Sont interdits dans ce framework :

- les comptes-rendus fleuves ;
- les journaux melant tout ;
- les annexes geantes recopiees ;
- les "master docs" tentant de tout centraliser ;
- les reformulations multiples de la meme decision.

## Checklist de revue

Avant de considerer une mise a jour saine, verifier :

1. le bon fichier source a-t-il ete modifie ?
2. l'information est-elle factuelle ou hypothetique ?
3. y a-t-il duplication inutile ?
4. un fichier depasse-t-il son budget ?
5. un split serait-il plus propre ?
