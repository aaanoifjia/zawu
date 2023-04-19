import sys
import math
import computes_with_generator as cg

class Group:
    def __init__(self, n):
        self.elements = []
        for x in range(n):
            if math.gcd(x, n) == 1:
                self.elements.append(x)
        print("Group of units modulo", n, "contains:", len(self.elements),
              " elements", self.elements)


class Order:
    def __init__(self, order, generator):
        self.order = order
        self.elements = []
        self.elements.append(generator)
    def output(self):
        print(self.order, ":", self.elements)


n = int(sys.argv[1])
g = Group(n)

orders = []
for x in g.elements:
    t = 1
    while t < n:
        if (x**t - 1)%n == 0:
            added = False
            for o in orders:
                if t == o.order:
                    o.elements.append(x)
                    added = True
                    break
            if added:
                break
            o = Order(t, x)
            orders.append(o)
            break
        t=t+1

print("Orders in form of order: element1, element2, ...")
for o in orders:
    o.output()
    cg.computes_with_generator(o.elements[0], o.order, n)
    print('')