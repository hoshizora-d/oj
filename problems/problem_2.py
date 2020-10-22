from typing import Tuple, List, Dict, Any
import numpy as np
import cv2
from oj import problem, special_judge, special_data_generator


@problem()
class FillCircleAA:
    """Fill a circle([center],[radius]) with color 255 for the input grayscale [image].

    Notice:
        Edge should be processed with anti-aliasing.
    """

    def solve(self, image: np.ndarray, center: Tuple[int, int], radius: int) -> np.ndarray:
        raise NotImplementedError

    @special_data_generator
    def generate_cases(self) -> Tuple[List, Dict, Any]:
        def solution(img, o, r):
            scaling = 16
            h, w = img.shape
            expected = np.zeros((h*scaling, w*scaling), np.uint8)
            cv2.circle(expected, tuple(map(int, [(o[0]+0.5)*scaling-0.5, (o[1]+0.5)*scaling-0.5])), int(r*scaling), 255, -1)
            expected = cv2.resize(expected, None, fx=1/scaling, fy=1/scaling, interpolation=cv2.INTER_AREA)
            return expected

        example_args = [
            (np.zeros((5, 5), np.uint8), (2, 2), 2),
            (np.zeros((3, 3), np.uint8), (2, 2), 2),
            (np.zeros((999, 999), np.uint8), (499, 499), 500),
            (np.zeros((999, 999), np.uint8), (499, 499), 5),
            (np.zeros((999, 999), np.uint8), (499.2, 499.8), 499),
        ]
        for args in example_args:
            yield args, {}, solution(*args)

    @special_judge
    def judge(self, expected: np.ndarray, answer: np.ndarray):
        diff = abs(expected.astype(int)-answer.astype(int))
        return (diff < 32).all()
