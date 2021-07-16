import pytest
import requests


def add_func(x):
    return x


def test_01():
    assert add_func(3) == 3


def test_02():
    assert add_func(5) == 4

if __name__ == '__main__':
    pytest.main(['-s'])