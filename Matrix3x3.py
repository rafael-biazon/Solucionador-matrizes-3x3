import math
from Complex import *

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

class Matrix3x3:
     def __init__(self, r1, r2, r3, a11, a12, a13, a21, a22, a23, a31, a32, a33):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.a11 = a11
        self.a12 = a12
        self.a13 = a13
        self.a21 = a21
        self.a22 = a22
        self.a23 = a23
        self.a31 = a31
        self.a32 = a32
        self.a33 = a33
        self.delta = [0, 0, 0, 0]
        self.unknown = [0, 0, 0, 0]

     def SolveDelta(self, deltaIndex, a11, a12, a13, a21, a22, a23, a31, a32, a33):
        deltaIndex = deltaIndex 
        termo1 = Complex.Multiply3(a11, a22, a33)
        termo2 = Complex.Multiply3(a12, a23, a31)
        termo3 = Complex.Multiply3(a13, a21, a32)
        termo4 = Complex.Multiply3(a13, a22, a31)
        termo5 = Complex.Multiply3(a12, a21, a33)
        termo6 = Complex.Multiply3(a11, a23, a32)
        deltaA = Complex.Add3(termo1, termo2, termo3)
        deltaB = Complex.Add3(termo4, termo5, termo6)
        self.delta[deltaIndex] = Complex.Subtract(deltaA, deltaB)
        #print complex numbers' info for debugging
        """ print(f"termo1.info() = {termo1.info()}")
        print(f"termo2.info() = {termo2.info()}")
        print(f"termo3.info() = {termo3.info()}")
        print(f"termo4.info() = {termo4.info()}")
        print(f"termo5.info() = {termo5.info()}")
        print(f"termo6.info() = {termo6.info()}")
        print(f"deltaA.info() = {deltaA.info()}")
        print(f"deltaB.info() = {deltaB.info()}")
        print(f"self.delta.info() = {self.delta[deltaIndex].info()}") """
        return f"Delta{deltaIndex} = {deltaA.radius} ∠ {deltaA.angleInDeg}°  -  {deltaB.radius} ∠ {deltaB.angleInDeg}°  =  {self.delta[deltaIndex].radius} ∠ {self.delta[deltaIndex].angleInDeg}°"

     def SolveDelta0(self):
         return self.SolveDelta(0, self.a11, self.a12, self.a13, self.a21, self.a22, self.a23, self.a31, self.a32, self.a33)
     
     def SolveDelta1(self):
         return self.SolveDelta(1, self.r1, self.a12, self.a13, self.r2, self.a22, self.a23, self.r3, self.a32, self.a33)
     
     def SolveDelta2(self):
         return self.SolveDelta(2, self.a11, self.r1, self.a13, self.a21, self.r2, self.a23, self.a31, self.r3, self.a33)
     
     def SolveDelta3(self):
         return self.SolveDelta(3, self.a11, self.a12, self.r1, self.a21, self.a22, self.r2, self.a31, self.a32, self.r3)
     
     def SolveUnknown(self, unknownIndex):
         self.unknown[unknownIndex] = Complex.Divide(self.delta[unknownIndex], self.delta[0])
         return f"Incógnita {unknownIndex} = Delta{unknownIndex}/Delta = {self.unknown[unknownIndex].radius} ∠ {self.unknown[unknownIndex].angleInDeg}°"

     def SolveAll(self):
         self.SolveDelta0()
         self.SolveDelta1()
         self.SolveDelta2()
         self.SolveDelta3()
         self.SolveUnknown(1)
         self.SolveUnknown(2)
         self.SolveUnknown(3)

        
    
    

    



        