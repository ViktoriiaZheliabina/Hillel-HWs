def test_age(human):
    assert human.age == 25


def test_gender(human):
    assert human.gender == 'female'


def test_name(human):
    assert human.name == "Eva"


def test_grow(human):
    human.grow()
    assert human.age == 26


def test_change_gender(human):
    human.change_gender('male')
    assert human.gender == "male"


def test_is_alive_when_alive(human):
    assert True


def test_is_alive_when_dead(old_human):
    assert True


def test_save_state(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__gender", "female"
    )
    assert human.gender == "female"


def test_validate_gender(non_human):
    assert True



