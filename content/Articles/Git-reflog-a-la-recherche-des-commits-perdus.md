title: Git reflog : à la recherche des commits perdus
description: Comment la commande git reflog peut être très utile pour corriger quelques mauvaises manips
date: 20241224
author: Simon
tags: article, tech, git, learninpublic

## TL;DR

* Si vous avez abusé de `git reset --hard` et que vous avez perdu un commit, `git reflog` peut vous aider.
* Si vous cherchez un journal complet des actions Git réalisées en local, `git reflog` peut vous aider.

## En plus long :

Cette fin d'année j'ai pas mal (re)découvert `git` en lisant quelques publications de références sur le sujet ([Pro Git](https://git-scm.com/book/en/v2) ou [How Git Works](https://wizardzines.com/zines/git/) par exemple). J'ai creusé quelques commandes que je n'avais pas l'habitude d'utiliser, en particulier `git reflog`, voilà ce que j'ai retenu : 

### On commence par quelques notions 

#### Les références (ref): 
Une référence c'est un alias compréhensible qui pointe sur un commit. Pensez à un nom de domaine sur Internet : au lieu de manipuler des adresses IP compliquées (ég. `185.15.58.226`), on préfère utiliser un nom comme `wikipedia.com`. Avec Git, les références jouent un rôle similaire.

On manipule beaucoup de références quand on utilise Git : 

* `Les branches` : `mafeaturebranch`est une référence qui se déplace au fur et à mesure que "j'ajoute" des commits à ma branche (cette définition n'est pas complètement exacte, mais pour notre sujet d'aujourd'hui on va dire que l'approximation suffit).
* `Les tags` :  Un tag est un pointeur vers un commit particulier.
* `stash` : stash est également une référence un peu particulière vers un commit.
* `head`: on en reparle juste en dessous.

Si on veut creuser un peu plus, les références courantes sont stockées dans le dossier `.git/refs` d'un repo Git :

```
.git/refs
├── heads
│   ├── bsr-mettre-en-lowercase-enregistrements-dns
│   ├── bsr-rend-ansible-vpn-infra-v1-idempotent-en-check-mode
│   ├── doc-fiche-reflexe-mes-pods-ont-bougés
│   ├── docs-adr-ttl-rabbitmq
│   ├── fix-corriger-handler-systemd-exporter
│   ├── main
│   ├── preprod
│   └── valider-drift-ansible-hebdo
├── remotes
│   └── origin
│       ├── HEAD
│       ├── doc-fiche-reflexe-mes-pods-ont-bougés
│       ├── fixer-adresse-ips-routers
│       ├── main
│       ├── permettre-la-persistence-des-logs
│       └── preprod
├── stash
└── tags
```

Pour savoir sur quoi pointe une référence, il suffit de regarder le contenu d'un des fichiers : 

``` 
cat .git/refs/heads/main
b0318fbadce00bcf2ce21104d12de267d60e6189
```

#### La référence HEAD : 

`HEAD` représente la "tête de lecture" de Git, c'est comme l'aiguille d'une platine vinyle, `HEAD` pointe vers le commit actuellement actif.

Git stocke la branche (ou le commit) sur lequel `HEAD` pointe dans le fichier `.git/HEAD` :

```
cat .git/HEAD
ref: refs/heads/main
```

Si je fais un `git show HEAD` j'affiche le commit sur lequel pointe la référence `HEAD` actuellement

```
$ git show HEAD

commit b0318fbadce00bcf2ce21104d12de267d60e6189 (HEAD -> main, origin/main, origin/HEAD)
Author: John Doe <john@doe.com>
Date:   Thu Dec 19 12:14:28 2024 +0000
[...]
```

On remarque que logiquement le hash de commit est le même que celui renvoyé par la commande `cat .git/refs/heads/main` plus haut
#### Les reflogs (reference logs)

Voilà ce que nous dit la doc Git : _Reference logs, or "reflogs", record when the tips of branches and other references were updated in the local repository_

Un reflog, c'est l'historique détaillé d'une référence :

* La liste ordonnée des commits sur lesquels cette référence a pointé.
* La liste des actions ayant conduit à ces changements (checkout, pull, reset, etc.).

Pour afficher un reflog, on utilise la commande `git reflog show` : 

```
git reflog show HEAD

b0318fbad HEAD@{0}: pull: Fast-forward
6398927de HEAD@{1}: checkout: moving from main to main
6398927de HEAD@{2}: pull: Fast-forward
70d300375 HEAD@{3}: checkout: moving from main to main
70d300375 HEAD@{4}: checkout: moving from fix-changer-nom-cluster-dev to main
679bfa305 HEAD@{5}: commit: fix(kubernetes/dev): corriger le nom du nouveau cluster de dev
70d300375 HEAD@{6}: checkout: moving from main to fix-changer-nom-cluster-dev
70d300375 HEAD@{7}: checkout: moving from main to main
70d300375 HEAD@{8}: checkout: moving from creer-utilisateur-read-only-gui to main
70d300375 HEAD@{9}: checkout: moving from main to creer-utilisateur-read-only-gui
70d300375 HEAD@{10}: pull: Fast-forward
6a87866ac HEAD@{11}: checkout: moving from parametrer-correctement-ntp to main
97833b121 HEAD@{12}: rebase (finish): returning to refs/heads/parametrer-correctement-ntp
97833b121 HEAD@{13}: rebase (pick): refacto(ntp/local): supprimer les indirections dans le code ansible
fefbc2b6b HEAD@{14}: rebase (squash): feat(ntp/local): utiliser timesyncd pour synchroniser les serveurs
e666efb31 HEAD@{15}: rebase (start): checkout main
c9ef7b474 HEAD@{16}: commit: wip(tosquash/squash): squash
87b3ed256 HEAD@{17}: rebase (finish): returning to refs/heads/parametrer-correctement-ntp
87b3ed256 HEAD@{18}: rebase (pick): refacto(ntp/local): supprimer les indirections dans le code ansible
e666efb31 HEAD@{19}: rebase (squash): feat(ntp/local): utiliser timesyncd pour synchroniser les serveurs
[...]
```

### Et à quoi ça sert ?

Si on décortique la sortie de la commande `git reflog`, voilà ce qu'on trouve : 

`679bfa305 HEAD@{5}: commit: fix(kubernetes/dev): corriger le nom du nouveau cluster de dev`

* `679bfa305` : le hash du commit sur lequel pointe/pointait la référence
* `HEAD` : le nom de la référence
* `{5}` : index relatif de "quand" s'est passé l'évènement (le mouvement s'est passé il y a 5 actions)
* `commit` : l'action qui a généré le mouvement, on voit qu'on retrouve différentes actions (checkout, pull, rebase...)
* `fix(kubernetes/dev): corriger le nom du nouveau cluster de dev` des détails sur l'action, ici le message du commit mais ça peut également être des détails pour savoir depuis/vers quelle branche nous avons switché...

Le reflog me permet donc d'avoir deux informations intéressantes : 

1. La liste de tous les commits par lesquels je suis passé sur mon poste local (peu importe si j'étais sur une branche, si j'ai checkout un commit qui n'est plus associé à aucune branche, si mon commit a par la suite été supprimé d'une branche, modifié, amendé...).
2. La liste de toutes les actions de modification que j'ai pu faire sur mon poste local.

Combiné à quelques filtres, reflog ça peut servir à plusieurs choses : 

```
git reflog show HEAD                 # Voir toutes les dernières actions que j'ai pu faire en local sur ma machine et qui ont modifié HEAD
git reflog show HEAD | grep checkout # Voir toutes les branches explorées.
git reflog show HEAD | grep rebase   # Revoir toutes les étapes d'un rebase.
git reflog show HEAD | grep commit   # Voir tous les commits créés (peu importe sur quelle branche ils sont partie ensuite).
```

Mais surtout, vu que `git reflog` est capable de retracer tous les commits par lesquels est passé `HEAD`, ça permet de rattraper quelques bêtises :

Si j'ai reset tout mon travail courant un peu trop vite (au hasard un petit `git reset --hard origin/main` des familles) et que j'ai perdu mes commits, un coup de `git reflog` pour voir les différents commit que j'ai créé dans le temps et récupérer mes petits et c'est reparti : 
```
# Je checkout une nouvelle branche et je créer quelques commits
git checkout -b manouvellebranche
echo "1" >> fichier.txt
git add fichier.txt
git commit -m "commit 1"
echo "2" >> fichier.txt
git add fichier.txt
git commit -m "commit 2"
echo "3" >> fichier.txt
git add fichier.txt
git commit -m "commit 3"

# Je valide la liste de mes commits sur cette branche : 
git log --oneline
aea190a06 (HEAD -> manouvellebranche) commit 3
88fa0e8b6 commit 2
0a7da724f commit 1

# Je reset mon working directory pour qu'il ressemble à ce que j'ai sur origin/main
git reset --hard origin/main
git log --oneline
7fe731e2c (HEAD -> manouvellebranche, origin/main, origin/HEAD, main)

# J'ai donc "perdu" mes 3 commits, pour les retrouver, un coup de gitreflog : 
git reflog 
7fe731e2c (HEAD -> manouvellebranche, origin/main, origin/HEAD, main) HEAD@{0}: reset: moving to origin/main
aea190a06 HEAD@{1}: commit: commit 3
88fa0e8b6 HEAD@{2}: commit: commit 2
0a7da724f HEAD@{3}: commit: commit 1

# Pour ensuite récupérer mes commits je peux choisir de checkout ma branche à partir de commit 3 ou je peux choisir de cherry-pick uniquement le commit de mon choix
```


Si j'ai malencontreusement supprimé une branche que je n'avais pas poussé sur mon serveur (quelque chose du genre `git branch -D mabranche` ou `git checkout -B mabranch origin/mabranch`, je peux assez facilement me ratrapper : 
```
# Je checkout une nouvelle branche et je créer quelques commits
git checkout -b monautrebranche
echo "1" >> fichier.txt
git add fichier.txt
git commit -m "commit 1"
echo "2" >> fichier.txt
git add fichier.txt
git commit -m "commit 2"
echo "3" >> fichier.txt
git add fichier.txt
git commit -m "commit 3"

# Je valide la liste de mes commits sur cette branche : 
git log --oneline
751a14deb (HEAD -> monautrebranche) commit 3
6af9b9d14 commit 2
c82ce38f5 commit 1

# Je fais un peu de ménage sur mon poste et je supprime la branche 
git checkout main
git branch -D monautrebranche

# Finalement je souhaite récupérer ma branche
git reflog monautrebranche
fatal : argument 'monautrebranche' ambigu : révision inconnue ou chemin inexistant.

# Et oui, si on supprime une branche, son reflog disparait également, mais il est probable que HEAD puisse nous aider : 
7fe731e2c (HEAD -> master, origin/master, origin/HEAD, manouvellebranche) HEAD@{0}: checkout: moving from monautrebranche to master
751a14deb HEAD@{1}: commit: commit 3
6af9b9d14 HEAD@{2}: commit: commit 2
c82ce38f5 HEAD@{3}: commit: commit 1

# Je recréer monautrebranche à partir du commit 3
git checkout -b monautrebranche HEAD@{1}

# Je vérifie que j'ai bien retrouvé tous mes commits
git log --oneline
751a14deb (HEAD -> monautrebranche) commit 3
6af9b9d14 commit 2
c82ce38f5 commit 1
```

# Et c'est quoi la différence avec git log

En vrai la commande `git reflog` est un alias de la commande : `git log --walk-reflogs --abbrev --pretty=oneline`. Si on lit la doc, `--use-reflog` permet d'afficher l'historique en parcourant le reflog plutôt qu'en parcourant l'arbre des parents. Ainsi plutôt que de connaître l'enchainement des différents commits en remontant de parent en parent, on préfère remonter de commit en commit en cherchant par où est passé HEAD, même si il n'y a pas forcément de lien entre 2 commits successifs. Ce que j'en comprends c'est que : 

* Par défaut `git log` permet de remonter l'arbre généalogique d'un commit en remontant ses parents de proche en proche.
* `git reflog` permet de remonter les différents endroits où est passé une référénce.

# Les limites

* Un reflog est local à une machine, ainsi il n'est pas poussé sur un serveur distant, il n'est pas possible de récupérer le reflog de son collègue en pullant un repo.
* Si vous n'avez pas commité votre code, `git reflog` ne pourra rien pour vous, (tu vois le petit `git restore .` après 2 heures de taff ?).

# Quelques références et pointeurs qui m'ont aidé à comprendre git reflog

* [Git reflog - ma commande (sous-côtée) préférée de Git - Eve Julliard](https://www.youtube.com/watch?v=E09Mml_ZHCw)
* [How git works zine - Julia Evans](https://wizardzines.com/zines/git/)
* [La documentation officielle de git reflog](https://git-scm.com/docs/git-reflog)
