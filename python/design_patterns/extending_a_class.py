class Triangles:
    count = 0
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        Triangles.count += 1

    def set_name(self, name):
        self.name = name

    def set_dim(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def get_count(self):
        return Triangles.count

# Describing a class
class Peri(Triangles):
    def calculate(self):
        self.pm = 0
        self.pm = self.s1 + self.s2 + self.s3

    def display(self):
        return self.pm

def main():
    p = Peri("PQR", 2, 3, 4)
    p.calculate()
    print(p.__str__())
    print(p.display())
    print(p.get_count())

    # The other way of calling from base class is:
    # print(super(Peri, self).display())

main()