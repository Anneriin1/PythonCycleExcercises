import pytest

from fisher import fisher


@pytest.mark.parametrize("text, expected", [
    ("Sa jood [_]b ja naudid elu.", 1),
    ("Hommikul on meres on palju ^~~, kuid sa läksid ikka \______/ ", 2),
    ("Sa {zzz}°°° ning hiljem ning kalakäsiraamatust uusi õngetrikke õppida", 3),
    ("oOoOoOoOoOo ning {zzz}", 4),
    ("Hommikul on meres on palju ^~~ ja 0% akudest laetud", 2),
    ("oOoOoOoOoOo ja {zzz}°°°", 4),
    ("oOoOoOoOoOo ja {zzz}°°° ning päeva lõpuks [_]b", 4),
    ("Täna on päikesepaisteline päev, lainet pole üldse.", 0),
    ("[-_-]b", 0),
    ("~~~~~~^~~~~~", 2),
    ("{zzz}°°°( -_-)", 3),
    ("oOoOoOoOoOo", 4),
    ("^~~", 2),
    ("0% IIII 100%", 3),
    ("∠ ･`_´･", 4),
])
def test_fisher_additional_cases(text, expected):
    assert fisher(text) == expected
