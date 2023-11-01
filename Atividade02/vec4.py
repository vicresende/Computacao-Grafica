import math

class Vec4:
    def __init__(self, x=0, y=0, z=0, w=0):
        self.e = [x, y, z, w]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def w(self):
        return self.e[3]

    def negative(self):
        return Vec4(-self.e[0], -self.e[1], -self.e[2], -self.e[3])

    def get_item(self, i):
        return self.e[i]

    def set_item(self, i, value):
        self.e[i] = value

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2] + self.e[3] * self.e[3]

    def __add__(self, other):
        if isinstance(other, Vec4):
            return Vec4(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2], self.e[3] + other.e[3])
        raise TypeError("Unsupported operand type for +: Vec4 and {}".format(type(other)))

    def __eq__(self, other):
        if isinstance(other, Vec4):
            return self.e == other.e
        return False

    def multiply_inplace(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        self.e[3] *= t
        return self

    def divide_by_scalar(self, t):
        return self * (1.0 / t)

    def to_string(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]} {self.e[3]}"

    def subtract(self, other):
        return Vec4(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2], self.e[3] - other.e[3])

    def multiply(self, other):
        return Vec4(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2], self.e[3] * other.e[3])

    def __mul__(self, scalar):
        return Vec4(self.e[0] * scalar, self.e[1] * scalar, self.e[2] * scalar, self.e[3] * scalar)


def unit_vector(v):
    return v / v.length()

def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2] + u[3] * v[3]
