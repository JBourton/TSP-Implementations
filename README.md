# TSP Implementations

This repo holds my python implementations of heuristic and informed-search approaches for solving the Travelling Salesman Problem. I built this project as part of an "AI search" module at Durham University.

## What It Shows

- Practical implementation of graph-search and combinatorial optimisation techniques
- Clear comparison between baseline and enhanced versions of the same algorithm families
- Use of heuristics, local search, memoisation, and adaptive restart strategies to improve solution quality and runtime behaviour
- Ability to work within strict external constraints, including fixed input formats, validation logic, and standard-library-only Python

## Implementations

| File | Algorithm | Notes |
| --- | --- | --- |
| `AlgBbasic.py` | Basic Greedy Search | Builds a tour by repeatedly selecting the cheapest available next edge |
| `AlgBenhanced.py` | Enhanced Greedy Search | Adds randomized restarts, adaptive restart counts, and 2-opt local search to refine tours |
| `AlgAbasic.py` | Iterative Deepening A* | Uses an MST-based heuristic, implemented with Prim's algorithm, to guide search |
| `AlgAenhanced.py` | Enhanced Iterative Deepening A* | Improves start-city selection and memoises MST heuristic values to reduce repeated work |

## Performance Comparison

Based on official validation feedback, here's how the algorithms compare across test instances:

| Metric | AlgB (Greedy) | AlgA (IDA*) |
|--------|---------------|-----------|
| Smallest instance (12 cities) | 56, 0.0s | 56, 0.0s |
| Medium instance (58 cities) | 26,948, 1.0s | 27,384, 1.4s |
| Largest instance (535 cities) | 48,998, 4,753.6s | 50,069, 17,053.0s |

The key finding: Greedy's O(n²) complexity vastly outperforms IDA* on larger instances, but the enhanced versions narrow the solution quality gap through intelligent local search and adaptive strategies.

## Running

Each script can be run directly with Python:

```bash
python AlgBenhanced.py AISearchfile058.txt
```

The coursework harness expects the city files and `alg_codes_and_tariffs.txt` to sit in the parent directory structure used by the original assignment. When run with the expected inputs, each script outputs a valid tour.

## Why This Project Matters

The interesting part of this repo is not just solving TSP instances, but improving imperfect algorithms under real constraints. The enhanced versions show iterative refinement: starting from underperforming baselines and systematically applying optimization techniques to achieve measurable improvements in both runtime and solution quality.
