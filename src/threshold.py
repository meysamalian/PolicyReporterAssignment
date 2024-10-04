# The DataPoint class represents a single data point in our dataset.
class DataPoint:
    # The constructor initializes the data point with the given threshold, true positives (tp), true negatives (tn), false positives (fp), and false negatives (fn).
    def __init__(self, threshold, tp, tn, fp, fn):
        self.threshold = threshold
        self.tp = tp
        self.tn = tn
        self.fp = fp
        self.fn = fn

    # The recall method calculates the recall for this data point, which is defined as tp / (tp + fn).
    def recall(self):
          if self.tp == 0 and self.fn == 0:
             return 0
          return self.tp / (self.tp + self.fn)

# The ThresholdFinder class is used to find the best threshold from a list of data points.
class ThresholdFinder:
    # The constructor initializes the ThresholdFinder with the given list of data points.
    def __init__(self, data_points):
        self.data_points = data_points

    # The best_threshold method finds and returns the best threshold from the data points.
    # The best threshold is defined as the smallest threshold that gives a recall of at least 0.9.
    # If no such threshold is found, it returns None.
    def best_threshold(self):
        best_threshold = None
        for data_point in self.data_points:
            if data_point.recall() >= 0.9:
                if best_threshold is None or data_point.threshold < best_threshold:
                    best_threshold = data_point.threshold
        return best_threshold


# Create a list of data points.
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

# Create an instance of ThresholdFinder with the list of data points.
finder = ThresholdFinder(data_points)

# Find and print the best threshold.
# If no threshold is found with a recall of at least 0.9, print a message indicating this.
if finder is not None:
    print(finder.best_threshold())
else:
    print("No threshold found with recall >= 0.9")