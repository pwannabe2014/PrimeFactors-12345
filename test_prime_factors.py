import pytest

from prime_factors import PrimeFactor


def test_prime_factor_of_1():
    prime_factor = PrimeFactor()
    assert prime_factor.of(1) == []
