# Feature brief - Parcours offres et vente

## Issue GitHub liee

- `#3 Specifier la page Nos offres`

## But

Definir un parcours clair qui presente les offres, rassure, puis emmene vers l'achat d'une prestation pour soi ou a offrir.

## Valeur metier

- mieux convertir ;
- rendre l'offre lisible ;
- sortir du tunnel legacy expose ;
- preparer un back-office simple pour le gestionnaire.

## Utilisateur cible

- acheteur d'un bapteme ou d'un bon cadeau ;
- proche offrant une experience ;
- prospect voulant comprendre prix, format et suite du parcours.

## Perimetre in

- presentation des offres principales ;
- prix et durees ;
- rassurance ;
- CTA vers achat ou demande ;
- possibilite d'acheter une prestation a offrir ;
- reservation d'un creneau date/heure parmi des disponibilites ouvertes par le gestionnaire ;
- articulation avec paiements et confirmations ;
- preuve d'achat facilement presentable le jour de la prestation ;
- lien vers telephone / contact si besoin.

## Perimetre out

- reconduction d'un agenda public legacy type `JEvents` ;
- reprise technique de `DT Register` ;
- logique CRM avancee ;
- promotions complexes au premier lot.

## Regles de gestion

- une offre doit etre comprenable sans jargon ;
- le CTA principal doit etre evident ;
- le parcours doit accepter l'achat en ligne sans exposer de page technique legacy ;
- le parcours doit rendre explicite la difference entre achat pour soi et achat a offrir ;
- pour une offre offrable, le premier point de capture retenu est l'ajout au panier, au niveau de la ligne de commande ;
- pour une offre reservable, le parcours cible doit permettre la selection d'un creneau parmi les disponibilites ouvertes par le gestionnaire ;
- le creneau choisi est rattache a la ligne de commande ;
- la reservation devient definitive a la commande placee ;
- un creneau reserve doit devenir indisponible pour une autre commande ;
- le gestionnaire doit pouvoir reporter une reservation si les conditions, notamment meteo, l'imposent ;
- le parcours doit produire un justificatif d'achat simple a presenter et difficile a falsifier ;
- une offre a offrir doit rester rattachee a une vraie commande et a un identifiant unique ;
- le justificatif doit pouvoir etre controle rapidement cote pilote via une verification serveur ;
- l'identifiant de justificatif et ses statuts restent hors saisie acheteur et sous controle serveur / back-office ;
- le gestionnaire doit pouvoir mettre a jour textes, prix et blocs de rassurance.

## UI attendue

- page de type landing commerciale ;
- cartes ou blocs d'offres comparables ;
- zone de rassurance ;
- FAQ courte ;
- bloc contact humain visible.

## Donnees / contenus

- intitulés d'offres ;
- prix ;
- durees ;
- eligibility cadeau / offre a offrir ;
- eligibility reservation / offre reservable ;
- disponibilites / creneaux selon les offres concernees ;
- destinataire / beneficiaire si achat cadeau ;
- conditions simples ;
- messages de reassurance ;
- mode de justification / controle le jour J ;
- informations de contact.

## Definition of done

- la structure cible du parcours est claire ;
- les offres prioritaires sont identifiees ;
- le type de CTA par offre est defini ;
- les blocs editoriaux utiles a la conversion sont nommes ;
- la page spec `Nos offres` peut servir de base de build.

## Fichiers de contexte a lire

- `00-initialisation-projet.md`
- `decisions/ADR-001-commerce-sobre.md`
- `decisions/ADR-002-legacy-dtregister-jevents.md`
- `pages/page-spec-nos-offres.md`
