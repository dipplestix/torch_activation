import os
import sys
from torch_activation import __version__
sys.path.insert(0, os.path.abspath("../"))

# Configuration file for the Sphinx documentation builder.

project = "Torch Activation"
copyright = "2024, Alan Huynh"
author = "Alan Huynh"
release = __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# HTML output configuration
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "logo.png"
html_theme_options = {
    "logo_only": True,
}
