def sum_str(a: str, b: str) -> str:
    """
    strの数字同士を足し合わせてstrで返す
    :param a: str
    :param b: str
    :return: str
    """
    return str(int(a.strip() or 0) + int(b.strip() or 0))
