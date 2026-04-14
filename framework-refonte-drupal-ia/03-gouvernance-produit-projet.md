# Gouvernance produit et projet

## Phases

Le projet doit avancer en lots simples :

1. **Cadrage metier**
2. **Architecture cible**
3. **Design system et composants**
4. **Back-office gestionnaire**
5. **Commerce / leads / CRM**
6. **Migration de contenu**
7. **Recette et lancement**

## Artefacts minimum

Chaque lot doit produire :

- un objectif ;
- un perimetre ;
- une definition of done ;
- une liste de risques ;
- un lot de taches IA.

## Backlog operationnel

Le backlog courant ne vit pas dans les documents du framework.

Il vit dans les **GitHub Issues** du repo framework.

Usage attendu :

- une issue = une unite de suivi ;
- un lot = un ensemble d'issues coherentes ;
- une issue peut pointer vers un brief, une page spec, un ADR ou un task pack ;
- les documents de framework restent les sources de cadrage, pas des listes de tickets vivantes.

## Workflow de statut

Workflow minimal impose :

1. `todo`
2. `in-progress`
3. `blocked`
4. issue fermee

Regles :

- on evite plusieurs labels de statut en meme temps ;
- fermer une issue vaut `done` ;
- un blocage important doit etre documente dans le corps de l'issue ;
- le label `client` ne s'applique qu'aux sujets montrables tels quels.

## Sources de verite

Le cadre doit toujours distinguer :

1. la vision ;
2. la decision ;
3. la spec ;
4. l'execution.

Regle :

- une decision structurante vit dans un ADR ;
- une fonctionnalite vit dans un feature brief ;
- une page vit dans une page spec ;
- une tache agent vit dans un task pack.

Un meme fait critique ne doit pas etre entretenu manuellement dans plusieurs fichiers.

## Definition of Ready

Une fonctionnalite n'entre en build que si elle a :

1. un besoin metier clair ;
2. un ecran ou parcours cible ;
3. des regles de gestion ;
4. un proprietaire de decision ;
5. un impact editorial ou technique identifie.

## Definition of Done

Une fonctionnalite est terminee si :

1. elle est livree ;
2. le gestionnaire sait l'utiliser ;
3. le contenu de demonstration est comprenable ;
4. la documentation courte existe ;
5. les impacts SEO / accessibilite / RGPD ont ete regardes.

## Rituels

### Hebdomadaire

- arbitrage produit ;
- blocages ;
- decisions a prendre.
- mise a jour des issues clientes visibles ;

### Par lot

- revue du besoin ;
- revue UX ;
- revue technique ;
- revue gestionnaire.

### Par sprint IA

- contexte transmis ;
- travail d'agent ;
- revue humaine ;
- consolidation courte.

## Registre de decisions

Toute decision structurante doit devenir un ADR court :

- Drupal Commerce ou non ;
- Layout Builder seul ou non ;
- CRM interne ou externe ;
- strategie analytics ;
- strategie consentement.

## Regle anti-hallucination

Un agent ne peut pas presenter comme fait :

- une hypothese ;
- une preference ;
- une deduction non verifiee ;
- une decision non encore tranchee.

Ces cas doivent etre etiquetes explicitement :

- `fait observe`
- `hypothese`
- `decision a prendre`
- `risque`

## Regle de clarification

Si une question impacte fortement le build, elle doit etre tranchee avant d'etre codee.

Exemples :

- paiement en ligne requis ou non ;
- bon cadeau nominatif ou non ;
- agenda public ou agenda interne ;
- CRM dans Drupal ou via SaaS externe.

## Regle d'edition documentaire

Lorsqu'un document est mis a jour :

1. corriger la source de verite d'abord ;
2. mettre a jour les renvois ensuite ;
3. ne pas etendre un fichier si un split est plus sain ;
4. preferer une correction precise a une reecriture massive.

## Regle de liaison issue -> document

Quand un sujet merite un document :

- l'issue pointe vers le document source ;
- le document rappelle l'issue de suivi si elle est utile ;
- on evite de recopier l'integralite de l'issue dans le document.
