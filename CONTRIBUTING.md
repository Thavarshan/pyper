# Contributing

This is a personal learning repo: a set of coding-challenge stubs the owner is
solving to learn Python. It isn't looking for solution pull requests, since
that would spoil the exercise for anyone else using it the same way.

Contributions that are welcome:

- **Bug reports** — a wrong example output, a contradiction between a
  challenge's docblock sections, an ambiguous spec, or a broken test stub.
  Please open an [issue](https://github.com/Thavarshan/pyper/issues) with the
  file path and what's wrong.
- **New challenges** — if you'd like to propose an additional challenge
  (same format: docblock stub + empty test file, no solution), open an issue
  first to discuss where it fits in the curriculum.
- **Tooling fixes** — pytest config, CI, editor config, docs.

Please do **not** open a pull request containing a solved challenge (a
function body that isn't `raise NotImplementedError`).

## Development setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Style

Each challenge file follows a fixed docblock structure (see any file under
`challenges/level03_lists/ex03_rotate_list.py` for the template): YOUR TASK,
an optional background section, THE RULES, EXAMPLES, COMPLEXITY TARGET (from
level 07 onward), EDGE CASES TO TEST, HINTS, PYTHON CONCEPTS TO LEARN and
STRETCH GOALS. The audience is a Python beginner: use short sentences, explain
jargon the first time it appears, and give each example a one-line "why".
Please match it if you're proposing a new one.
