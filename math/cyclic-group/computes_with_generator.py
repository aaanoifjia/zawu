import bisect

def computes_with_generator(x, n, mod):
  elements = []
  for p in range(n):
    bisect.insort(elements, x**p%mod)
  print(f"<{x}> = {elements}")