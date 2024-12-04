title: Votre architecture est le résultat des luttes de pouvoir au sein de votre organisation
description: Intuition : pourquoi mon architecture n'a aucun sens
date: 20241204
author: Simon
tags: article, intuition, orga, méthodo


---

_Intuition : Dans cette série d'articles courts je souhaite simplement partager des intuitions que j'ai, ce ne sont pas des idées qui sont encore complètement construites et abouties, mais je les trouve déjà assez intéressantes pour en proposer une ébauche_

---

Après plusieurs missions dans différents contextes, je me suis rendu compte d’une chose bête : nos architectures techniques sont rarement le fruit de décisions purement techniques, froides et éclairées.
Conway le disait déjà il y a un paquet d'années dans son fameux papier [“How Do Committees Invent?“](https://www.melconway.com/Home/pdf/committees.pdf) : _"organizations which design systems [...] are constrained to produce designs which are copies of the communication structures of these organizations"_

Dans son papier Conway définit ainsi que si mon organisation c’est 5 boîtes reliées par 9 flèches, il y a de grandes chances pour que l’architecture que je vais dessiner finisse par ressembler à quelque chose comme… 5 boîtes et 9 flèches. Ce que ne fait pas vraiment Conway en revanche, c’est qu’il ne parle pas du contenu des boîtes et des flèches.

De mon côté je suis convaincu qu'au-delà de la structure de communication d’une entreprise, ce sont les intérêts des différents acteurs (les gens dans les boîtes) qui  jouent un rôle crucial dans le design d’une architecture. Chaque élément de mon architecture me donne des pouvoirs, de l’influence, du budget ou m’apporte des problèmes. Chaque équipe/direction/directeur a ses propres intérêts, et les intérêts de chacun sont rarement de produire la meilleure architecture possible…

J’ai commencé à chercher quelques frameworks/outils pour analyser une architecture sous ce prisme et je me suis rendu compte qu’on pouvait se poser les questions que l’on se pose lorsque l’on fait une analyse géopolitique. Chacun a un peu sa définition, mais celle que je retiens c’est : la géopolitique c'est l'étude des relations entre géographie et pouvoir : quelle terre/territoire donne quel pouvoir et comment les acteurs internationaux s'organisent et interagissent de manière officielle ou officieuse pour conserver ou acquérir ce pouvoir. Si on transpose ça à l’étude d’une architecture technique, ça donne :

* __Où__ : quel est le territoire que l’on souhaite étudier : on peut simplement se dire que notre schéma d’architecture c’est le territoire, le gâteau qu’il faut se partager
* __Qui__ : qui sont les acteurs en jeu, quelles équipes, qui est là pour se partager le gâteau…
* __Quoi__ : quels sont les pouvoirs actuels de chaque acteur et quels sont les pouvoirs qu’apporte chaque élément de l’architecture
* __Pourquoi__ : quels sont les intérêts de chaque groupe/direction ? Pourquoi une équipe souhaiterait être owner d’un pan de l’architecture ou un autre  ?

Jusqu’ici cette liste de questions ne m’a clairement pas permis de prendre ou d’orienter de meilleures décisions d’architecture. En revanche, elle m’a permis de comprendre que les architectures sur lesquelles je bosse sont rarement cassées “par accident”, ce n’est pas un bug mais bien une feature.  Elles ne répondent peut-être pas ou plus au problème initial mais elles répondent exactement aux luttes de pouvoir, aux guerres de territoire et aux dysfonctionnements de l’organisation qui les a conçues.
