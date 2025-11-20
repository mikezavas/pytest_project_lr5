import math


# 1
def is_prime(n):
    """
    Проверяет, является ли число простым
    :param n: целое число
    :return: True or False
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 2
def factorial(n):
    """
    Вычисляет факториал числа
    :param n: неотрицательное целое число
    :return: факториал числа n
    """
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 3
def gcd(a, b):
    """
    Находит наибольший общий делитель (НОД) двух чисел
    :param a: целое число
    :param b: целое число
    :return: НОД чисел a и b
    """
    while b:
        a, b = b, a % b
    return abs(a)


# 4
def celsius_to_kelvin(celsius):
    """
    Конвертирует температуру из Цельсия в Кельвины
    :param celsius: число — температура в градусах Цельсия
    :return: число — температура в Кельвинах
    """
    return celsius + 273.15


# 5
def is_palindrome(text):
    """
    Проверяет, является ли строка палиндромом
    :param text: строка
    :return: True or False
    """
    text = text.lower().replace(" ", "")
    return text == text[::-1]
