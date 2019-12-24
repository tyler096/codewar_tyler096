def well(x):
    """
    リストの中身のgoodの数で3つの結果を返却する。
    goodが1or2 => Publish!
    good > 2 => I smell a series
    それ以外 => Fail!
    :param x: goodとbadを含むリスト
    :return: Fail/Publish!/I smell a series!
    """
    num = x.count("good")
    if num > 0:
        if num <= 2:
            return "Publish!"
        else:
            return "I smell a series!"
    else:
        return "Fail!"


"""
    num = x.count('good')
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
"""
