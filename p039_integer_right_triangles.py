#!/usr/bin/python
# _*_ coding: utf-8 _*_


def right_triangle(a, b, c):
    """Return True if a b c is a right triangle, force a<=b and c long side"""
    return (a**2 + b**2 == c**2) and a <= b
    '''or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)
    '''


def find_tri(p):
    """Return all the possible right triangle(s) by perimeter p"""
    tri = []
    for a in range(1, p/2):
        for b in range(1, p/2):
            c = p - a - b
            if right_triangle(a, b, c):
                tri.append([a, b, c])
    if tri:
        return tri
    else:
        return None


def main():
    max_p = 0
    max_sol = 0
    for i in range(1, 1001):
        i_tri = find_tri(i)
        if i_tri:
            print '{} has {}: {}'.format(i, len(i_tri), i_tri)
            if len(i_tri) > max_sol:
                max_sol = len(i_tri)
                max_p = i
    print '  --\n maxium p is:{}\n  --'.format(max_p)


if __name__ == "__main__":
    main()
