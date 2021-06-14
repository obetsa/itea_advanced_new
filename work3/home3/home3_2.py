"""2. Покрыть тестами задачу из прошлой домашки с матрицами: сложение, умножение на число, возникновение ошибки.
Либо если не получается с матрицей, то взять любую другую задачу из дз и написать тесты для неё."""


class InvalidMatrixDimensions(Exception):
    pass


class Matrix:
    def __init__(self, rows):
        maxlength = max(len(r) for r in rows)
        minlength = min(len(r) for r in rows)
        if minlength != maxlength:
            raise InvalidMatrixDimensions
        else:
            self.rows = rows
            self.width = maxlength
            self.height = len(rows)

    def __add__(self, other: 'Matrix'):
        if (self.height == other.height and self.width == other.width):
            rows = []
            for p,t in zip(self.rows, other.rows):
                r = []
                for i in range(self.width):
                    r.append(p[i] + t[i])
                rows.append(r)
            return Matrix(rows)

    def __sub__(self, other: 'Matrix'):
        if (self.height == other.height and self.width == other.width):
            rows = []
            for p,t in zip(self.rows, other.rows):
                r = []
                for i in range(self.width):
                    r.append(p[i] - t[i])
                rows.append(r)
            return Matrix(rows)

    def __mul__(self, other: 'Matrix'):
        if (self.height == other.height and self.width == other.width):
            rows= []
            for p,t in zip(self.rows, other.rows):
                r = []
                for i in range(self.width):
                    r.append(p[i] * t[i])
                rows.append(r)
            return Matrix(rows)

    def __truediv__(self, other: 'Matrix'):
        if (self.height == other.height and self.width == other.width):
            rows = []
            for p,t in zip(self.rows, other.rows):
                r = []
                for i in range(self.width):
                    r.append(p[i] / t[i])
                rows.append(r)
            return Matrix(rows)

                      
m = Matrix([[1, 2, 3], [2, 3, 4]])
n = Matrix([[1, 2, 3], [5, 3, 4]])
p = m + n
print(p.rows)
s = m - n
print(s.rows)
g = m * n
print(g.rows)
j = m / n
print(j.rows)
