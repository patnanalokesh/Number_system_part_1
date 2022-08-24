# from decimal import Decimal as d
# a=d(0.7+0.2)  # will give exactly lengthy answer as{0.899999999999999911182158029987476766109466552734375}
# a=d(0.7)+d(0.2)  # will give exact half answer as {0.8999999999999999666933092612}
# a=d('0.7')+d('0.2')  #{0.9}
# print(a)  

# a=0.7;b=0.2
# c=a+b
# print(c)  #0.8999999999999999
# print('%.1f'%c)   # 0.9

# print(5/0)   # ZeroDivisionError: division by zero  {in mathematics anything by 0 is given as infinity value.}

# from fractions import Fraction as f
# a=f(1,0)   #ZeroDivisionError: Fraction(1, 0)
# a=f(1,1)
# print(a)
# a=f(1,4)
# print(a)
# b=f(2)
# print(b)
# b=f(5,25)
# print(b)
# b=f(4,24)
# print(b)
# b=f(4,25)  # 4/25
# print(b)


# a=7_246415_3655
# print(a,type(a))

# b=45_451
# print(b,type(b))

# c=89_14.548484
# print(c,type(c))

# d=1_.2315
# print(d,type(d))  #  SyntaxError: invalid decimal literal

# e=1._5452
# print(e,type(e))  # SyntaxError: invalid decimal literal

# f=12_454.455
# print(f,type(f))

# a=8;b=2.6
# print(a,type(a))
# print(b,type(b))
# print(isinstance(a, int))
# print(isinstance(a, float))
# print(isinstance(b, float))
# print(isinstance(b, int))
# print(isinstance(b, bool))
# print(isinstance(b, str))

# c=64j
# print(c,type(c))  # <class 'complex'>

# f=25+654j
# print(f,type(f))
# print(isinstance(f, complex))

from fractions import Fraction as F 
# print(F(6,2))
# print(F(2.5))
# print(F('2.5'))
# print(F("2.5"))
# print(F(4.5))
# print(F(5,0))   # ZeroDivisionError: Fraction(5, 0)
# b=5/0  #  ZeroDivisionError: division by zero
# v=F(5,20)
# print(v)

# f=25+54j
# print(f,type(f))
# print(f.real)
# print(f.imag)

# b=3*4.3j
# print(b,type(b))
# print(b.real)
# print(b.imag)

# print(1e0)
# print(4e3)
# print(4e0)
# print(1e1)
# print(1e2)
# print(12e1)
# print(12e3)

# print(5*8)
# print(4**3)
# print(2**3)
# print(2.5**3)
# print(2.5**2)
# print(1.2**2)

# import math as m
# print(m.exp(1))  # e=2.71828,  e*e*e
# print(m.exp(3))
# print(m.exp(55))