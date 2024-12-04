import math


class Square:
    # コードが期待通り動作するように実装
    def __init__(self, side):
        self.side = side

    def area(self):
        result = f"{self.side**2:.2f}".rstrip("0").rstrip(".")
        return result

    def diagonal(self):
        result = f"{math.sqrt(2)*self.side:.2f}".rstrip("0").rstrip(".")
        return result


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
