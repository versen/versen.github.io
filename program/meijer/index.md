---
layout: default
title: Erik Meijer
---

# Erik Meijer - Contravariance is the Dual of Covariance Implies Iterable is the Dual of Observable (Making Money Using Math)

Every developer that has ever dealt with contra- and covariance in a
modern OO language with generics, shivers with fear when they have to deal
with these concepts in their code (except of course in Dart language,
where all generic types are covariant).

Typically the solution is to click, click, click, click on the "suggested
fix" by the IDE until the error messages finally go away. To add insult to
injury, all this panic is for nothing since typically at runtime all
generics are erased anyway, so all thus type torture really didn’t matter
in the end (except in .NET where generics is reified).
However, fear no more!

In this talk we will provide trauma recovery therapy for victims of
variance by explaining the concepts from first principles using real world
examples such as vending machines and garbage cans.
For additional fun, we will throw in some good old imperative side-effects
and show how the simplest possible covariant type of getters()=>T and the
simplest contra-variant type of setters T=>() are essentially the same as
Iterator[+T] and Observer[-T].

Add a pinch of self-application on top of that, and we discover that
`Iterable[+T]` boils down to `Iterator[Iterator[T]] = ()=>(()=>T)` and
`Observable[+T]` boils down to `Observer[Observer[T]] = (T=>())=>()`. Lambdas
all the way down, and all arrows reversed.

In case you wondered why Scala uses +T for covariance and -T for
contravariance, and why a contravariant type in a contravariant position
becomes a covariant type, well, that is all part of the magic of the
Curry-Howard isomorphism, but we’ll have to leave that for another talk.
The most amazing thing of all however is that companies like Netflix are
powered by this exact duality in the form of RxJava. And after this talk,
you too will know how to make money using math.
