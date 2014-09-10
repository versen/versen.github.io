---
layout: default
title: Jaco van de Pol
---

# Power optimisation for multi-processor dataflow applications - Jaco van de Pol

Synchronous Data Flow (SDF) provides a convenient formalism for the
design of streaming applications on embedded multi-processor systems.
SDF tools provide efficient algorithms for mapping tasks onto processors,
and scheduling them in time.

In reality, hardware platforms are heterogeneous. Processors provide different
capabilities and vary in speed, memory, and energy consumption. The design
problem is complicated by constraints on the mapping of tasks to processors.
Moreover, a tradeoff is required between time and energy consumption.

We propose to complement a functional SDF description by a realistic Processor
Application Model (PAM). The PAM describes constraints, speed and power
consumption of the processors. It also describes the dynamic power management
capabilities of the hardware system. Examples include voltage and frequency scaling,
which can even be applied to individual voltage-frequency islands.

We provide a systematic and automatic translation of the application (SDF) and
the hardware (PAM) to Timed Automata with costs. Subsequently, we use UPPAAL
to determine efficient mappings and schedules on a minimal set of processors, and
UPPAAL CORA to compute optimal schedules and energy-management strategies,
taking into account trade-offs between time and energy.
