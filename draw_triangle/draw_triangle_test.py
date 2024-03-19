"""Tests for method draw_triangle"""

import pytest

from draw_triangle import draw_triangle


@pytest.mark.parametrize("height, expected", [
    (1, "*"),
    (3, "  *\n ***\n*****"),
    (5, "    *\n   ***\n  *****\n *******\n*********"),
    (0, ""),
    (2, " *\n***"),
    (10,
     "*\n        ***\n       *****\n      *******\n     *********\n    ***********\n   *************\n  "
     "***************\n *****************\n*******************"),
    (7, "      *\n     ***\n    *****\n   *******\n  *********\n ***********\n*************"),
    (4, "   *\n  ***\n *****\n*******"),
])
def test_draw_triangle(height, expected):
    assert draw_triangle(height) == expected


def test_non_integer_height():
    with pytest.raises(TypeError):
        draw_triangle("abc")


def test_float_height():
    with pytest.raises(TypeError):
        draw_triangle(3.5)


def test_single_character():
    height = 1
    result = draw_triangle(height)
    assert result == "*"
