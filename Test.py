from Complex import *
from Matrix3x3 import *

""" number1 = Complex("Rectangular", -3, 4)
number2 = Complex("Polar", 10, 30)
print(number1.info())
print(number2.info())
number3 = Complex.Add(number1, number2)
print(number3.info()) """


# [Matriz dos resultados/fontes] = [Matriz "das impedâncias" (a + linha + coluna)] [Matriz das incógnitas]
#  ___      ___            ___                           ___    ___       ___
# |     r1     |    ___   |       a11     a12     a13       |  |     inc1    |
# |     r2     |    ___   |       a21     a22     a23       |  |     inc2    |
# |___  r3  ___|          |___    a31     a32     a33    ___|  |___  inc3 ___|
#
# Delta0 = a11*a22*a33 + a12*a23*a31 + a13*a21*a32 - a13*a22*a31 - a12*a21*a33 - a11*a23*a32
# Delta1 = r1*a22*a33 + a12*a23*r3 + a13*r2*a32 - a13*a22*r3 - a12*r2*a33 - r1*a23*a32
# Delta2 = a11*r2*a33 + r1*a23*a31 + a13*a21*r3 - a13*r2*a31 - r1*a21*a33 - a11*a23*r3
# Delta3 = a11*a22*r3 + a12*r2*a31 + r1*a21*a32 - r1*a22*a31 - a12*a21*r3 - a11*r2*a32

# Defina r1, r2, r3, a11, a12... a33 como complexos

"""
r1 = Complex("Polar", 5, 5)
r2 = Complex("Polar", 5, 5)
r3 = Complex("Polar", 6, 7)

a11 = Complex("Polar", 4, 3)
a12 = Complex("Polar", 9, 50)
a13 = Complex("Polar", 7, 30)

a21 = Complex("Polar", 45, 80)
a22 = Complex("Polar", 6, 87)
a23 = Complex("Polar", 3, -45)

a31 = Complex("Polar", 2, -126)
a32 = Complex("Polar", 7, 280)
a33 = Complex("Polar", 10, -175)

matrix1 = Matrix3x3(r1, r2, r3, a11, a12, a13, a21, a22, a23, a31, a32, a33)
matrix1.SolveAll()
"""