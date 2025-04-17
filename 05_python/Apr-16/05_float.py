x = 10.0
print(type(x))
print(x.as_integer_ratio())
print(x.is_integer())
print(x.hex())
x = float.fromhex('0x1.4000000000000p+3')
print(x)