---
layout: default
title: Paul Klint
---

# Paul Klint - The Revenge of the Coroutines

One of the key questions of software engineering is how to structure large software systems and what concepts are best suited to achieve modular, reusable, extensible, and maintainable software.

Coroutines are a generalization of subroutines and were introduced by Conway in 1958 to organize the cooperation between compiler phases. They provide an abstraction of both state and control and have been used to implement, for instance, iterators, streams and cooperative multitasking. The coroutine's state abstraction has become popular in object-oriented programming while its control abstraction is provided by various process-oriented approaches. Coroutines are supported by only a few dozen languages, mostly in simplified form. Today they are gaining in popularity as a light-weight alternative to threads. Should we reconsider coroutines as a software structuring concept?

First, I will give a brief recap of the coroutine concept itself and show examples how they can be used. Next, I will report on a larger scale experiment to test coroutines as structuring device. In the run-time system of the Rascal compiler (joint work with Anastasia Izmaylova) we make extensive use of coroutines to implement pattern matching and backtracking. This experiment demonstrates that when coroutines are combined with partial parameterization this can lead to substantially simpler and smaller code. We also discovered that list matching and set matching can be implemented as instances of the same matching algorithm.

Based on this experience,  I claim that coroutines deserve a more prominent place in the software engineer’s toolbox.
