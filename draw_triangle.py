"""KT Cycle exercise solution by Anne-Riin"""


def draw_triangle(height):
    """
    "Draw a triangle iteratively with asterisks (*).

    The triangle must be equilateral, and the input is the number of rows. The last row must not be empty.
    Note: Recursion should not be used!"
    :param height:
    :return: triangle
    """
    result = ""
    for i in range(1, height + 1):
        result += " " * (height - i)
        result += "*" * (2 * i - 1)
        result += "\n"
    return result[:-1]


print(draw_triangle(-1))
