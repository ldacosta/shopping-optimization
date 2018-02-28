# -*- coding: utf-8 -*-
"""A physical place.

Example:

Attributes:

Todo:
    * Nothing for now.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
from geometry.angle import AngleInRadians


class Place(object):

    def __init__(self, latitude: AngleInRadians, longitude: AngleInRadians):
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, latitude: AngleInRadians, longitude: AngleInRadians) -> float:
        """Distance in Kms."""

        # TODO: try https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude ?
        raise NotImplementedError()