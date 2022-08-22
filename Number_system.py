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

from fractions import Fraction as f
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