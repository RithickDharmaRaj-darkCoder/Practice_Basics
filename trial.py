# Data Structure ...
# User-Defined ...
# Stack...
# Collections Library ...
# deque (Double Ended Queue) ...

from collections import *

stk = deque([7,8,5])
stk.append(6)
print(stk)
stk.pop()
print(stk)
print(stk.pop())
print(not stk)