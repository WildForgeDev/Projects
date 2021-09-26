class Number:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self, other):
        n1 = self.n1 + other.n1
        n2 = self.n2 + other.n2
        s3 = Number(n1, n2)

        return s3


s1 = Number(58, 69)
s2 = Number(60, 65)

s3 = s1 + s2

print(s3.n1)

a = 5
b = 6
c = a + b
print(c)

