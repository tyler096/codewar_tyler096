def is_divisible(n: int, x: int, y: int) -> bool:
    """
    nをx,yの両方の数で割り切れるかを確認し、割り切れた場合はTrueを割り切れない場合はFalseを返す
    x,yの値は自然数
    :param n: 割られる数
    :param x: 割る数その1
    :param y: 割る数その2
    :return: Boolean
    """
    con = (n % x == 0) & (n % y == 0)
    return con
