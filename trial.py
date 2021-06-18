# Data Structure ...
# User-Defined ...
# Queue ...
# Collection Lib ...
# deque ...

from collections import *

qu = deque()
print(not qu)
qu.appendleft(7)
qu.appendleft(8)
qu.appendleft(5)
qu.appendleft(6)
qu.appendleft(9)
print(qu)
qu.pop()
print(qu)

qu1 = deque()
qu1.append(7)
qu1.append(8)
qu1.append(5)
qu1.append(6)
qu1.append(9)
print(qu1)
qu1.popleft()
print(qu1[0])