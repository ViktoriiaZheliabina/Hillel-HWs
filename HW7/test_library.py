import pytest

import library

choices_kopiyka_ending = [
    ('13', 'копійок'),
    ('1', 'копійка'),
    ('3', 'копійки'),
    ('28', 'копійок')
]


choices_gryvna_ending = [
    ('11', 'гривень'),
    ('1', 'гривня'),
    ('3', 'гривні'),
    ('55', 'гривень'),
]


choices_gryvni_kopiyki = [
    (10.10, ['10 гривень', '10 копійок']),
    (51.01, ['51 гривня', '1 копійка']),
    ]

@pytest.mark.parametrize('value, expected', choices_kopiyka_ending)
def test_kopiyka_ending(value, expected):
    assert library.kopiyka_ending(value) == expected


@pytest.mark.parametrize('value, expected', choices_gryvna_ending)
def test_gryvna_ending(value, expected):
    assert library.gryvna_ending(value) == expected


@pytest.mark.parametrize('value, expected', choices_gryvni_kopiyki)
def test_gryvni_kopiyki(value, expected):
    assert library.gryvni_kopiyki(value) == expected

