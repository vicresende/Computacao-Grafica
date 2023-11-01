class Mat2:
    def __init__(self, a=1, b=0, c=0, d=1):
        self.m = [a, b, c, d]

    def get_item(self, i):
        return self.m[i]

    def set_item(self, i, value):
        self.m[i] = value

    def to_string(self):
        return f"[{self.m[0]} {self.m[1]}\n {self.m[2]} {self.m[3]}]"

    def multiply(self, other):
        a = self.m[0] * other.m[0] + self.m[1] * other.m[2]
        b = self.m[0] * other.m[1] + self.m[1] * other.m[3]
        c = self.m[2] * other.m[0] + self.m[3] * other.m[2]
        d = self.m[2] * other.m[1] + self.m[3] * other.m[3]
        return Mat2(a, b, c, d)

    def __eq__(self, other):
        if isinstance(other, Mat2):
            return self.m == other.m
        return False