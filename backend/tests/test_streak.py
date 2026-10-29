from app.streak import calculate_streak


def test_empty():
    assert calculate_streak([]) == 0


def test_all_done():
    assert calculate_streak([True, True, True]) == 3


def test_break_in_middle():
    assert calculate_streak([True, False, True, True]) == 2


def test_last_missed():
    assert calculate_streak([True, True, False]) == 0


def test_max_365():
    assert calculate_streak([True] * 400) == 365
