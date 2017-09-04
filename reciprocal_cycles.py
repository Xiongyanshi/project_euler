#!/usr/bin/python
# _*_ coding: utf-8 _*_

# import pprint
from decimal import *
getcontext().prec = 100


def reciprocal_math(x):
    """return dict of reciprocal result, from 1/2, 1/3.....1/x """
    repi_dict = {}
    for i in range(2, x+1):
        # print i, str(Decimal(1)/Decimal(i))
        i_deci = str(Decimal(1) / Decimal(i))
        print "1/{} \t= {}...".format(i, i_deci[:50])
        repi_dict[i] = i_deci

    return repi_dict






if __name__ == "__main__":
    # n = int(input("input :"))
    # print reciprocal_math(n)
    reci_cyc_max(10)
