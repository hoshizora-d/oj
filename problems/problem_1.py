from typing import Tuple, List, Dict, Any
import numpy as np
import cv2
from oj import problem, special_judge, special_data_generator


@problem
class DrawLine:
    @special_data_generator
    def generate_cases(self) -> Tuple[List, Dict, Any]:
        img_size = 100
        n_sample = 10
        np.random.seed(0)
        pts = (np.random.rand(n_sample*2, 2)*img_size-img_size/2).astype(int)
        pts1 = pts[:n_sample]
        pts2 = pts[n_sample:]
        for pt1, pt2 in zip(pts1, pts2):
            img = np.zeros((img_size, img_size), np.uint8)
            args = img, pt1, pt2
            ret = img.copy()
            cv2.line(ret, tuple(pt1), tuple(pt2), 1, 255)
            yield args, {}, ret

    @special_judge
    def judge(self, expected: np.ndarray, answer: np.ndarray):
        kernel = np.ones((3, 3), np.uint8)
        diff = abs(expected.astype(int) - answer.astype(int)).astype(np.uint8)
        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)
        return diff.sum() == 0

    def solve(self, img: np.ndarray, pt1: Tuple[float, float], pt2: Tuple[float, float]) -> np.ndarray:
        cv2.line(img, tuple(pt1), tuple(pt2), 1, 255)
        return img
