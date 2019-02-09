
from math import sqrt, sin, cos, exp
class functions:
    def __init__(self):
       print("Constructor")
    def ackley(self,values):
    
        a = 20
        b = 0.2
        c = 2*(22/7)
        d = len(values)

        # calc
        soma1 = 0.0
        soma2 = 0.0

        for x in values:
            soma1 += x*x
            soma2 += cos(c*x)
        
        soma1 /= d
        soma2 /= d

        # ackley
        result = -a*exp(-b*sqrt(soma1)) - exp(soma2) + a + exp(1)

        # ans
        return result

    def sphere(self,alist):
        sumOfValues = sum(i*i for i in alist)
        return sumOfValues

    def sumOfSquare(self,alist):

        count = 1
        sumOfValues = 0

        for x in alist:
            sumOfValues += count*(x*x)
            count +=1

        return sumOfValues

