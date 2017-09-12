#!/usr/bin/python
# _*_ coding: utf-8 _*_


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


def prime_factor(n):
    """find the prime factor of n"""
    i = 2
    rest = n
    prime_fac_list = []
    while rest != 1:
        if not(rest % i == 0 and prime(i)):
            i += 1
        elif prime(i) and rest % i == 0:
            prime_fac_list.append(i)
            print "prime factor of {} : {}".format(n, i)
            rest = rest / i
    return prime_fac_list


def main():
    pass
    n = 600851475143
    print "largest prime factor of {} is: {}".format(n, max(prime_factor(n)))


if __name__ == '__main__':
    main()
