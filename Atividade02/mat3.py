class Mat3:
    def __init__(self, a=1, b=0, c=0, d=0, e=1, f=0, g=0, h=0, i=1):
        self.m = [a, b, c, d, e, f, g, h, i]

    def get_item(self, i, j):
        return self.m[i * 3 + j]

    def set_item(self, i, j, value):
        self.m[i * 3 + j] = value

    def to_string(self):
        return f"[{self.m[0]} {self.m[1]} {self.m[2]}\n {self.m[3]} {self.m[4]} {self.m[5]}\n {self.m[6]} {self.m[7]} {self.m[8]}]"

    def multiply(self, other):
        result = [0] * 9
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i * 3 + j] += self.m[i * 3 + k] * other.m[k * 3 + j]
        return Mat3(*result)

    def __eq__(self, other):
        if isinstance(other, Mat3):
            return self.m == other.m
        return False