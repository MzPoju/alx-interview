#!/usr/bin/python3
""" Template """

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Minimum number of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Minimum number of operations to reach {} char: {}".format(n, minOperations(n)))
