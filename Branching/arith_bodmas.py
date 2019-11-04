x, y, z = (5,4,6)                                              # Variable declaration 
addi = x+y                                                     # sum
minu = x-y                                                     # subtraction
multi = x*y                                                    # multiplication
divi = x/y                                                     # division
expr = y*(z-y)+z                                               # 1st expression
bigexp = z%y*(x-y) + z%y*(x+y) + z%y*(x*y)                     # 2nd expression

print('x + y = ' + str(addi))
print('x - y = ' + str(minu))
print('x * y = ' + str(multi))
print('x / y = ' + str(divi))
print('y(z-y) + z = ' + str(expr))
print('z%y(x-y) + z%y(x+y) + z%y(x*y) = ' + str(bigexp))