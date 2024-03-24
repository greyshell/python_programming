from collections import (
    defaultdict,
    Counter,
)

g = 2
p = 104729

lookup = {}
result = defaultdict(list)

for x in range(3, 10000):
    s = (g ** x) % p
    # print(f"public key: {s}, private key:{x}, ")
    private_key = lookup.get(s)

    if private_key is None:
        lookup[s] = x
    else:
        result[s].append(x)

print(result)


