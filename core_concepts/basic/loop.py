# while loop, useful for loop counter manipulation
n = 5
while n < 5:
    print(n)
    n += 1

print("")
# Looping from i = 0 to i = 4
for i in range(5):
    print(i)

print("")
# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)

print("")
# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

nums = [10, 50, 70, 60]

# pick index and val from an iterable object
for i, val in enumerate(nums):
    print(i, val)

# break and continue
print("")
for n in nums:
    if n == 10:
        print("continue")
        continue
    elif n == 70:
        print("break")
        break
    print(f"{n}")
else:
    print("else part of for loop: we came here because control did not hit break")

print("end of loop")

low = 2
high = 10
# usage of else block: find prime nums from 2 to 10
for n in range(low, high):
    for i in range(2, n // 2):
        if n % i == 0:
            break
    else:
        print(f"prime: {n}")

# alternate: without using else block
print("")
for n in range(low, high):
    is_prime_flag = True
    for i in range(2, n // 2):
        if n % i == 0:
            is_prime_flag = False  # need to send a flag outside the loop and determine prime
            break

    if is_prime_flag is True:  # means break statement did not hit
        print(f"prime: {n}")

