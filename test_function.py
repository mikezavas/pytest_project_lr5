import pytest
import random

from sorting_lr3_function import (
    bubble_sort, selection_sort, insertion_sort,
    heap_sort, merge_sort, quick_sort
)
from utils_function import (
    is_prime, factorial, gcd, celsius_to_kelvin, is_palindrome
)


# Простые фикстуры
@pytest.fixture
def test_arrays():
    return {
        'empty': [],
        'single': [5],
        'sorted': [1, 2, 3, 4, 5],
        'reverse': [5, 4, 3, 2, 1],
        'random': [3, 1, 4, 1, 5]
    }


@pytest.fixture
def large_array():
    return random.sample(range(1, 101), 50)


# Тесты сортировок
@pytest.mark.parametrize("sort_func", [
    bubble_sort, selection_sort, insertion_sort,
    heap_sort, merge_sort, quick_sort
])
@pytest.mark.parametrize("arr,expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 1, 2], [1, 2, 3]),
])
def test_all_sorts(sort_func, arr, expected):
    """Тестируем все сортировки"""
    result, iterations = sort_func(arr.copy())
    assert result == expected
    assert iterations >= 0


def test_sorts_with_fixture(test_arrays):
    """Тестируем сортировки с фикстурой"""
    for name, arr in test_arrays.items():
        expected = sorted(arr)
        result, iterations = quick_sort(arr.copy())
        assert result == expected


# Тесты других функций
@pytest.mark.parametrize("number,expected", [
    (2, True), (3, True), (4, False), (17, True), (1, False)
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected


@pytest.mark.parametrize("n,expected", [
    (0, 1), (1, 1), (5, 120), (3, 6)
])
def test_factorial(n, expected):
    assert factorial(n) == expected


@pytest.mark.parametrize("a,b,expected", [
    (12, 18, 6), (17, 13, 1), (100, 25, 25)
])
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected


@pytest.mark.parametrize("celsius,kelvin", [
    (0, 273.15), (100, 373.15), (-273.15, 0)
])
def test_celsius_to_kelvin(celsius, kelvin):
    assert celsius_to_kelvin(celsius) == pytest.approx(kelvin)


@pytest.mark.parametrize("text,expected", [
    ("radar", True),
    ("hello", False),
    ("", True),
    ("a", True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected


# Тест исключений
def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-5)


# Простые тесты свойств
def test_sort_preserves_length(test_arrays):
    for name, arr in test_arrays.items():
        result, iterations = bubble_sort(arr.copy())
        assert len(result) == len(arr)


def test_sort_returns_tuple():
    test_data = [3, 1, 2]
    for sort_func in [bubble_sort, quick_sort, merge_sort]:
        result = sort_func(test_data.copy())
        assert isinstance(result, tuple)
        assert len(result) == 2