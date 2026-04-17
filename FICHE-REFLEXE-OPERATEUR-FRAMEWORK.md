# Fiche reflexe operateur - utiliser au mieux le framework IA

## But

Cette fiche aide l'operateur humain a tirer le meilleur du framework
`framework-refonte-drupal-ia/` pour faire avancer la refonte Lille ULM vite,
sans perdre le cadre ni melanger documentation, arbitrage et implementation.

## Point d'entree par defaut

Demarrer une seance dans :

`~/Projets/lille-ulm/lille-ulm-docs/`

Pourquoi :

- le `CLAUDE.md` racine cadre la session ;
- le framework vit dans `framework-refonte-drupal-ia/` ;
- les task packs actifs sont a la racine ;
- les issues projet vivent dans le repo docs ;
- le repo applicatif est accessible juste a cote via `../lille-ulm-drupal-app/`.

## Regle simple de pilotage

1. **Cadrer dans `lille-ulm-docs/`**
2. **Coder dans `lille-ulm-drupal-app/`**
3. **Revenir dans `lille-ulm-docs/` pour consolider et suivre**

Ne pas commencer une implementation dans le repo applicatif sans issue claire et
sans task pack pret.

## Workflow reflexe recommande

### 1. Ouvrir la bonne base

Depuis `lille-ulm-docs/`, relire au minimum :

- `README.md`
- `framework-refonte-drupal-ia/README.md`
- `framework-refonte-drupal-ia/00-initialisation-projet.md`
- `framework-refonte-drupal-ia/08-plan-de-lots.md`

Si le sujet est deja avance, lire aussi le ou les `task-pack-*.md` concernes.

### 2. Partir d'un vrai sujet suivi

Toujours partir de l'un des points suivants :

- une issue GitHub ;
- un lot du framework ;
- un besoin brut a transformer en issue courte.

Le backlog officiel reste dans `lille-ulm-docs`.

## 3. Choisir le bon niveau de travail

- **besoin flou / arbitrage / decoupage** -> rester dans `lille-ulm-docs/`
- **spec ou cadrage de page / fonctionnalite** -> rester dans `lille-ulm-docs/`
- **implementation Drupal reelle** -> basculer ensuite dans `../lille-ulm-drupal-app/`
- **retour d'audit ou consolidation** -> revenir dans `lille-ulm-docs/`

## 4. Produire un task pack borne

Un bon pack doit contenir :

- une issue liee ;
- une ou plusieurs sources de verite ;
- une liste courte de fichiers a lire ;
- des fichiers cibles explicites ;
- une verification attendue ;
- une definition de fin observable.

Regle :

- si le pack demande plusieurs sujets a la fois, il faut le splitter ;
- si les fichiers cibles ne sont pas connus, la tache n'est pas assez cadree.

## 5. Valider avant de deleguer

Depuis `lille-ulm-docs/` :

```bash
python3 framework-refonte-drupal-ia/orchestrateur.py validate task-pack-XX.md
python3 framework-refonte-drupal-ia/orchestrateur.py render task-pack-XX.md
```

Ne deleguer qu'apres lecture du handoff.

## 6. Deleguer avec le bon niveau de risque

Pour une premiere passe :

```bash
python3 framework-refonte-drupal-ia/orchestrateur.py dispatch task-pack-XX.md --dry-run
```

Pour un run live :

```bash
python3 framework-refonte-drupal-ia/orchestrateur.py dispatch task-pack-XX.md
```

Le `dispatch` live est maintenant isole :

- il travaille dans un workspace jetable ;
- il ne modifie plus directement le depot principal ;
- il stocke ses changements proposes dans
  `framework-refonte-drupal-ia/.orchestrator-state/runs/<run-id>/changes/`.

## 7. Relire comme un operateur, pas comme un simple executeur

Apres un run :

1. verifier le statut du pack ;
2. relire `stdout.txt` et `metadata.json` ;
3. regarder les fichiers proposes dans `changes/` ;
4. decider si le resultat est :
   - consolidable ;
   - a recadrer ;
   - a bloquer.

Si la sortie n'utilise pas les 5 headings imposes, le run doit etre considere
comme invalide.

## 8. Basculer vers le repo applicatif au bon moment

Le bon moment pour ouvrir une session dans
`~/Projets/lille-ulm/lille-ulm-drupal-app/` est :

- quand l'arbitrage est deja pris ;
- quand les fichiers cibles de code sont identifies ;
- quand le livrable attendu est testable ;
- quand le task pack est deja pret ou quasi pret.

En implementation Drupal, garder `lille-ulm-docs/` ouvert a cote pour ne pas
perdre les sources de verite.

## Seance type la plus efficace

1. session Claude Code dans `lille-ulm-docs/`
2. lecture du contexte minimal
3. issue courte ou verification de l'issue existante
4. creation / mise a jour du task pack
5. `validate` puis `render`
6. si le sujet est du code, ouverture d'une session separee dans `lille-ulm-drupal-app/`
7. implementation bornee
8. retour dans `lille-ulm-docs/` pour cloture, sync issue et consolidation

## Heuristiques utiles pour Lille ULM

- partir des pages et parcours qui convertissent : `Nos offres`, `Contact`,
  `Nous trouver`, puis les parcours de reservation ;
- ne jamais chercher a "refaire Joomla" ;
- preferer une reprise selective a une migration exhaustive ;
- traiter `DT Register` et `JEvents` comme des sujets legacy a cadrer, pas comme
  des briques a recopier ;
- penser DDEV et back-office gestionnaire simple des qu'une tache touche le code.

## Erreurs a eviter

- lancer une seance depuis `lille-ulm-drupal-app/` pour cadrer un sujet encore flou ;
- envoyer a l'agent trop de fichiers "au cas ou" ;
- melanger cadrage business, architecture Drupal et migration dans un seul pack ;
- oublier de declarer les fichiers cibles ;
- modifier la doc cadre apres implementation sans passer par une vraie decision ;
- traiter une issue comme finie sans mise a jour du suivi dans `lille-ulm-docs`.

## Commandes reflexes

```bash
# depuis lille-ulm-docs/
python3 framework-refonte-drupal-ia/orchestrateur.py validate task-pack-XX.md
python3 framework-refonte-drupal-ia/orchestrateur.py render task-pack-XX.md
python3 framework-refonte-drupal-ia/orchestrateur.py dispatch task-pack-XX.md --dry-run
python3 framework-refonte-drupal-ia/orchestrateur.py sync-issue task-pack-XX.md --dry-run
```

## Resume ultra-court

- **on pense dans `lille-ulm-docs/`**
- **on cadre avec le framework**
- **on code ensuite dans `lille-ulm-drupal-app/`**
- **on consolide et on suit a nouveau dans `lille-ulm-docs/`**
