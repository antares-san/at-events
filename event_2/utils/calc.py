""" My calc functions """

def segment_len(point_a: float, point_b: float) -> float:
    """
    Returns the length of the segment defined by point A and B

    Parameters:
        point_a : point A
        point_b : point B
    Return value:
        Length of the segment
    """
    return abs(point_b - point_a)


def is_triangle(a: float, b :float, c : float) -> bool:
    """
    Returns True if there is a triangle with the specified segments.
    Otherwise, the function returns False

    Parameters:
            a : segment a
            b : segment b
            c : segment c
    Return value:
            True if there is a triangle
            False if a triangle doesn't exist
    """
    if a <= 0 or c <= 0 or b <= 0:
        return False
    else:
        return a + b > c and a + c > b and b + c > a

