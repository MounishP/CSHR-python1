"""Implicit conversions"""
x = 10           # int
print(type(x))

y = 1.2          # float
print(type(y))

sum = x + y  # 11.2 float
print(type(sum))

"""Explicit conversions"""

n = "1234"     # convert into a int
print(type(n))
converted = int(n)
print(converted)
print(type(converted))
convertedFloat = float(n)
print(convertedFloat)

n = 47645
print(hex(n))
print(oct(n))

c = 'y'
print(ord(c))
