from typing import List


def sum_mix(arr: List[any]) -> int:
    """
    intとstrを含むListの総和を求める
    :param arr: List[any]
    :return: int
    """
    return sum([int(i) for i in arr])


"""
[]はいらないsum(int(i) for i in arr)でよかった
"""
