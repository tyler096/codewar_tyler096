def apple(x: any) -> str:
    """
    xを2乗して、その数値が1000以上であれば、
    It's hotter than the sun!!を返却し、下回れば
    Help yourself to a honeycomb Yorkie for the glovebox.を返却する
    :param x: strかintで数字が与えらえる
    :return: xの計算結果によっていずれからの文字列を返却する。
    """
    if int(x) ** 2 > 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."
