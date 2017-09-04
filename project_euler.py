#!/usr/bin/python
# _*_ coding:utf-8 _*_


import math
import pprint
import itertools


def multiples_of_3_and_5(n=1000):
    """return sum of all the multiples of 3 or 5 below n """
    list_3_multiples = [i * 3 for i in range(n / 3 + 1) if i * 3 < n]
    list_5_multiples = [j * 5 for j in range(n / 5 + 1) if j * 5 < n]
    return sum(set(list_3_multiples) | set(list_5_multiples))


def fibonacci(max_n):
    """Return a list contain fibonacci numbers below max_n"""
    fib_list = [1, 1]
    while fib_list[-1] + fib_list[-2] < max_n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


def even_fibonacci(max_num):
    """return a list consist of even fibonacci below max_num"""
    fib_list = fibonacci(max_num)
    even_dib_list = []

    for i in fib_list:
        if i % 2 == 0:
            print "even fibonacci number: {}".format(i)
            even_dib_list.append(i)

    return even_dib_list


def prime(n):
    """ Return True if n is a prime, otherwise False. """
    max_fac = int(math.sqrt(n) + 1)
    for i in range(2, max_fac):
        if n % i == 0:
            return False
    return True


def prime_v2(n):
    """ Return True if n is a prime, otherwise False. less memory cost """
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_v3(n):
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


def prime_below_max(max_num):
    """return all primes below max_num into a list, with function prime_v3."""
    prime_list = []
    i = 2
    while i <= max_num:
        if prime_v3(i):
            prime_list.append(i)
        i += 1

    return prime_list


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


def prime_factor(n):
    """find the largest prime factor of max_num"""
    i = 2
    rest = n
    prime_fac_list = []
    while rest != 1:
        if not(rest % i == 0 and prime_v3(i)):
            i += 1
        elif prime_v3(i) and rest % i == 0:
            prime_fac_list.append(i)
            print "prime factor of {} : {}".format(n, i)
            rest = rest / i
    return prime_fac_list
    # return max(prime_fac_list)


def palindrome(n):
    """Return True if n is a palindrome, like 81133118, also works for string like"""
    n = str(n)
    for i in range(len(n) / 2):
        if n[i] != n[-1 - i]:
            return False
    return True


def largest_palindrome_product(n):
    """
    find the largest palindrome number of product of n-digit number,
    return the product of each number
    """
    max_n = int('9' * n)

    target_list = []
    max_palin = 1
    for i in range(max_n, 0, -1):
        for j in range(max_n, 0, -1):
            posedu_palindrome = i * j
            if palindrome(posedu_palindrome):
                target_list.append(posedu_palindrome)
                if posedu_palindrome > max_palin:
                    print "palindrome:{} = {} * {}".format(posedu_palindrome, i, j)
                    max_palin = posedu_palindrome

    return max(target_list)


def divisible_by1_to_n(a, n=20):
    """return True if a is divisible by 1 to n (defult 20)"""
    i = 2
    while i <= n:
        if a % i != 0:
            return False
        i += 1

    return True


def smallest_multiple(n):
    """return the smallest number be divisible by 1 to n (defult 20)"""
    i = 1
    while not divisible_by1_to_n(i, n):
        i += 1

    return i


def sum_square_difference(n):
    """return square of sum MINUS sum of square for numbers from 1 to n"""
    sum_of_square = 0

    for i in range(n + 1):
        sum_of_square += i**2
    print "sum of square from 1 to {} is {}".format(n, sum_of_square)

    square_of_sum = (sum(range(n + 1)))**2
    print "square of sum from 1 to {} is {}".format(n, square_of_sum)

    return square_of_sum - sum_of_square


def the_n_th_prime(n):
    """return the n-th prime, begin with:2, 3, 5, 7...."""
    count = 0
    x = 2
    while True:
        if prime(x):
            count += 1
            print "{}-th prime:{}".format(count, x)
        if prime(x) and count == n:
            return x
        x += 1


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
            print "find product {} \t= self product of {}".format(largest_product, num)

    return largest_product


def special_pythagorean_triplet():
    """find the special pythagorean triplet with a+b+c =1000"""
    for a in range(1, 500):
        for b in range(1, 500):
            c = 1000 - (a + b)
            if a < b and a**2 + b**2 == c**2:
                print('a= %d b= %d c= %d, a*b*c= %d' % (a, b, c, a * b * c))


def summation_of_primes(max_n, min_n=2):
    """return the sum of primes below max_n, default begin with 2, 3, 5...."""
    i = min_n
    sum_prime = 0
    while i < max_n:
        if prime_v3(i):
            sum_prime += i
            print "add prime:{} sum = {}".format(i, sum_prime)
        i += 1

    return sum_prime


def n_th_triangle_num(n):
    return (1 + n) * n / 2


def highly_divisible_triangular_number(n):
    pass


def lattice_path(grid_size):
    """caution: cpu expose after grid size above 12*12"""
    walk_routes = []
    routes_generator = itertools.product('dr', repeat=grid_size * 2)
    count = 0
    try:
        while True:
            route = ''.join(next(routes_generator))
            if route.count('r') == grid_size and route.count('d') == grid_size:
                walk_routes.append(route)
                count += 1
                # print "-- {} -- all: {}".format(routes, count)

    except StopIteration:
        pass
    return walk_routes, count


def lattice_move(a, b):

    if a == 0 and b == 0:
        print a, b
        return 0
    elif a == 1 and b == 0:
        # print a, b
        return 1
    elif a == 0 and b == 1:
        # print a, b
        return 1
    elif a == 0:
        # print a, b
        return lattice_move(a, b - 1)
    elif b == 0:
        # print a, b
        return lattice_move(a - 1, b)
    else:
        # print a, b
        return lattice_move(a - 1, b) + lattice_move(a, b - 1)


def lattice_path_v2(a, b):
    path_initial = 'r' * a + 'd' * b

    return path_initial


def collatz(n):
    """next collatz number generator"""
    if n <= 1:
        yield None
    elif n % 2 == 0:
        yield n / 2
    elif n % 2 == 1:
        yield 3 * n + 1
    else:
        yield None


def longest_collatz_sequence(n):
    """return the longest collatz sequence under n """
    i = 1
    longest_seq = 0

    while i <= n:
        i_seq = [i, ]
        next_clooatz_i = i
        while next_clooatz_i != 1:
            next_clooatz_i = next(collatz(next_clooatz_i))
            i_seq.append(next_clooatz_i)
        # print i, len(i_seq), i_seq[0:5], '...'

        if len(i_seq) > longest_seq:
            longest_seq = len(i_seq)
            longest_seq_id = i
            print "collatz seq from {} has {} items: {} ... 1".format(longest_seq_id, longest_seq, i_seq[0:5])
        i += 1

    return longest_seq_id


def power_digit_sum(n):
    """ return the sum of digits of number n """
    n_integer = str(n)
    return sum([int(i) for i in n_integer])


def factorial_digit_sum(n):
    """ return the sum of digit in number n! """
    n_target = 1
    i = 1
    while i < n:
        i += 1
        n_target *= i
    print "{}! = {}".format(n, n_target)
    return sum([int(i) for i in str(n_target)])


def amicable_numbers(n):
    """return the sum of all the amicable m=numbeers under n"""
    i = 1
    amicable_list = []
    while i <= n:
        # d_i = d(i)
        i_fac = factors(i)[:-1]
        d_i = sum(i_fac)
        if i == sum(factors(d_i)[:-1]) and i != d_i:
            amicable_list.append(i)
            print "amicable list:", amicable_list
        i += 1

    return sum(amicable_list)


def perfect_number(n):
    """return true if n is a perfect number like 28, factor:1+2+4+7+14 = 28 """
    factors_n = factors(n)
    return sum(factors_n[:-1]) == n


def abundant_num(n):
    """return true if n is a abundant number """
    factors_n = factors(n)
    return sum(factors_n[:-1]) > n


def non_abundant_sum(n):

    abundant_add_set = set()
    abundant_list = []

    for i in range(1, n):
        if abundant_num(i):
            abundant_list.append(i)
    # print "abundant list: {}".format(abundant_list)

    for j in range(1, n):
        for abundant in abundant_list:
            if (j - abundant in abundant_list):
                abundant_add_set.add(j)
                break
    # print "abundant add set:{}".format(abundant_add_set)

    non_abundant_add_set = set(range(1, n)) - abundant_add_set
    print "non-abundant add set:", non_abundant_add_set

    return sum(non_abundant_add_set)


def one_thousand_digit_fibonacci(n=1000):
    max_search = 10**1000


if __name__ == '__main__':
    print "--**--\nTo solve problems at Project Euler.\
by Yanshi Xiong.\n--"
    print "solved problems:\n\
problem 1: Multiples of 3 and 5\n\
problem 2: Even Fibonacci numbers\n\
problem 3: Largest prime factor\n\
problem 4: Largest palindrome product\n\
problem 5: Smallest multiple\n\
problem 6: Sum square difference\n\
problem 7: 10001st prime\n\
problem 8: Largest product in a series\n\
problem 9: Special Pythagorean triplet\n\
problem 10: Summation of primes\n\
problem 14: Longest Collatz sequence\n\
problem 16: Power digit sum\n\
problem 20: Factorial digit sum\n\
problem 21: Amicable numbers\n\
problem 23: Non-abundant sum\n\
--"
    problem_index = input("input the problem number to test: ")
    print "--\nworking on problem: {}...\nResult:\n".format(problem_index)

    # <test longest_collatz_seq>:
    # pprint.pprint(longest_collatz_sequence(10**6))

    # <test lattice_path function>:
    # grid = 20
    # print "{} grid {} ways".format(grid, lattice_move(grid, grid))

    # <test_3 largest prime factor>:
    if problem_index == 23:
        print non_abundant_sum(28124)

    elif problem_index == 21:
        n = 10000
        print "the sum of all the amicable numbers under {} \
is: {}".format(n, amicable_numbers(n))

    elif problem_index == 20:
        n = 100
        print "the sum of the digits in the number {}! \
is: {}".format(n, factorial_digit_sum(n))

    elif problem_index == 16:
        n = 2**1000
        print "the sum of the digits of {} \
is: {}".format(n, power_digit_sum(n))

    elif problem_index == 14:
        n = 10**6
        print "the longest collatz seq under {} \
is: {}".format(n, longest_collatz_sequence(n))

    elif problem_index == 10:
        n = 2 * (10**6)
        print "the sum of all primes below {} \
is {}".format(n, summation_of_primes(n))

    elif problem_index == 9:
        special_pythagorean_triplet()

    elif problem_index == 8:
        with open("../data/Project_euler_source_largest_product\
_in_a_series.txt") as file:
            series_source = "".join(file.read().split())
        n = 13
        print "the greatest product by {} adjacent digits \
is {}".format(n, largest_product_in_series(series_source, n))

    elif problem_index == 7:
        n = 10001
        print "the 10 001st prime number is {}".format(the_n_th_prime(n))

    elif problem_index == 6:
        n = 100
        print "difference between the sum of the squares of the \
first {} natural numbers and the square of the sum \
is: {}".format(n, sum_square_difference(n))

    elif problem_index == 5:
        n = 20
        print "the smallest positive number that is evenly divisible by \
all of the numbers from 1 to {} is: {}".format(n, smallest_multiple(n))

    elif problem_index == 4:
        n = 3  # set to 3-digit number
        print "the largest palindrome made from the product of two {}-digit\
number is: {}".format(n, largest_palindrome_product(n))

    elif problem_index == 3:
        n = 600851475143
        print "the largest prime factor of {} \
is: {}".format(n, max(prime_factor(n)))

    # <test_2 even fibonacci numbers>:
    elif problem_index == 2:
        n = 4 * (10**6)
        print "the sum of even fibonacci number below {} \
is: {}".format(n, sum(even_fibonacci(n)))

    # <test_1 multiples of 3 and 5>:
    elif problem_index == 1:
        n = 1000
        print "the sum of all the multiples of 3 or 5 below {} \
is: {}".format(n, multiples_of_3_and_5(n))

    else:
        print "sorry, problem {} haven't finished....".format(problem_index)

print "\n--**--"

"""7768th tri num:3017479 has 24 factors so far max len: 480 with:17907120"""
