title: Structurer sa documentation technique grâce à Diataxis
description: À la découverte d'un framework de qualité de la documentation
date: 20240117
author: Simon
tags: article, méthodo, learnInPublic

Je suis actuellement Ops sur une mission de delivery, et nous avons décidé de refondre la base documentaire de l'équipe Infra. Le projet a maintenant 3 ans et cette base est composée de plus de 150 pages de "how-to", de post mortems, de décisions d’architecture, de CR d'ateliers... tout cela plus ou moins mélangé. 

Même en cherchant une info à partir d'un mot clé précis, cette base est difficile à naviguer, à manipuler et il est compliqué de savoir où trouver l'information que l'on cherche.

Au moins deux de mes collègues m'ont parlé de [Diataxis](https://diataxis.fr/) comme base de travail pour structurer une documentation. J'ai creusé le sujet, je me suis mis à l’utiliser à la fois pour la documentation de mon projet et pour ma base de connaissance personnelle, voilà ce que j'ai appris.

# Le problème que Diataxis cherche à résoudre

On dit souvent que le plus compliqué lorsque l'on code ce n'est pas d'écrire du code compréhensible par une machine, aka "ça compile", mais d'écrire du code compréhensible par un humain. Une bonne documentation doit AVANT TOUT être compréhensible et agréable à lire pour un humain.

Pour qu’une documentation soit lue, il doit être facile pour un utilisateur de savoir se diriger dans cette documentation, savoir où trouver tel élément ou tel type d'information.  
Pour qu’une documentation soit maintenue, ajouter ou modifier une information dans la base documentaire doit être simple et évident.

# La proposition de Diataxis

Diataxis part d’un principe simple : la documentation doit être centrée autour du besoin utilisateur. Quand un lecteur cherche à utiliser la documentation d'un projet, il souhaite répondre à un besoin. C'est en se concentrant sur ce besoin que l’on structure une *bonne* documentation.

Selon son niveau d'implication ou de maturité avec le produit, un utilisateur va avoir différents besoins :

* **Débutant** : l’utilisateur veut chercher à comprendre ce que sait faire le produit et en quoi il peut lui être utile. Du point de vue du rédacteur de la documentation, on cherche à convertir un prospect en utilisateur actif.
* **Avancé** : l’utilisateur connaît déjà le produit, il sait quel service le produit peut lui rendre. Il va chercher à exécuter une tâche en particulier ou à répondre à un cas précis.
* **Expert/Curieux** : l’utilisateur connaît très bien le produit, il sait l'utiliser mais il cherche à approfondir ses connaissances autour du produit et à comprendre les choix techniques qui ont été faits.

On peut aussi diviser nos utilisateurs dans plusieurs classes de *personas* : 

* **Simple utilisateur** : il cherche juste à utiliser l'outil, la librairie, le produit mais veut s'impliquer le moins possible dans sa compréhension. Il lui faut quelque chose de très simple qui lui permet en quelques minutes de savoir comment utiliser le produit mis à disposition, quels sont les principaux paramètres...
* **Développeur qui construit autour de la solution** : il a besoin de comprendre comment s'interfacer avec l'outil ou le produit, comment l'instancier et le paramétrer, mais il n'a pas besoin de comprendre les détails d'implémentation interne.
* **Contributeur qui développe le produit lui-même** : il a besoin de comprendre les choix techniques, la machinerie à l'intérieur de l'outil, les standards d'implémentation afin de pouvoir contribuer à son évolution.

Diataxis part du principe que l'on peut répondre à ces différents cas d'usage grâce à quatre types de documentation :

| Type de documentation | Intention                                         | La question à laquelle on cherche à répondre | Forme                    | Analogie                                             |
|-----------------------|---------------------------------------------------|----------------------------------------------|--------------------------|------------------------------------------------------|
| Tutoriel              | Permettre à un débutant de démarrer / d'apprendre | "Pouvez-vous m'apprendre à... ?"             | Une leçon, un cours      | Apprendre à un enfant à cuisiner                     |
| Guide pratique        | Montrer comment résoudre un problème spécifique   | "Comment puis-je... ?"                       | Une série d'étapes       | Une recette de cuisine                               |
| Référence             | Décrire le fonctionnement interne / informer      | "Qu'est ce que... ?"                         | Une description brute    | Un article wikipedia sur un ingrédient de la recette |
| Contexte              | Expliquer/Clarifier                               | "Pourquoi... ?"                              | Une discussion, un débat | Un livre sur l'histoire de la cuisine                |

## Les tutoriels

Un tutoriel est avant tout destiné aux utilisateurs débutants. On cherche à aider le lecteur à comprendre ce qu'il peut faire avec l'outil afin qu'il puisse ensuite l'utiliser en autonomie.  
A la fin d'un tutoriel, le lecteur doit être capable de comprendre le reste de la documentation car il a assimilé le fonctionnement global du produit.  
Ici c'est le rédacteur qui définit l'objectif du tutoriel, c’est le rédacteur qui décide comment il souhaite transformer un débutant en utilisateur autonome, c'est lui qui sait ce qui doit être démontré quant à l'utilisation du produit.  
L'objectif d'un tutoriel c'est de faire découvrir par la pratique les différentes possibilités d'un outil.  

## Les guides pratiques

On consulte un guide pratique quand on cherche à résoudre un problème précis, quand on cherche à répondre à la question "Comment...". Par exemple "Comment ajouter une clé ssh sur toutes nos machines ?".  
Un guide pratique est une liste d'étapes à exécuter dans l'ordre comme une recette de cuisine.  
On consulte généralement un guide pratique lorsqu’on est bloqué dans notre flow de travail.   
Du point de vue de l’utilisateur, tout ce qui n'aide pas à résoudre son problème spécifique freine son flow de travail et n'a pas sa place dans un guide pratique.  

## Les documents de références

Un document de référence est une description froide et objective du fonctionnement interne du produit ou de l'équipe : quelles sont les options disponibles, comment instancier l'outil, quelles sont les conventions de nommage...  
L'objectif d'un document de référence c'est de donner toutes les informations nécessaires à la compréhension du produit sans avoir besoin d'aller lire le code ou de demander à l'équipe qui l'a implémenté.  
Les documents de référence doivent être des sources de certitude et de vérité pour l'utilisateur.  
On peut retrouver dans cette partie les documents d'architecture, les spécifications, les standards d'implémentation et d'organisation de l'équipe : convention de nommage, règles de revue de code et de collaboration...  
Un document de référence peut être vu comme un dictionnaire : il n'est pas fait pour être lu de bout-en-bout mais pour être consommé en fonction du besoin. On le scanne, on récupère l’info dont on a besoin et on le repose.  

## Les documents de contexte

Si les documents de références cherchent à décrire *verticalement* le fonctionnement du produit, les documents de contexte vont plutôt servir à donner du contexte *horizontal*. Un document de contexte c'est un [ADR](https://blog.octo.com/architecture-decision-record), le compte-rendu d'un atelier...  
Le but d'un document de contexte c'est d'améliorer la compréhension d'un sujet, d'expliciter une décision, de préciser le contexte dans lequel le produit évolue, d'avoir des connaissances plus riches et profondes du sujet.  
Ce genre de document est rarement utile pour utiliser le projet mais peut le devenir quand on cherche à comprendre d'où vient son architecture, telle ou telle décision, quelles sont les alternatives possibles...  

# En résumé

Voici le tableau de décision que j’utilise pour catégoriser un document selon mon intention et le besoin utilisateur :

| Si le contenu décrit...            | et que l'utilisateur cherche à...&emsp; | alors il doit aller dans... |
|------------------------------------|-----------------------------------------|-----------------------------|
| des étapes pratiques               | apprendre, comprendre                   | les tutoriels               |
| des étapes pratiques               | coder, implémenter, réaliser            | les guides pratiques        |
| des connaissances théoriques&emsp; | coder, implémenter, réaliser            | les documents de référence  |
| des connaissances théoriques&emsp; | apprendre, comprendre                   | Les documents de contexte   |

# Retour d’expérience après quelques semaines

Nous avons refondu une grande partie de la documentation existante de notre projet et l'utilisation de Diataxis nous a aidé à :  

* découper notre documentation selon les 4 grandes catégories proposées.
* redécouper nos pages existantes dans différents documents car nos pages historiques  mélangeaient références, contextes et guides pratiques.
* savoir si un élément était nécessaire dans une documentation ou non : nous avons supprimé beaucoup d'éléments dans les guides pratiques car ils ne servaient pas directement à atteindre l'objectif de chaque guide.
* poser des faits sur certaines douleurs que nous avions :
	* nous n'avons pour l'instant aucun tutoriel, ce qui rend l'onboarding pour une personne "débutante" sur la mission très complexe.
	* nous avons très peu de documents de référence, le meilleur moyen aujourd’hui d'avoir une information étant d'aller le lire dans le code.

Diataxis est un modèle plutôt simple à adopter et utiliser, cela aide l’équipe à savoir où doit aller chaque information et comment elle doit être formatée.

Je me suis également mis à utiliser les 4 catégories de Diataxis pour structurer ma base de connaissances personnelle. En me considérant comme l'unique *persona*, Diataxis m’a permis de découper ma documentation selon que je cherche à répondre à une question particulière "comment récupérer toutes les ressources d'un namespace Kubernetes ?" ou selon que je cherche à approfondir mes connaissances ou mes notes sur un sujet en particulier.

---

Quelques sources pour aller plus loin :

* [https://documentation.divio.com/](https://documentation.divio.com/)
* [https://diataxis.fr/](https://diataxis.fr/)
* [Youtube - What nobody tells you about documentation](https://www.youtube.com/watch?v=t4vKPhjcMZg)
