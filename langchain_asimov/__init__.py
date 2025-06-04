# This is free and unencumbered software released into the public domain.

"""ASIMOV for LangChain."""

from ._version import __version__, __version_tuple__
from .document_loaders import AsimovLoader
from .errors import AsimovModuleNotFound

__all__ = [
    'AsimovLoader',
    'AsimovModuleNotFound',
    '__version__',
    '__version_tuple__',
]
