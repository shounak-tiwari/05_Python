x = 1024
print(x.to_bytes(2,byteorder='big'))
b = b'\x04\x00'
num = int.from_bytes(b,byteorder='big')
print(num)


# magic / special methods 

#add 
#mul
#floordiv
#mod
#pow
#eq ==equality check 
#lt --lest than 
#gt == greater than
#abs()
#div()
#oct:b
#bin:b
#hex:b
#roound:b
#isinstance :b
