import math

class Complex:
        def __init__(self, type, arg1, arg2):
            self.type = type
            if self.type == "Rectangular":
                self.real = round(arg1,8)
                self.imag = round(arg2,8)
                self.radius = round(math.sqrt((arg1*arg1)+(arg2*arg2)),8)
                self.angle = round(math.atan2(arg2, arg1),8)
                self.angleInDeg = round(math.degrees(math.atan2(arg2, arg1)),8)
            if self.type == "Polar":
                self.radius = round(arg1,8)
                self.angleInDeg = round(arg2,8)
                self.angle = round(math.radians(self.angleInDeg),8)
                self.real = round(self.radius*math.cos(self.angle),8)
                self.imag = round(self.radius*math.sin(self.angle),8)

        def Add(complex1, complex2):
            result = Complex("Rectangular", complex1.real+complex2.real, complex1.imag+complex2.imag)
            return result
            
        def Add3(complex1, complex2, complex3):
            result = Complex("Rectangular", complex1.real+complex2.real+complex3.real, complex1.imag+complex2.imag+complex3.imag)
            return result

        def Multiply(complex1, complex2):
            result = Complex("Polar", complex1.radius*complex2.radius, complex1.angleInDeg+complex2.angleInDeg)
            return result
        
        def Multiply3(complex1, complex2, complex3):
            result = Complex("Polar", complex1.radius*complex2.radius*complex3.radius, complex1.angleInDeg+complex2.angleInDeg+complex3.angleInDeg)
            return result

        def Subtract(complex1, complex2):
            result = Complex("Rectangular", complex1.real-complex2.real, complex1.imag-complex2.imag)
            return result

        def Divide(complex1, complex2):
            result = Complex("Polar", complex1.radius/complex2.radius, complex1.angleInDeg-complex2.angleInDeg)
            return result

        def info(self):
            return f"real = {self.real}, imag = {self.imag}, radius = {self.radius}, angle = {self.angle}, angleInDeg = {self.angleInDeg}"
             
