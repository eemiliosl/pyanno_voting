import unittest
import numpy as np

from pyanno import voting
from pyanno.voting import MISSING_VALUE as MV
from pyanno.voting import PyannoValueError
from numpy.testing import assert_array_equal, assert_array_almost_equal


class TestVoting(unittest.TestCase):

    def test_labels_count(self):
        annotations = [
            [1,  2, MV, MV],
            [MV, MV,  3,  3],
            [MV,  1,  3,  1],
            [MV, MV, MV, MV],
        ]
        nclasses = 5
        expected = [0, 3, 1, 3, 0]
        result = voting.labels_count(annotations, nclasses)
        self.assertEqual(result, expected)

    def test_majority_vote(self):
        annotations = [
            [1, 2, 2, MV],
            [2, 2, 2, 2],
            [1, 1, 3, 3],
            [1, 3, 3, 2],
            [MV, 2, 3, 1],
            [MV, MV, MV, 3],
        ]
        expected = [2, 2, 1, 3, 1, 3]
        result = voting.majority_vote(annotations)
        self.assertEqual(expected, result)

    def test_majority_vote_empty_item(self):
        # Bug: majority vote with row of invalid annotations fails
        annotations = np.array(
            [[1, 2, 3],
             [MV, MV, MV],
             [1, 2, 2]]
        )
        expected = [1, MV, 2]
        result = voting.majority_vote(annotations)
        self.assertEqual(expected, result)

    def test_one_plus_two(self):
        self.assertEqual(3, 2 + 1, "not good !")

    def test_add_floats(self):
        self.assertAlmostEqual(3.3, 1.1 + 2.2, 10)

    def test_add_arrays(self):
        x = np.array([1, 1])
        y = np.array([2, 2])
        z = np.array([3, 3]) 
        assert_array_equal(x + y, z)

    def test_labels_frequency(self):
        result = voting.labels_frequency([[1, 1, 2], [-1, 1, 2]], 4)
        expected = np.asarray([ 0. ,  0.6,  0.4,  0. ])
        assert_array_almost_equal(result, expected)

    def test_exception_all_missing(self):
        with self.assertRaises(PyannoValueError):
            result = voting.labels_frequency([[MV, MV, MV], [MV, MV, MV]], 4)

    def test_exception_empty_list(self):
        with self.assertRaises(PyannoValueError):
            result = voting.labels_frequency([], 4)

    def test_optional_missing_value_labels_count(self):
        mv = -99
        result = voting.labels_count([[1, 1, 2], [mv, 1, 2]], 4, mv)
        expected = np.asarray([ 0. ,  3,  2,  0. ])
        assert_array_almost_equal(result, expected)

    def test_optional_missing_value_majority_vote(self):
        mv = -99
        annotations = [
            [1, 2, 2, mv],
            [2, 2, 2, 2],
            [1, 1, 3, 3],
            [1, 3, 3, 2],
            [mv, 2, 3, 1],
            [mv, mv, mv, 3],
        ]
        expected = [2, 2, 1, 3, 1, 3]
        result = voting.majority_vote(annotations, mv)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
