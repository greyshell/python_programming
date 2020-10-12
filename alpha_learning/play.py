# helper script to create the hashtable

from math import sqrt

MAX = 10 ** 6


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 2):
        if n % i == 0:
            return False

    return True


powers_2 = []
n = 2
while n < MAX:
    powers_2.append(n)
    n *= 2
powers_2.append(n)

results = []

for i in range(MAX):
    if not is_prime(i):
        continue
    min_diff = MAX
    for j in powers_2:
        diff = int(abs(i - j))
        if diff < min_diff:
            min_diff = diff
    results.append((min_diff, i))

current = (-1, 0)
for result in results:
    if current[0] < result[0]:
        print(result)
        current = result
