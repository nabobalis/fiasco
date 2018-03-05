"""
A Python interface to the CHIANTI atomic database
"""
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# ----------------------------------------------------------------------------
from ._sunpy_init import *
# ----------------------------------------------------------------------------

if not _ASTROPY_SETUP_:
    from .base import *
    from .ion import Ion
    from .collections import IonCollection
    from .element import Element

    from .util import setup_paths
    defaults = setup_paths()
