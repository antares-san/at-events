""" My output functions """

def format_card(title: str, **kwargs) -> str:
    """
    Returns formatted text with data

    Parameters:
        title :
        kwargs :
    Return value:
    """
    formatted_card = f'\n==== {title}: ===='
    for name, value in kwargs.items():
        formatted_card += f'\n --> {name}: {value}'
    return formatted_card


def format_list(*args, title ='My list', ) -> str:
    """
    Returns formatted list of persons

    Parameters:
        title :
        args :
    Return value:
    """
    formatted_persons = f'\n==== {title} ===='
    for name in args:
        formatted_persons += f'\n*** {name} ***'
    return formatted_persons

