#!/usr/bin/python
# _*_ coding: utf-8 _*_


def self_product(n):
    """return the self product result of each digit number"""
    if type(n) != int:
        return 0
    else:
        product = 1
        for i in range(len(str(n))):
            product *= int(str(n)[i])

    return product


def largest_product_in_series(series, loci_len):
    """for question 'largest product in a series' """
    largest_product = 1
    for i in range(len(series) - loci_len):
        num = int(series[i:i + loci_len])
        product = self_product(num)
        if product > largest_product:
            largest_product = product
            print "find product {} \t=\
            self product of {}".format(largest_product, num)
    return largest_product


def main():
        with open("./data_source/Project_euler_source_largest_product\
_in_a_series.txt") as file:
            series_source = "".join(file.read().split())
        n = 13
        print "the greatest product by {} adjacent digits \
is {}".format(n, largest_product_in_series(series_source, n))


if __name__ == '__main__':
    main()
