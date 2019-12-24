def century(year: int) -> int:
    """
    西暦年から世紀を計算する。
    :param year: int
    :return: int
    """
    return int((year - 1) / 100 + 1)


"""
def century(year: int) -> int:
    return (year-1)//100 + 1
"""
