---
layout: default
title: Fahrad Arbab
---

# Composition of Concurrency - Fahrad Arbab

Traditionally, concurrency protocols manifest themselves only as
ephemeral side-effects of execution of concrete structured primitive
actions that comprise a piece of software.  Understanding and reasoning
about the properties of concurrency protocols are notoriously
difficult.  Such ephemeral manifestation of concurrency protocols
increases this difficulty by making the study of their properties
possible only indirectly, through a convoluted analysis of their
underlying structured actions.  Furthermore, the complex relationship
between structured actions whose execution manifests a  protocol and the
protocol itself, makes it non-trivial, if not impossible, to realize
desired composition or manipulation of concurrency protocols by
translating them into composition or manipulation of their concrete
underlying structured actions.

Our work on Reo, its semantics, and tools shows that treating
concurrency protocols as explicit first-class constructs, yields a very
expressive model of concurrency, with useful software engineering
properties.At its core, Reo proffers an /interaction-based/ model of
concurrency where more complex protocols result from composition of
simpler, and eventually primitive, protocols. In Reo, combining a small
set of user-defined synchronous and asynchronous primitives, in a manner
that resembles construction of electronic circuits from gates and
elements, yields arbitrarily complex concurrency protocols. Semantics of
Reo preserves synchrony and exclusion through composition.This form of
compositionality makes specification of protocols in Reo simpler than in
conventional models and languages, which offer low-level synchronization
constructs (e.g., locks, semaphores, monitors, synchronous methods).
Moreover, the high-level constructs and abstractions in Reo also leave
more room for compilers to perform novel optimizations in mapping
protocol specifications to lower-level instructions that implement them.
In on-going work we currently develop code generators that produce
executables whose performance and scalability on multi-core platforms
compare favorably with hand-crafted, hand-optimized code.

