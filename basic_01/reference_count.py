import sys

a = [1, 2, 3]
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(a))
print(sys.getrefcount(a))
print(sys.getrefcount(a))



