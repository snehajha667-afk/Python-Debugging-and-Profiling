"""
Profiling Practice
Author: Sneha Jha

This file demonstrates Python profiling
using time, timeit and cProfile.
"""

import time
import timeit
import cProfile


# ---------------------------------
# Example 1 : time module
# ---------------------------------

start = time.time()

total = 0

for i in range(1000000):
    total += i

end = time.time()

print("Execution Time using time module:")
print(end - start)


# ---------------------------------
# Example 2 : timeit
# ---------------------------------

execution = timeit.timeit(
    stmt="sum(range(1000))",
    number=1000
)

print("\nExecution Time using timeit:")
print(execution)


# ---------------------------------
# Example 3 : cProfile
# ---------------------------------

def calculate():

    total = 0

    for i in range(1000000):
        total += i

    return total


print("\nProfiling calculate() function\n")

cProfile.run("calculate()")
