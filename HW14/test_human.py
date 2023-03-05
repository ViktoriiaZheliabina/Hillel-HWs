from HW14.human import Human
import pytest


class TestHuman:

    def setup_class(self):
        self.human = Human("Eva", 25, 'female')

    def setup(self):
        print("Setup for each test")

    def test_age(self):
        assert self.human.age == 25

    def test_gender(self):
        assert self.human.gender == 'female'

    def test_name(self):
        assert self.human.name == "Eva"

    def test_grow(self):
        self.human.grow()
        assert self.human.age == 26


    def test_change_gender(self):
        self.human.change_gender("male")
        assert self.human.gender == "male"


    def test_is_alive(self):
        self.human.is_alive()
        assert self.human.status is True

    @pytest.mark.parametrize("gender, expected", [
        ('male', 'male'),
        ('female', "female"),
         ])
    def test_human_gender(self, gender, expected):
        self.human.change_gender(gender)
        assert self.human.gender == expected


    def test_wrong_gender(self):
        with pytest.raises(Exception):
            self.human.change_gender("")

    def teardown(self):
        print("Teardown after each test")
