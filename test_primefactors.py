import pytest

from primefactor import PrimeFactor


def test_prime_factor_of_1():
    prime_factor = PrimeFactor()
    assert 1 == 1