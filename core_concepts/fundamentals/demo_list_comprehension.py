a = [(x, y)
     for x in range(0, 10)
     if x > 3
     for y in range(0, 10)
     if y > 3  # default AND support but no OR
     if y < 6]
print(a)
