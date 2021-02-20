import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal

from pyro_risks.models import check_xy, check_x, discretizer


class UtilsTester(unittest.TestCase):
    def test_check_xy(self):
        self.assertRaises(
            TypeError, check_xy, np.array([[0, 0, 0], [0, 0, 0]]), np.array([0, 1])
        )

    def test_check_x(self):
        self.assertRaises(
            TypeError, check_x, np.array([[0, 0, 0], [0, 0, 0]]), np.array([0, 1])
        )

    def test_discretizer(self):
        self.assertEqual(discretizer(5), 1)
        self.assertEqual(discretizer(0), 0)


if __name__ == "__main__":
    unittest.main()
