#!/usr/bin/python
# _*_ coding: utf-8 _*_

import pprint
from decimal import *
getcontext().prec = 100

def reciprocal_math(x):
    """return the reciprocal result to x, like 1/1, 1/2, 1/3.....1/x """
    repi_list = []
    longest = 1
    for i in range(1, x+1):
        # print i, str(Decimal(1)/Decimal(i))
        i_deci = str(Decimal(1) / Decimal(i))
        print "1/{} \t= {}".format(i, i_deci)
        repi_list.append([i, i_deci])

    return repi_list


def cycle(string, win_len):
    """return true if string is a cycle seq by window length win_len """
    for start_pos in range(0, len(string) - win_len + 1, win_len):
        end_pos = start_pos + win_len
        # print start_pos, end_pos
        if string[start_pos:end_pos] != string[0:win_len]:
            return False
    return True


def reci_cyc_max(max_n):
    """Main function for longest reciprocal cycle searching, not working yet"""
    reci_list = reciprocal_math(max_n)
    for reci in reci_list:
        reci_id = reci[0]
        reci_seq = reci[1][2:]
        if len(reci_seq) == 100:
            search_start = 0
            longest_window = 1
            for window_wid in range(1, len(reci_seq)):
                pass            
    return True

if __name__ == "__main__":
    # n = int(input("input :"))
    # reciprocal_math(n)
    reci_cyc_max(10)
