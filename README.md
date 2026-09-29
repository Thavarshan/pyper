# pyper

[![tests](https://github.com/Thavarshan/pyper/actions/workflows/tests.yml/badge.svg)](https://github.com/Thavarshan/pyper/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](pyproject.toml)

A Python learning playground: 94 coding challenges that start with the basics
and build up to LeetCode-style algorithms. You solve them **test-first**.

Each challenge is a stub function (or class) that just raises
`NotImplementedError`. Above it, a detailed docblock explains the problem, with
examples, constraints, edge cases, hints, the Python concepts involved, stretch
goals and (from level 07) a target time/space complexity. Each challenge has an
empty test file waiting for your tests.

## Requirements

- Python 3.10 or newer (developed with 3.12)
- Dev dependencies, installed into the virtual environment by the setup below:
  - [pytest](https://docs.pytest.org/): the test runner
  - [pytest-cov](https://pytest-cov.readthedocs.io/): coverage reports

There are no runtime dependencies. Every challenge uses only the standard library.

## Setup

The `.venv` virtual environment is already created with everything installed.
Activate it in each new terminal:

```bash
source .venv/bin/activate
```

To rebuild it from scratch (e.g. on a new machine):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"
```

`pip install -e .` installs the `challenges` package in *editable* mode, so
edits to your solutions are picked up immediately without reinstalling.

### VS Code

`.vscode/settings.json` points VS Code at `.venv` and enables pytest. Open the
**Testing** panel (the flask icon) to run or debug individual tests with one
click. If tests don't show up, run **Python: Select Interpreter** and choose
`.venv`.

## Workflow for each challenge

1. **Read** the level overview in its `__init__.py`, then the challenge, e.g.
   `challenges/level01_basics/ex01_greet.py`.
2. **Write tests** in the matching file,
   `tests/challenges/level01_basics/test_ex01_greet.py`. Use the "EXAMPLES" and
   "EDGE CASES TO TEST" sections for ideas. Each test file already imports the
   code under test and includes commented-out examples to get you started.
3. **Run the tests and watch them fail** (red). Before you implement anything,
   tests fail with `NotImplementedError`, which is expected:
   `pytest tests/challenges/level01_basics/test_ex01_greet.py -v`
4. **Implement** the function until your tests pass (green).
5. **Refactor**, then try the stretch goals.

Try not to peek at the HINTS section until you've been stuck for a while.

### Useful pytest commands

```bash
pytest                                     # everything
pytest tests/challenges/level02_strings    # one level
pytest -k anagram -v                       # tests whose name matches "anagram"
pytest -x                                  # stop at the first failure
pytest --lf                                # re-run only the tests that failed last time
pytest --cov=challenges --cov-report=term-missing   # coverage, with uncovered lines
```

> A fresh checkout reports `no tests ran` (exit code 5) because the test files
> contain only commented-out examples. That changes once you write tests.

### pytest tips for these challenges

- **Many cases, one test:** `@pytest.mark.parametrize("n, expected", [(1, ...), (2, ...)])`
- **Expected exceptions:** `with pytest.raises(ValueError): ...`
- **Floats:** `assert result == pytest.approx(98.6)` instead of `==`
- **Order doesn't matter:** compare `sorted(result) == sorted(expected)`
  (the docblock says when this applies)

## Structure

```text
pyper/
├── challenges/
│   ├── common/
│   │   └── structures.py          ListNode / TreeNode + builders (already implemented)
│   ├── level01_basics/
│   │   ├── __init__.py            level overview: concepts covered
│   │   ├── ex01_greet.py          challenge stub + docblock
│   │   └── ...
│   └── level02_strings/ ... level12_algorithms/
├── tests/
│   └── challenges/
│       ├── level01_basics/
│       │   ├── test_ex01_greet.py your tests go here
│       │   └── ...
│       └── ...
├── .vscode/                       editor settings (interpreter + pytest)
├── pyproject.toml                 project metadata, dev dependencies, pytest config
└── README.md
```

### Linked-list and tree helpers

Levels 10 and 11 use `challenges/common/structures.py`, which is already
implemented, to build inputs and check outputs:

```python
from challenges.common.structures import list_to_linked, linked_to_list, build_tree, tree_to_list

head = list_to_linked([1, 2, 3])              # 1 -> 2 -> 3
assert linked_to_list(head) == [1, 2, 3]

root = build_tree([3, 9, 20, None, None, 15, 7])   # LeetCode-style level order
assert tree_to_list(root) == [3, 9, 20, None, None, 15, 7]
```

## Curriculum

| Level | Topic | Challenges |
| --- | --- | --- |
| 01 | **Basics**: arithmetic, conditionals, loops, functions | greet, even_or_odd, fizzbuzz, temperature_conversion, leap_year, sum_of_multiples, factorial, grade_calculator |
| 02 | **Strings** | reverse_string, valid_palindrome, count_vowels, title_case, valid_anagram, caesar_cipher, run_length_encoding, longest_common_prefix |
| 03 | **Lists** | find_max, remove_duplicates, rotate_list, second_largest, chunk_list, merge_sorted_lists, move_zeroes, running_sum |
| 04 | **Dicts & sets** | word_frequency, two_sum, first_unique_character, contains_duplicate, intersection_of_arrays, invert_dictionary, group_anagrams, roman_to_integer |
| 05 | **Functions**: comprehensions, `*args`, closures, generators, decorators | apply_to_all, comprehensions, flexible_sum, compose, make_counter, fibonacci_generator, memoize, count_calls |
| 06 | **Errors & parsing** | safe_divide, parse_int_list, validate_password, parse_config, parse_duration, custom_exceptions, parse_csv_line |
| 07 | **Recursion** | sum_digits, power, flatten_nested, tower_of_hanoi, subsets, permutations, generate_parentheses |
| 08 | **Classes & OOP** | bank_account, rectangle, stack, queue_with_stacks, shapes_inheritance, vector, inventory |
| 09 | **Searching & sorting** | linear_search, binary_search, bubble_sort, insertion_sort, merge_sort, quick_sort, search_insert_position, find_min_rotated |
| 10 | **Data structures**: stacks, linked lists, heaps, caches | valid_parentheses, reverse_linked_list, merge_two_sorted_lists, linked_list_cycle, min_stack, kth_largest, top_k_frequent, lru_cache |
| 11 | **Trees & graphs**: DFS, BFS, topological sort | max_depth, invert_tree, level_order, validate_bst, lowest_common_ancestor_bst, number_of_islands, course_schedule, shortest_path_binary_matrix |
| 12 | **Algorithms**: two pointers, sliding window, dynamic programming | best_time_to_buy_sell_stock, container_with_most_water, three_sum, longest_substring_without_repeating, maximum_subarray, climbing_stairs, coin_change, longest_increasing_subsequence, edit_distance |

Work through the levels in order, since later levels assume earlier concepts.
Within a level, challenges get harder as the numbers go up.

## Tracking progress

Tick off challenges as you finish them:

- [ ] Level 01: Basics (0/8)
- [ ] Level 02: Strings (0/8)
- [ ] Level 03: Lists (0/8)
- [ ] Level 04: Dicts & sets (0/8)
- [ ] Level 05: Functions (0/8)
- [ ] Level 06: Errors & parsing (0/7)
- [ ] Level 07: Recursion (0/7)
- [ ] Level 08: Classes & OOP (0/7)
- [ ] Level 09: Searching & sorting (0/8)
- [ ] Level 10: Data structures (0/8)
- [ ] Level 11: Trees & graphs (0/8)
- [ ] Level 12: Algorithms (0/9)

## Contributing

This is a personal learning repo, so it isn't looking for solved-challenge
pull requests. Bug reports (a wrong example, an ambiguous spec) and proposals
for new challenges are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE) © Jerome Thayananthajothy
