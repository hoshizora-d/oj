from typing import Tuple, List, Dict, Any
import numpy as np
import cv2
from oj import problem, special_judge, special_data_generator


@problem()
class FillTriangleAA:
    """Fill a triangle with color 255 for the input grayscale [image].

    Notice:
        Edge should be processed with anti-aliasing.
    """

    def solve(self, image: np.ndarray, pt1: Tuple[float, float], pt2: Tuple[float, float], pt3: Tuple[float, float]) -> np.ndarray:
        raise NotImplementedError

    @special_data_generator
    def generate_cases(self) -> Tuple[List, Dict, Any]:
        def solution(img, pt1, pt2, pt3):
            scaling = 16
            h, w = img.shape
            pts = np.array([pt1, pt2, pt3])
            expected = np.zeros((h*scaling, w*scaling), np.uint8)
            cv2.fillConvexPoly(expected, ((pts+0.5)*scaling-0.5).astype(int), 255)
            expected = cv2.resize(expected, None, fx=1/scaling, fy=1/scaling)
            return expected

        example_args = [
            (np.zeros((5, 5), np.uint8), (0, 1), (3, 3), (5, 1)),
            (np.zeros((10, 10), np.uint8), (1, 1), (10, 10), (2, 8)),
            (np.zeros((999, 999), np.uint8), (0, 1), (3, 3), (5, 1)),
            (np.zeros((999, 999), np.uint8), (0, 0), (0, 998), (998, 998)),
            (np.zeros((999, 999), np.uint8), (0.2, 0.8), (0, 998), (998.2, 998.8)),
        ]
        for args in example_args:
            yield args, {}, solution(*args)

    @special_judge
    def judge(self, expected: np.ndarray, answer: np.ndarray):
        diff = abs(expected.astype(int)-answer.astype(int))
        return (diff < 32).all()
