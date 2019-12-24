def no_space(x: str) -> str:
    """
    入力されたxからスペースを除去した文字列を返却する
    :param x: スペースを含む文字列
    :return: スペースを除いた文字列
    """
    return "".join(x.split())
