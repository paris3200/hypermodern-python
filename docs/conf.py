"""Sphinx configuration."""
import os
import sys

sys.path.insert(0, os.path.abspath("../src/"))

project = "hivetool"
author = "Jason Paris"
copyright = f"2021, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
