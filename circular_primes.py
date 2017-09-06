#!/usr/bin/python
# _*_ coding: utf-8 _*_


def prime(n):
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        w = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True


def circle_list(n):
    cir_list = []
    str_n = str(n)
    for i in range(len(str_n)):
        new_n = str_n[i:] + str_n[:i]
        cir_list.append(int(new_n))
    return cir_list


def all_circle_prime(n):
    """return True if all circle numbers of n is prime"""
    n_circle = circle_list(n)
    for i in n_circle:
        if not prime(i):
            return False
    return True


def main(n=6):
    count = 0
    for i in range(1, 10**n):
        if all_circle_prime(i):
            print i, '\tis a circular prime'
            count += 1
    return count


if __name__ == "__main__":
    count = main(6)
    print "  --\n{} circular primes within 1 million\n  --".format(count)
