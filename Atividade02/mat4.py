class Mat4:
    def __init__(self, a=1, b=0, c=0, d=0, e=0, f=1, g=0, h=0, i=0, j=0, k=1, l=0, m=0, n=0, o=1, p=0):
        self.m = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]

    def get_item(self, i, j):
        return self.m[i * 4 + j]

    def set_item(self, i, j, value):
        self.m[i * 4 + j] = value

    def to_string(self):
        return f"[{self.m[0]} {self.m[1]} {self.m[2]} {self.m[3]}\n {self.m[4]} {self.m[5]} {self.m[6]} {self.m[7]}\n {self.m[8]} {self.m[9]} {self.m[10]} {self.m[11]}\n {self.m[12]} {self.m[13]} {self.m[14]} {self.m[15]}]"

    def multiply(self, other):
        result = [0] * 16
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    result[i * 4 + j] += self.m[i * 4 + k] * other.m[k * 4 + j]
        return Mat4(*result)

    def __eq__(self, other):
        if isinstance(other, Mat4):
            return self.m == other.m
        return False