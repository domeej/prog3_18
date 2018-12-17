import sys

"""ersten 10 zahlen"""
x = list(range(0,101))
print(x[:10])
print(x[-10:])
print(x[::10])
print(x[int(len(x)/2)])
print(list(x[::3])[4:-5])
