import unittest
from main import get_spiral_elements


class TestGetSpiralElements(unittest.TestCase):

    def test_number_of_elements_for_matrix_in_data_is_more_than_width_mul_height(self):
        try:
            get_spiral_elements(3, 2, [10])
        except AssertionError:
            self.assertTrue(True)
        except Exception:
            raise Exception, 'Unhandled error if number of elements is more than width*height'

    def test_number_of_elements_for_matrix_in_data_is_less_than_width_mul_height(self):
        try:
            get_spiral_elements(3, 2, [10])
        except AssertionError:
            self.assertTrue(True)
        except Exception:
            raise Exception, 'Unhandled error if number of elements is less than width*height'

    def test_rectangle_matrix_3x2(self):
        width = 3
        height = 2
        data = range(6)
        expectation = [0, 1, 2, 5, 4, 3]
        self.assertEqual(get_spiral_elements(width, height, data), expectation)

    def test_rectangle_matrix_2x3(self):
        width = 2
        height = 3
        data = range(6)
        expectation = [0, 1, 3, 5, 4, 2]
        self.assertEqual(get_spiral_elements(width, height, data), expectation)

    def test_only_1_element(self):
        width = height = 1
        data = [1]
        expectation = [1]
        self.assertEqual(get_spiral_elements(width, height, data), expectation)

    def test_square_matrix_2x2(self):
        width = height = 2
        data = range(1,5)
        expectation = [1,2,4,3]
        self.assertEqual(get_spiral_elements(width, height, data), expectation)

    def test_square_matrix_3x3(self):
        width = height = 3
        data = range(1,10)
        expectation = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(get_spiral_elements(width, height, data), expectation)



if __name__ == '__main__':
    unittest.main()
