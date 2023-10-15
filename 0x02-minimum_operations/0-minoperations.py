#!/usr/bin/python3
""" Script that executes only two operations which are CopyAll and Paste """

def minOperations(n):
    """
    Operations to be executed are CopyAll and Paste

    Args:
        n: input value
        factor_list: save two operations
    Return:sum of operations
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
