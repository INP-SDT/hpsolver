# -*- coding: utf-8 -*-
"""HPS-Geometry-Data.
"""
import numpy as np
from hpsolver.hps import hpsdata


class HPSGeom(hpsdata.HPSData):
    """HPS-Geometry data.

    - Derived from `HPSData`.
    - Contains no body.

    """

    def new_body_west(self):
        return None

    def new_body_east(self):
        return None

    def new_body_join(self, west_data, east_data):

        if west_data.body is None:
            return None

        if east_data.body is None:
            return None

        return None

    def make_sol(self):
        self.body = None

    def mat_from_body(self):

        keys = [
            'a11', 'a12', 'a21', 'a22'
        ]

        return {
            k: np.zeros(self.SIZE) for k in keys
        }

    def vec_from_body(self):

        return {
            k: np.zeros(self.SIZE) for k in ['b_1', 'b_2']
        }
