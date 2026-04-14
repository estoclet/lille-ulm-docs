# Rapport d'intervention — Site bapteme-air-lille.fr

**Client :** Lille ULM Nord — Baptême de l'air
**Date d'intervention :** 14 avril 2026
**Intervenant :** Eric STOCLET
**Objet :** Restauration locale du site piraté, analyse forensique et documentation

---

## 1. Contexte

Le site **bapteme-air-lille.fr** (Joomla 3, hébergé chez OVH) affichait une page de defacement depuis une date indéterminée. Les progrès de l'IA m'ont permis une analyse plus précise des 40.747 fichiers que contient votre site. J'avais conservé précieusement :

- Une archive des fichiers du site (répertoire `www/`)
- Un dump de la base de données MySQL (`baptemea111_mysql_db.sql`, 189 Mo)

L'objectif de cette intervention est de :

1. Restaurer le site dans un environnement local (DDEV) pour consultation et analyse
2. Identifier le vecteur et le mécanisme de l'attaque
3. Documenter toutes les actions effectuées
4. Fournir des recommandations pour la remise en production

---

## 2. Environnement de travail mis en place

### 2.1 Outils utilisés

| Outil   | Version | Rôle                                   |
| ------- | ------- | -------------------------------------- |
| DDEV    | 1.25.1  | Environnement de développement local   |
| MariaDB | 11.8    | Serveur de base de données (via DDEV)  |
| PHP     | 7.4     | Interpréteur PHP (compatible Joomla 3) |
| Joomla  | 3.10.12 | CMS (réinstallé, voir §3.2)            |

### 2.2 URL locale du site restauré

```
http://lille-ulm.ddev.site
http://lille-ulm.ddev.site/administrator/
```

Identifiants administrateur restaurés :

- **Login :** `bapteme`
- \*\*Mot de passe : `GcmuV3463VV5qq`

---

## 3. Déroulé de l'intervention

### 3.1 Réinstallation de Joomla 3.10.12

**Action :** Téléchargement de Joomla 3.10.12 (dernière version de la branche 3.x) et remplacement des fichiers core Joomla, en préservant :

- `configuration.php`
- `images/` (photos du site)
- `templates/rt_quantive/` (template personnalisé)
- Plugins, composants et modules tiers

```bash
rsync -a /tmp/joomla3_extract/ /home/eric/Projets/lille-ulm/www/ \
  --exclude=configuration.php \
  --exclude=images/ \
  --exclude=installation/
```

### 3.2 Configuration de la base de données

**Action :** Mise à jour de `configuration.php` pour pointer vers la base de données DDEV :

| Paramètre    | Valeur originale (production)           | Valeur locale (DDEV)               |
| ------------ | --------------------------------------- | ---------------------------------- |
| `$host`      | `baptemea111.mysql.db`                  | `db`                               |
| `$db`        | `baptemea111`                           | `db`                               |
| `$user`      | `baptemea111`                           | `db`                               |
| `$password`  | _(mot de passe OVH)_                    | `db`                               |
| `$log_path`  | `/home/baptemea/www/administrator/logs` | `/var/www/html/administrator/logs` |
| `$tmp_path`  | `/home/baptemea/www/tmp`                | `/var/www/html/tmp`                |
| `$force_ssl` | `2` (HTTPS forcé)                       | `0` (désactivé en local)           |

**Importation du dump :**

```bash
ddev import-db --file=baptemea111_mysql_db.sql
```

---

## 4. Analyse de l'attaque

### 4.1 Symptôme observé

Lors de l'accès à `http://lille-ulm.ddev.site/`, la page affichait :

```
Hacked By Turkic Hackers Rulez (OPJ & M3T4L)
```

avec un fond noir et un ASCII art, au lieu du site légitime.

### 4.2 Identification du vecteur

**Fichier compromis :**

```
templates/rt_quantive/index.php — ligne 20
```

**Code injecté (extrait) :**

```php
eval(base64_decode("aWYoZGF0ZSgnWS1tLWQnKT4nMjAyNC0wNi0xNScpe2..."));
```

### 4.3 Mécanisme : bombe à retardement obfusquée

Le code injecté était dissimulé sous **deux couches de base64** (Crypté une première fois puis cryptage de la première version cryptée). Sans l'IA, il était quasiment impossile de localiser ce bout de code et de le décrypter pour le comprendre. Une fois décodé, il révèle :

```php
// Couche 1 — décodée :
if(date('Y-m-d') > '2024-06-15') {
    echo base64_decode('<!DOCTYPE html>...<title>Hacked</title>...');
    exit();
}
```

**Fonctionnement :**

1. Avant le 15 juin 2024 : le code injecté ne fait rien — le site s'affiche normalement
2. Après le 15 juin 2024 : le code affiche la page de defacement **avant** le chargement de Joomla, puis stoppe l'exécution (`exit()`)

Ce type de bombe à retardement est conçu pour :

- Passer inaperçu lors des audits post-injection
- Laisser le temps à l'attaquant de placer d'autres backdoors
- Déclencher l'attaque visible longtemps après l'intrusion initiale

### 4.4 Traces d'une intrusion antérieure (2021)

Le dump SQL contient une trace d'un **webshell PHP** uploadé dans le répertoire `/images/` en juillet 2021 :

```
URL enregistrée en base : https://www.bapteme-air-lille.fr/images/sh3.php?cmd=php -r 'eval(base64_decode("zgllkhbpkckqndipow=="));'
```

Cela indique que des attaquants ont **uploadé un fichier PHP exécutable** (`sh3.php`) dans le répertoire `/images/`, normalement réservé aux médias. Ce webshell leur permettait d'exécuter des commandes arbitraires sur le serveur.

> **Note :** Le fichier `sh3.php` n'est plus présent dans l'archive des fichiers fournie — je l'avais détecté et supprimé à l'époque, pensant résoudre le problème.

### 4.5 Chronologie reconstituée de l'attaque

| Date               | Événement                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| ~Juillet 2021      | Upload du webshell `images/sh3.php` — première intrusion confirmée                                                |
| Entre 2021 et 2024 | Injection probable du code malveillant dans `templates/rt_quantive/index.php` via le webshell ou une autre faille |
| 15 juin 2024       | Déclenchement de la bombe à retardement — le site affiche le defacement                                           |
| 14 avril 2026      | Découverte, analyse et nettoyage lors de cette intervention                                                       |

---

## 5. Actions correctives effectuées

### 5.1 Suppression du code malveillant dans le template

**Fichier :** `templates/rt_quantive/index.php`
**Action :** Suppression de la ligne 20 contenant l'appel `eval(base64_decode(...))`.

```diff
- eval(base64_decode("aWYoZGF0ZSgnWS1tLWQnKT4nMjAy..."));
```

**Résultat :** Le site s'affiche correctement, le contenu original est intact.

### 5.2 Suppression des comptes utilisateurs malveillants

**18 comptes spam/malveillants supprimés** de la table `jh3_users` :

| ID  | Utilisateur         | Motif de suppression           |
| --- | ------------------- | ------------------------------ |
| 93  | riagenbuyma         | Spam cyrillique (mail.ru)      |
| 94  | propictifor1976     | Spam (yandex.kz)               |
| 95  | garekathe1988       | Spam viagra                    |
| 96  | treasomonja1982     | Spam viagra                    |
| 97  | threadtazasi1975    | Spam viagra                    |
| 98  | moiducofumb1989     | Spam viagra                    |
| 99  | fispelesi           | Spam cyrillique (mail.ru)      |
| 100 | lworformuvac        | Spam cyrillique (rambler.ru)   |
| 102 | vepurvingcons       | Spam cyrillique (list.ru)      |
| 105 | perhybowfscheer1974 | Spam viagra                    |
| 106 | fisesunfu1974       | Spam viagra                    |
| 107 | utecmocom1989       | Spam viagra                    |
| 108 | ltimocesna1982      | Spam cialis                    |
| 112 | ipenuw              | Spam polonais (rzesomaniak.pl) |
| 113 | egitexety           | Spam polonais (rzesomaniak.pl) |
| 118 | nickviagrapan       | Spam viagra                    |
| 119 | Gabapentino247      | Spam (rambler.ru)              |
| 123 | ThomasVep           | Spam loterie russe ГОСЛОТО     |

Les entrées orphelines dans `jh3_user_usergroup_map` ont également été supprimées.

### 5.3 Audit des fichiers PHP — aucune autre backdoor détectée

Analyse effectuée sur l'ensemble des répertoires `templates/`, `plugins/`, `components/`, `modules/`, `administrator/` à la recherche de :

- `eval(base64_decode(...))`
- `system($_GET[...])` / `exec($_GET[...])` / `passthru($_GET[...])`
- `preg_replace` avec modificateur `/e`
- `assert($_...)` (exécution de code arbitraire)

**Résultat :** Aucun autre code malveillant détecté. Un seul faux positif identifié et écarté (`plugins/system/ja_payment/lib/vendor/USAePay/src/Message/usaepay.php` — code de paiement légitime).

### 5.4 Suppression d'adminer.php

Le fichier `adminer.php` était présent à la racine du site. Cet outil d'administration de base de données, accessible publiquement sans authentification, représente une faille de sécurité majeure.

**Action :** Suppression du fichier.

### 5.5 Désactivation du mode debug

Pour l'environnement de consultation locale, les paramètres suivants ont été ajustés dans `configuration.php` :

```php
public $debug = '0';           // Mode debug désactivé
public $error_reporting = 'default';  // Niveau d'erreur standard
public $caching = '0';         // Cache désactivé (plus pratique en local)
```

---

## 6. État du site après intervention

### 6.1 Ce qui fonctionne

- ✅ Page d'accueil avec le contenu original
- ✅ Navigation dans les menus
- ✅ Articles : offres de baptême, l'avion, FAQ, partenaires
- ✅ Galerie photos (PhocaGallery)
- ✅ Interface d'administration (`/administrator/`)
- ✅ Base de données complète et intacte

### 6.2 Comptes utilisateurs restants (légitimes)

| Utilisateur                    | Rôle                            | Statut                          |
| ------------------------------ | ------------------------------- | ------------------------------- |
| admin                          | Administrateur                  | Actif                           |
| bapteme                        | Compte client principal         | Actif                           |
| hob_admin                      | Prestataire HOB France Services | Actif                           |
| Wilfried, dansette, BOGAERT... | Membres du club (2010-2011)     | Actifs                          |
| MEGRET, Romain, Nabyl...       | Membres récents                 | Bloqués (en attente validation) |

---

## 7. Recommandations pour la remise en production

### 7.1 Sécurité — Actions immédiates

> ⚠️ **Ces actions sont à effectuer AVANT de remettre le site en ligne.**

1. **Changer tous les mots de passe**
   - Compte FTP OVH
   - Compte MySQL OVH
   - Comptes administrateurs Joomla (`admin`, `bapteme`)
   - Accès au panel OVH

2. **Supprimer ou déplacer `adminer.php`** si présent sur le serveur de production

3. **Protéger `/images/` contre l'exécution PHP** — ajouter dans un fichier `.htaccess` dans le répertoire `/images/` :

   ```apache
   php_flag engine off
   <FilesMatch "\.(php|php5|phtml|phar)$">
       Order Deny,Allow
       Deny from all
   </FilesMatch>
   ```

4. **Auditer le serveur OVH** avec un outil comme [Maldet](https://www.rfxn.com/projects/linux-malware-detect/) ou demander à l'hébergeur un scan antivirus

5. **Vérifier les tâches CRON** sur le serveur OVH — les attaquants en installent parfois pour maintenir leur accès

### 7.2 Mise à jour — Actions à planifier

6. **Migrer vers Joomla 4 ou 5** — Joomla 3.10 n'est plus maintenu depuis **août 2023** et ne reçoit plus de correctifs de sécurité. C'est la cause racine de la compromission.

7. **Mettre à jour le template** — Le template Gantry 4 / rt_quantive est incompatible avec Joomla 4. Il faudra soit :
   - Trouver un template de remplacement compatible Joomla 4
   - Faire migrer le design vers un nouveau template

8. **Mettre à jour tous les plugins** : JCE Editor, PhocaGallery, DTRegister, etc.

### 7.3 Surveillance — Actions à mettre en place

9. **Activer les logs d'accès** chez OVH et les surveiller régulièrement

10. **Installer un plugin de sécurité** Joomla (ex: Akeeba Admin Tools, RSFirewall) pour détecter les modifications de fichiers

11. **Mettre en place des sauvegardes automatiques** quotidiennes (Akeeba Backup)

12. **Configurer des alertes par email** pour les connexions administrateur

---

## 8. Accès à l'environnement local

Pour consulter le site restauré sur cette machine :

```bash
# Démarrer l'environnement
cd ~/Projets/lille-ulm/www
ddev start

# Arrêter l'environnement
ddev stop
```

**URLs :**

- Site : http://lille-ulm.ddev.site
- Administration : http://lille-ulm.ddev.site/administrator/

---

_Document généré le 14 avril 2026 — à mettre à jour après chaque action complémentaire._
