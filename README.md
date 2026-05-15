# TSP Implementations

Python implementations of heuristic and informed-search approaches for the Travelling Salesman Problem. This project was built for an algorithms coursework setting, using a provided validation harness and city-file format, with the core work focused on designing and improving search strategies for producing valid tours under runtime constraints.

## What It Shows

- Practical implementation of graph-search and combinatorial optimisation techniques.
- Clear comparison between baseline and enhanced versions of the same algorithm families.
- Use of heuristics, local search, memoisation, and adaptive restart strategies to improve solution quality and runtime behaviour.
- Ability to work within strict external constraints, including fixed input formats, validation logic, and standard-library-only Python.

## Implementations

| File | Algorithm | Notes |
| --- | --- | --- |
| `AlgBbasic.py` | Basic Greedy Search | Builds a tour by repeatedly selecting the cheapest available next edge. |
| `AlgBenhanced.py` | Enhanced Greedy Search | Adds randomized restarts, adaptive restart counts, and 2-opt local search to refine tours. |
| `AlgAbasic.py` | Iterative Deepening A* | Uses an MST-based heuristic, implemented with Prim's algorithm, to guide search. |
| `AlgAenhanced.py` | Enhanced Iterative Deepening A* | Improves start-city selection and memoises MST heuristic values to reduce repeated work. |

## Running

Each script can be run directly with Python:

```bash
python AlgBenhanced.py AISearchfile058.txt
```

The coursework harness expects the city files and `alg_codes_and_tariffs.txt` to sit in the parent directory structure used by the original assignment. When run with the expected inputs, each script writes a validated tour file containing the generated route, tour length, and runtime note.

## Tech

- Python 3
- Standard library only
- Graph algorithms, heuristic search, greedy optimisation, and local search

## Why This Project Matters

The interesting part of this repo is not just solving TSP instances, but improving imperfect algorithms under real constraints. The enhanced versions show iterative refinement: starting from understandable baselines, then adding targeted improvements such as 2-opt, restart strategies, MST heuristics, and memoisation to make the search more effective.