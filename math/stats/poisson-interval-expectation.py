import math

n = 40  # the range of intervals
u = 80.2 # the constant of poission distribution

result = 0
for a in (0, 40, 80, 120):
    for i in range(a, a+n):
        # print(i)
        result += math.exp(-u) * pow(u, i) / math.factorial(i)
    print(a, ':', result)
    result = 0