# Python Package Tutorial

A simple Python package for string operations, created as a tutorial project.

## Features

- Reverse strings
- Count vowels in a string
- Capitalize words in a string

## Installation

You can install this package using pip (once published) or directly from source:

```bash
pip install .
```

## Usage

```python
from skander_package_tutorial.string_ops import reverse_string, count_vowels, capitalize_words

print(reverse_string("hello"))          # Output: olleh
print(count_vowels("hello world"))    # Output: 3
print(capitalize_words("hello world")) # Output: Hello World
```

## Documentation

The documentation is built using Sphinx. You can find the built HTML in the `docs/build/html` directory.

## GitHub Pages

This repository is configured to automatically build and deploy documentation to GitHub Pages via a GitHub Action. Every push to the `master` branch triggers the `documentation` workflow which:

1. Builds the Sphinx documentation.
2. Pushes the results to the `gh-pages` branch using `ghp-import`.
