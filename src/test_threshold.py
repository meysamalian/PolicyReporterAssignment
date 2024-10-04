import unittest
from threshold import DataPoint,ThresholdFinder

class TestDataPoint(unittest.TestCase):
    def test_recall(self):
        # Test recall calculation with normal values
        data_point = DataPoint(0.1, 50, 30, 20, 5)
        self.assertEqual(data_point.recall(), 50 / (50 + 5))

        # Test recall calculation when tp and fn are zero
        data_point = DataPoint(0.1, 0, 30, 20, 0)
        self.assertEqual(data_point.recall(), 0)

        # Test recall calculation when tp is zero and fn is not zero
        data_point = DataPoint(0.1, 0, 30, 20, 5)
        self.assertEqual(data_point.recall(), 0)

        # Test recall calculation when tp is not zero and fn is zero
        data_point = DataPoint(0.1, 50, 30, 20, 0)
        self.assertEqual(data_point.recall(), 1)


class TestThresholdFinder(unittest.TestCase):
    def test_best_threshold(self):
        # Test best_threshold with normal values
        data_points = [
            DataPoint(0.1, 50, 30, 20, 5),
            DataPoint(0.2, 48, 32, 18, 6),
            DataPoint(0.3, 46, 33, 15, 8),
            DataPoint(0.4, 44, 35, 12, 9),
            DataPoint(0.5, 42, 36, 10, 10),
            DataPoint(0.6, 40, 38, 10, 11),
            DataPoint(0.7, 38, 39, 6, 12),
            DataPoint(0.8, 36, 40, 4, 13),
            DataPoint(0.9, 34, 41, 2, 14),
        ]
        finder = ThresholdFinder(data_points)
        self.assertEqual(finder.best_threshold(), 0.1)

        # Test best_threshold when no threshold gives a recall of at least 0.9
        data_points = [
            DataPoint(0.1, 40, 30, 20, 15),
            DataPoint(0.2, 38, 32, 18, 16),
            DataPoint(0.3, 36, 33, 15, 18),
            DataPoint(0.4, 34, 35, 12, 19),
            DataPoint(0.5, 32, 36, 10, 20),
            DataPoint(0.6, 30, 38, 10, 21),
            DataPoint(0.7, 28, 39, 6, 22),
            DataPoint(0.8, 26, 40, 4, 23),
            DataPoint(0.9, 24, 41, 2, 24),
        ]
        finder = ThresholdFinder(data_points)
        self.assertIsNone(finder.best_threshold())

        # Test best_threshold when all thresholds give a recall of at least 0.9
        data_points = [
            DataPoint(0.1, 50, 30, 20, 5),
            DataPoint(0.2, 52, 32, 18, 4),
            DataPoint(0.3, 54, 33, 15, 3),
            DataPoint(0.4, 56, 35, 12, 2),
            DataPoint(0.5, 58, 36, 10, 1),
            DataPoint(0.6, 60, 38, 10, 0),
            DataPoint(0.7, 62, 39, 6, 0),
            DataPoint(0.8, 64, 40, 4, 0),
            DataPoint(0.9, 66, 41, 2, 0),
        ]
        finder = ThresholdFinder(data_points)
        self.assertEqual(finder.best_threshold(), 0.1)
    
    def test_best_threshold_with_empty_data_points(self):
        # Test best_threshold when data_points is an empty list
        data_points = []
        finder = ThresholdFinder(data_points)
        self.assertIsNone(finder.best_threshold())

if __name__ == '__main__':
    unittest.main()