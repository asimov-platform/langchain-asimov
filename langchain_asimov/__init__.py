# This is free and unencumbered software released into the public domain.

from ._version import __version__, __version_tuple__
from .document_loaders import AsimovLoader

__all__ = ['AsimovLoader', '__version__', '__version_tuple__']
