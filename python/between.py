import numpy as np
from typing import List


def between(a: int, b: int) -> List[int]:
    """
    aから始まりbまで1ずつ増えていく配列を作る
    :param a: スタートの数
    :param b: ゴールの数
    :return: aからbへずつ増加する等差数列のリスト
    """
    return list(np.arange(a, b+1, 1))

"""
def between(a, b):
    return range(a, b+1)
"""