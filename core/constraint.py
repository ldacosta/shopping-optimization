# -*- coding: utf-8 -*-
"""'Constraint' definition(s).

Example:

Attributes:

Todo:
    * Nothing for now.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
from enum import Flag, auto


class Constraint(Flag):
    """Constraints when solving the problem."""
    TIME = auto()
    COST = auto()
    TIME_AND_COST = TIME & COST