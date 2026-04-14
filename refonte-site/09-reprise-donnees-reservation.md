# Reprise des donnees de reservation

## Pourquoi ce sujet est critique

La reservation n'est pas seulement un lien de menu :

- 4004 inscriptions historiques dans `jh3_dtregister_user`
- activite observee de 2010-07-01 a 2024-06-15
- 13 `eventId` distincts utilises
- 250 evenements `JEvents`

La refonte doit donc decider explicitement :

- reprise applicative ;
- reprise partielle ;
- archivage legal / commercial ;
- ou abandon sans reprise.

## Indicateurs observes

- premiere inscription : `2010-07-01 07:30:58`
- derniere inscription : `2024-06-15 20:52:15`
- inscriptions totales : `4004`
- lignes marquees `payment_verified=1` : `4003`
- lignes annulees `cancel=1` : `0`

## Distribution des inscriptions par `eventId`

Top releve :

- `eventId=1` : 1109 inscriptions
- `eventId=4` : 696
- `eventId=2` : 620
- `eventId=3` : 342
- `eventId=10` : 335
- `eventId=18` : 303
- `eventId=17` : 171
- `eventId=15` : 167
- `eventId=11` : 117
- `eventId=6` : 115
- `eventId=7` : 19
- `eventId=12` : 9
- `eventId=0` : 1

Lecture :

- plusieurs offres historiques ne sont plus forcement exposees publiquement mais ont porte une vraie activite ;
- les `eventId` 10, 18, 17, 15, 11, 12 correspondent aux CTA releves sur la page "Nos offres" actuelle ;
- les `eventId` 1 a 4 semblent correspondre a des offres plus anciennes ou precedentes versions du catalogue.

## Modes de paiement observes

- `Paypal` : 2269
- `At_door` : 629
- `NULL` : 1103
- `Free` : 3

Lecture :

- PayPal a ete fortement utilise ;
- le site a gere au moins un mode de paiement sur place ;
- les valeurs `NULL` imposent de verifier la qualite de la donnee avant tout reporting ou migration.

## Elements fonctionnels lies a la reservation

Le parcours visible actuel indique :

1. achat du bon en ligne ;
2. paiement securise ;
3. reception d'un code de confirmation ;
4. prise de rendez-vous ensuite par telephone.

Cela ressemble davantage a une vente de bon / coupon qu'a une reservation temps reel de type agenda public.

## Hypotheses de travail

### Hypothese 1 : historique commercial uniquement

La base `DT Register` sert surtout d'historique d'achats et d'inscriptions, sans necessite de reprise dans le futur site.

Action cible :

- export CSV / archive RGPD ;
- pas de migration applicative.

### Hypothese 2 : historique + consultation interne

L'historique doit rester consultable en back-office.

Action cible :

- extraire les donnees vers un outil d'archive ou un mini back-office dedie ;
- ne pas reconduire `DT Register`.

### Hypothese 3 : reprise metier partielle

Certains clients, bons ou flux doivent continuer a vivre dans le nouveau systeme.

Action cible :

- cartographier les entites :
  - offre
  - commande
  - client
  - paiement
  - code de confirmation
  - prise de rendez-vous

## Recommandation immediate

Avant toute decision technique sur la refonte, il faut organiser un atelier de cadrage specifique "reservation / paiement / historique clients" avec ces questions :

- Faut-il vendre en ligne dans la cible ?
- Faut-il gerer des disponibilites ?
- Faut-il conserver l'historique en consultation ?
- Existe-t-il des obligations comptables ou SAV liees aux bons vendus ?
- Quel canal de paiement doit exister dans la cible ?
