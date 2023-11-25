class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius**2

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area():.2f}{self.unit}.")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * self.__side_a * self.__side_b

    def info(self):
        print(f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, "
              f"area: {self.calculate_area()}{self.unit}.")


circles = [Circle(2), Circle(3)]
triangles = [RightTriangle(5, 8), RightTriangle(3, 4), RightTriangle(6, 9)]

for circle in circles and triangles:
    circle.info()
