# import Pack.pack2 as p2
#
# p2.greet('Ivan')
#
# fact = p2.factor(6)
# print(fact)

# from Pack.pack2 import greet, factor
#
# greet('Ivan')
# fact = factor(6)
# print(fact)

# import Pack.pack2
# print(dir())
#
# print(Pack.pack2.__name__)
# print(__name__)

# import sys
# print(sys.path)

from Pack.pack3 import A
A.fun_a()

from Pack.pack2 import (greet as g,
                        factor as f)

g('Ivan')
print(f(4))


