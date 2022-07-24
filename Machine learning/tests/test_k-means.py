import unittest
import numpy
import os
import pickle
import os
os.path.insert(0 , '../')
from scripts import KMeans

_DATA_DIR = os.path.dirname(os.path.realpath(__file__)) + "/data"


def get_feature_map():
    with open(f"{_DATA_DIR}/kmeans.pickle", "rb") as handle:
        return pickle.load(handle)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        k = 1
        actual = KMeans.get_k_means(get_feature_map(), 4, k)
        expected = [[-1.0659, -1.0981, -1.0667, -1.0846]]
        self.assertEqual(round_output_values(actual), expected)

    def test_case_2(self):
        k = 2
        actual = KMeans.get_k_means(get_feature_map(), 4, k)
        expected = [
            [0.3109, 0.3282, 0.3325, 0.3437],
            [-1.479, -1.526, -1.4864, -1.5131],
        ]
        self.assertEqual(round_output_values(actual), expected)

    def test_case_3(self):
        k = 3
        actual = KMeans.get_k_means(get_feature_map(), 4, k)
        expected = [
            [0.3109, 0.3282, 0.3325, 0.3437],
            [-1.1271, -1.6013, -1.4669, -1.5284],
            [-1.7739, -1.4629, -1.5028, -1.5004],
        ]
        self.assertEqual(round_output_values(actual), expected)

    def test_case_4(self):
        k = 4
        actual = KMeans.get_k_means(get_feature_map(), 4, k)
        expected = [
            [-1.2694, -1.5202, -1.1358, -1.5602],
            [-1.2249, -1.6868, -1.8245, -1.3984],
            [-1.8371, -1.4109, -1.5173, -1.5607],
            [0.3109, 0.3282, 0.3325, 0.3437],
        ]
        self.assertEqual(round_output_values(actual), expected)

    def test_case_5(self):
        k = 5
        actual = KMeans.get_k_means(get_feature_map(), 4, k)
        expected = [
            [-1.1544, -1.4444, -1.1587, -1.6412],
            [-1.251, -1.7981, -1.7665, -1.3378],
            [-1.6647, -1.2963, -1.8271, -1.6676],
            [0.3109, 0.3282, 0.3325, 0.3437],
            [-1.8224, -1.5567, -1.1926, -1.4176],
        ]
        self.assertEqual(round_output_values(actual), expected)


def round_output_values(centroids):
    if type(centroids) is not list:
        # Bad output; let tests fail.
        return centroids

    return [[round_to_4(x) for x in centroid] for centroid in centroids]


def round_to_4(number):
    if not is_number(number):
        # Bad output; let tests fail.
        return number

    return round(number, 4)


def is_number(element):
    return type(element) in (int, float, numpy.float64)
