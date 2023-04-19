# This program gives all generators of order n in Z mod.
#   x: a known generator of order n

import sys
import bisect
import group_of_units_modulo_n as gr

x = int(sys.argv[1])
n = int(sys.argv[2])
mod = int(sys.argv[3])

gcds = gr.Group(n)

for p in gcds.elements:
  print(f"{x}^{p} mod {mod} = {x**p % mod}")

