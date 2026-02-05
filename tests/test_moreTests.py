import pytest

def test_first():
    person_age = 20
    assert person_age >= 18, "Personen er ikke voksen endnu"

def test_second():
    username = "this_is_my_username"
    max_username_length = 15
    assert len(username) <= max_username_length, "Brugernavnet er for langt"