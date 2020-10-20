import os
import glob
import json
from typing import Tuple, List, Dict


class FileDataGenerator:
    """Generate data of a problem.
    
    Notice:
        The files follows the rule: [root]/[index][ext]
    """

    def __init__(self, root: str, ext: str, index_func=lambda x: int(os.path.basename(x).split(".")[0])):
        paths = glob.glob(os.path.join(root, "*" + ext))
        self.paths = sorted(paths, key=index_func)

    def __iter__(self) -> Tuple[List, Dict]:
        raise NotImplementedError


class JsonDataGenerator(FileDataGenerator):
    def __iter__(self) -> Tuple[List, Dict]:
        for path in self.paths:
            with open(path, "r") as fp:
                obj = json.load(fp)
                if isinstance(obj, List):
                    yield obj, {}
                elif isinstance(obj, Dict):
                    yield [], obj
                else:
                    yield obj
