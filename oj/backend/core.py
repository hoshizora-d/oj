import os
import time
from typing import List, Tuple, Dict, Any
from joblib import Parallel, delayed
from oj.backend.data import JsonDataGenerator


class Problem:
    __test__ = False
    __data__ = "./"
    __title__ = None
    __time_limit__ = 1000

    def test_all(self):
        max_time = 0
        for args, kwargs, expected in self.generate_cases():
            task = delayed(self.solve)(*args, **kwargs)
            now = time.process_time()
            answer = Parallel(-1, timeout=self.__time_limit__/1000)([task])[0]
            assert self.judge(expected, answer)
            max_time = max(time.process_time() - now, max_time)
        print(f"time: {max_time*1000:.0f}ms")

    def generate_cases(self) -> Tuple[List, Dict, Any]:
        root = os.path.join(self.__data__, self.__title__)
        input_gen = JsonDataGenerator(root, ".in.json")
        output_gen = JsonDataGenerator(root, ".out.json")
        for (args, kwargs), ret in zip(input_gen, output_gen):
            yield args, kwargs, ret

    def get_example(self, case: int = 0):
        it = self.generate_cases()
        for _ in range(case):
            next(it)
        return next(it)

    def solve(self, *args, **kwargs):
        raise NotImplementedError

    def judge(self, expected, answer):
        return expected == answer
