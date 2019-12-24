def mouth_size(animal: str) -> str:
    """
    animal=alligatorの場合はsmallを返す。
    それ以外はwideを返す
    :param animal: str
    :return: str (wide/small)
    """
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"


"""
def mouth_size(animal): 
    return 'small' if animal.lower() == 'alligator' else 'wide'
"""
