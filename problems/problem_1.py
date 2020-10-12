from typing import Tuple, List, Dict, Any
import numpy as np
import cv2
from oj import problem, special_judge, special_data_generator


@problem
class FillCircle:
    """Fill a circle([center],[radius]) with color 255 for the input grayscale [image].

    Notice:
        Coordinate system example. x:[0,4] y:[0,5] for image:[4,3]
    """

    def solve(self, image: np.ndarray, center: Tuple[float, float], radius: float) -> np.ndarray:
        raise NotImplementedError

    @special_data_generator
    def generate_cases(self) -> Tuple[List, Dict, Any]:
        def solution(img, o, r):
            result = img.copy()
            cv2.circle(result, tuple(map(int, o)), int(r), 255, -1)
            return result

        example_args = [
            (np.zeros((4, 4), np.uint8), (2.5, 2.5), 2),
            (np.zeros((4, 3), np.uint8), (2.5, 2.5), 2),
            (np.zeros((999, 999), np.uint8), (499.5, 499.5), 500),
            (np.zeros((999, 999), np.uint8), (499.5, 499.5), 5),
        ]
        for args in example_args:
            yield args, {}, solution(*args)

    @special_judge
    def judge(self, expected: np.ndarray, answer: np.ndarray):
        np.testing.assert_array_equal(expected, answer)
        return True
