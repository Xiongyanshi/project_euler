#!/usr/bin/python
# _*_ coding: utf-8 _*_


from sourcefunction import prime


def the_n_th_prime(n):
    """return the n-th prime, begin with:2, 3, 5, 7...."""
    count = 0
    x = 2
    while True:
        if prime(x):
            count += 1
            # print "{}-th prime:{}".format(count, x)
        if prime(x) and count == n:
            return x
        x += 1


def main():
    n = 10001
    print "the 10001st prime number is {}".format(the_n_th_prime(n))


if __name__ == '__main__':
    main()
