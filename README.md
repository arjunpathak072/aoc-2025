# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) written in Python.

## Structure

```
aoc-2025/
├── day_01/
│   ├── p1.py          # Part 1 solution
│   ├── p1.in          # Part 1 input
│   ├── p2.py          # Part 2 solution
│   └── p2.in          # Part 2 input
├── day_02/
│   ├── p1.py
│   ├── p1.in
│   ├── p2.py
│   └── p2.in
├── day_03/
│   ├── p1.py
│   ├── p1.in
│   ├── p2.py
│   └── p2.in
└── ...
```

Each day has its own directory containing:
- `p1.py` - Solution for part 1
- `p1.in` - Input data for part 1
- `p2.py` - Solution for part 2
- `p2.in` - Input data for part 2

## Running Solutions

Solutions read from stdin. To run a solution:

```bash
python day_01/p1.py < day_01/p1.in
```

Or from the day directory:

```bash
cd day_01
python p1.py < p1.in
```

## Setup

This project uses Python 3.13+ and uv for dependency management.

```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate
```
