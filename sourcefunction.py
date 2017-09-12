#!/usr/bin/python
# _*_ coding: utf-8 _*_


"""this is a basic collection of function frequently used in Project Euler
right now have: prime, factors, palindrome..."""


def prime(n):
    """Return True if n is a prime. It should be faster"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def factors(n):
    """ return all factors of n into a list, including 1 and n """
    if n <= 0:
        return False
    if n == 1:
        return [1, 1]

    i = 2
    max_factor = n / 2
    factors_list = [1]

    while i <= max_factor:
        if n % i == 0:
            factors_list.append(i)
        i += 1

    factors_list.append(n)
    return factors_list


def palindrome(n):
    """Return True if n is a palindrome, like 81133118 """
    n = str(n)
    for i in range(len(n) / 2):
        if n[i] != n[-1 - i]:
            return False
    return True
