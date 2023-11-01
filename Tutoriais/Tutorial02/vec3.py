import math

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.e = [x, y, z]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def negative(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def get_item(self, i):
        return self.e[i]

    def set_item(self, i, value):
        self.e[i] = value

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    def add(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self

    def multiply_inplace(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def divide_by_scalar(self, t):
        return self * (1.0 / t)

    def to_string(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def subtract(self, other):
        return Vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])

    def multiply(self, other):
        return Vec3(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2])

    def multiply_by_scalar(self, t):
        return Vec3(t * self.e[0], t * self.e[1], t * self.e[2])

def unit_vector(v):
    return v / v.length()

def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]

def cross(u, v):
    return Vec3(u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
