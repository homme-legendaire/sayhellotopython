import mod1
print(mod1.add(3,4))
print(mod1.sub(5,1))

from mod1 import add
print(add(4,7))

import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))
