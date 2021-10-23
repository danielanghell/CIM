import math


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def fullnumber(self):
        if self.real >= 0:
            if self.img >= 0:
                return str(self.real) + " + j" + str(self.img)
            else:
                stripping = str(self.img)
                stripping = stripping.lstrip('-')
                return str(self.real) + " - j" + stripping
        else:
            if self.img >= 0:
                return str(self.real) + " + j" + str(self.img)
            else:
                stripping = str(self.img)
                stripping = stripping.lstrip('-')
                return str(self.real) + " - j" + stripping


#overload the + operator
    def __add__(self, other):
        result_real = self.real + other.real
        restul_img = self.img + other.img
        return Complex(result_real, restul_img)


#overload the - operator
    def __sub__(self, other):
        result_real = self.real - other.real
        result_img = self.img - other.img
        return Complex(result_real, result_img)


#modulus of a Complex number
    def modulus(self):
        real = self.real
        img = self.img
        return int(math.sqrt(pow(real,2) + pow(img, 2)))





