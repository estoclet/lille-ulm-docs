# Orchestration Claude, Codex et Copilot

## Claude

A utiliser prioritairement pour :

- cadrer un lot ;
- decomposer une grosse question ;
- construire ou relire une spec ;
- arbitrer entre 2 options ;
- consolider un resultat.

## Codex

A utiliser prioritairement pour :

- coder un module ou une fonctionnalite ;
- produire des diffs ;
- migrer des donnees ;
- lancer tests et audits ;
- corriger un bug borne.

## Copilot

A utiliser prioritairement pour :

- petits ajustements rapides ;
- navigation dans le code ;
- documentation courte ;
- finitions ;
- revue locale rapide pendant l'edition.

## Regle de delegation

Ne jamais lancer un agent sans :

1. objectif ;
2. fichiers a lire ;
3. sortie attendue ;
4. contrainte de perimetre ;
5. definition de fin.

Si le travail correspond a une issue GitHub, ajouter aussi :

6. numero ou lien d'issue ;
7. statut actuel ;
8. labels de lot et de priorite.

Et ne jamais lui demander de "completer ce qui manque" sans dire :

- ce qui est certain ;
- ce qui est a deduire ;
- ce qui doit rester ouvert.

## Paquet de contexte maximum

Un agent ne doit lire que :

- 1 README local ;
- 1 spec ;
- 1 template ;
- quelques fichiers cibles.

Pas un repository entier.

## Regles anti-derives

Un agent ne doit pas :

- fusionner plusieurs sujets dans un gros document ;
- creer une nouvelle source de verite concurrente ;
- recopier de longs passages deja presents ailleurs ;
- transformer une note de cadrage en specification finale sans validation.

## Cycle recommande

1. Claude prepare le lot
2. Codex implemente
3. Copilot aide aux petits ajustements
4. Claude ou humain relit et arbitre

## Quand splitter

Si une demande melange :

- commerce
- SEO
- UX editoriale
- architecture Drupal

alors il faut 2 a 4 taches, pas une seule.

## Format d'une bonne demande IA

- contexte court ;
- perimetre ferme ;
- livrable mesurable ;
- liste de fichiers ;
- interdits explicites.
- issue GitHub liee si le sujet est deja suivi.

## Format de sortie attendu

Une bonne sortie d'agent doit separer :

1. faits confirms ;
2. propositions ;
3. questions ouvertes ;
4. fichiers modifies.

Si une issue existe deja, la sortie doit aussi permettre de mettre a jour :

5. le statut ;
6. le commentaire de synthese ;
7. les liens vers les fichiers produits.

## Regle de split documentaire

Si une sortie propose :

- plus de 2 decisions majeures ;
- plus de 2 pages ;
- plus de 2 domaines ;

alors il faut plusieurs livrables, pas un seul fichier.
