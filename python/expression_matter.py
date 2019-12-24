def expression_matter(a: int, b: int, c: int) -> int:
    """
    a,b,cの3つの数値と+,*,()を使って計算結果が最大となるものを求める
    :param a: int
    :param b: int
    :param c: int
    :return: int
    """
    pattern = [a + b + c, (a + b) * c, a * b * c, a * (b + c)]
    return max(pattern)
