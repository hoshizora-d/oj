from typing import Tuple, List, Dict, Any
import numpy as np
import cv2
from oj import problem, special_judge, special_data_generator


@problem
class DrawLine:
    """Draw a line from [pt1] to [pt2]. Line width should be 1 and color is 255 for the input grayscale [image].
    """

    def solve(self, image: np.ndarray, pt1: Tuple[float, float], pt2: Tuple[float, float]) -> np.ndarray:
        raise NotImplementedError

    @special_data_generator
    def generate_cases(self) -> Tuple[List, Dict, Any]:
        def solution(img, pt1, pt2):
            scaling = 16
            ret = cv2.resize(img, None, fx=scaling, fy=scaling)
            cv2.line(ret, tuple(pt1*scaling), tuple(pt2*scaling), 255, 1*scaling)
            return cv2.resize(ret, None, fx=1/scaling, fy=1/scaling, interpolation=cv2.INTER_AREA)

        example_args = np.zeros((5, 5), np.uint8), np.array([1, 2]), np.array([4, 4])
        yield example_args, {}, solution(*example_args)

        img_size = 300
        n_sample = 10
        np.random.seed(0)
        pts = (np.random.rand(n_sample*2, 2)*img_size).astype(int)
        pts1 = pts[:n_sample]
        pts2 = pts[n_sample:]
        for pt1, pt2 in zip(pts1, pts2):
            img = np.zeros((img_size, img_size), np.uint8)
            args = img, pt1, pt2
            yield args, {}, solution(*args)

    @ special_judge
    def judge(self, expected: np.ndarray, answer: np.ndarray):
        kernel = np.ones((3, 3), np.uint8)
        diff = abs(expected.astype(int) - answer.astype(int)).astype(np.uint8)
        filtered = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)
        score = 1 - diff.sum()/answer.sum()
        return filtered.sum() == 0 and score >= 0.8
