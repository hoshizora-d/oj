import os
from typing import List, Tuple, Dict, Any
from oj.backend.data import JsonDataGenerator


class Problem:
    __test__ = False
    __data__ = "./"
    __title__ = None

    def test_all(self):
        for args, kwargs, ret in self.generate_cases():
            assert self.judge(ret, self.solve(*args, **kwargs))

    def generate_cases(self) -> Tuple[List, Dict, Any]:
        root = os.path.join(self.__data__, self.__title__)
        input_gen = JsonDataGenerator(root, ".in.json")
        output_gen = JsonDataGenerator(root, ".out.json")
        for (args, kwargs), ret in zip(input_gen, output_gen):
            yield args, kwargs, ret

    def solve(self, *args, **kwargs):
        raise NotImplementedError

    def judge(self, expected, answer):
        return expected == answer
