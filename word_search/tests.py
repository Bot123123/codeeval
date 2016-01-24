import unittest
from main import get_result, search_start_positions

GRID = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]


class TestSearchStartPositions(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(search_start_positions(GRID, 'F'), [(1, 1)])

    def test_absent_letter(self):
        self.assertEqual(search_start_positions(GRID, 'Q'), [])

    def test_more_than_one_possible_positions(self):
        self.assertEqual(search_start_positions(GRID, 'A'), [(0, 0), (2, 0)])
        self.assertEqual(search_start_positions(GRID, 'C'), [(0, 2), (1, 2)])
        self.assertEqual(search_start_positions(GRID, 'E'), [(0, 3), (2, 2), (2, 3)])


class TestGetResult(unittest.TestCase):

    def test_positive_from_first_letter(self):
        self.assertEqual(get_result(GRID, 'ABCE'), True)
        self.assertEqual(get_result(GRID, 'ASA'), True)
        self.assertEqual(get_result(GRID, 'ASFC'), True)
        self.assertEqual(get_result(GRID, 'ASFCSEEDA'), True)

    def test_negative_from_first_letter(self):
        self.assertEqual(get_result(GRID, 'ABCEQ'), False)
        self.assertEqual(get_result(GRID, 'ASAW'), False)

    def test_negative_diagonale(self):
        self.assertEqual(get_result(GRID, 'AF'), False)
        self.assertEqual(get_result(GRID, 'FE'), False)

    def test_positive_one_letter(self):
        self.assertEqual(get_result(GRID, 'A'), True)
        self.assertEqual(get_result(GRID, 'C'), True)
        self.assertEqual(get_result(GRID, 'E'), True)

    def test_negative_one_letter(self):
        self.assertEqual(get_result(GRID, 'Q'), False)
        self.assertEqual(get_result(GRID, 'W'), False)

    def test_negative_already_used_letters(self):
        self.assertEqual(get_result(GRID, 'ABA'), False)
        self.assertEqual(get_result(GRID, 'FDF'), False)

    def test_more_than_one_way(self):
        self.assertEqual(get_result(GRID, 'CSEE'), True)
        self.assertEqual(get_result(GRID, 'CSEC'), True)
        self.assertEqual(get_result(GRID, 'SECB'), True)
        self.assertEqual(get_result(GRID, 'SEED'), True)
        self.assertEqual(get_result(GRID, 'SECC'), True)
