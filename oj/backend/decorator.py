import configparser
from .core import Problem
config = configparser.ConfigParser()
config.read("oj.ini")


def problem(cls):
    """Append test feature
    
    Notice:
        Configure data path with [oj.ini]-[data]-[root]. 
    """
    class decorator_cls(cls, Problem):
        __test__ = True
        __data__ = config["data"]["root"]
        __title__ = cls.__name__

    return decorator_cls
