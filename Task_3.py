# a) Создайте класс Matrix
# который должен принимать данные (список списков) для формирования матрицы.

# b) Следующий шаг
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# c) Далеее
# реализовать перегрузку метода __add__()
# для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, Mylist):
        self.Mylist = Mylist

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.Mylist]))

    def __add__(self, other):
        for i in range(len(self.Mylist)):
            for j in range(len(other.Mylist[i])):
                self.Mylist[i][j] = self.Mylist[i][j] + other.Mylist[i][j]
        return Matrix.__str__(self)


matrix = Matrix([[-1, 0, 1], [-1, 0, 1]])
newMatrix = Matrix([[-2, 0, 2], [-2, 0, 2]])
print('Результат сложения двух матриц:')
print(matrix.__add__(newMatrix))