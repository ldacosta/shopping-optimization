# -*- coding: utf-8 -*-
"""Template for Solver.

Example:

Attributes:

Todo:
    * Nothing for now.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import abc
import collections

from typing import Set

from core.constraint import Constraint

Solution = collections.namedtuple('Solution', 'place items')

class Solver(abc.ABC):

    def __init__(self):
        pass

    def recommend(self, constraints: Set[Constraint]) -> Set[Solution]:
        """Issues recommendations given constraints."""
        raise RuntimeError("Abstract class, not callable.")


