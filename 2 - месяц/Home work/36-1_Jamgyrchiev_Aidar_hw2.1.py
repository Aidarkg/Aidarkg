class Figure:
    unit = 'mm'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length

    def calculate_perimeter(self):
        perimeter = self.__side_length * 4
        self.perimeter = perimeter
        return self.perimeter

    def calculate_area(self):
        area = self.__side_length * self.__side_length
        return area

    def info(self):
        return f'Square side length: {self.__side_length} perimeter: {self.calculate_perimeter()} ' \
               f'area: {self.calculate_area()}'


class Rectangle(Figure):
    def __init__(self, lenght, wide):
        super(Rectangle, self).__init__()
        self.__length = lenght
        self.__width = wide

    def calculate_perimeter(self):
        perimeter = (self.__length + self.__width) * 2
        self.perimeter = perimeter
        return self.perimeter

    def calculate_area(self):
        area = self.__width * self.__length
        return area

    def info(self):
        return f'Rectangle length: {self.__length} width: {self.__width} perimeter: {self.calculate_perimeter()}' \
               f' area: {self.calculate_area()}'


square1 = Square(15)
square2 = Square(23)
rectangle1 = Rectangle(12, 20)
rectangle2 = Rectangle(5, 16)
rectangle3 = Rectangle(23, 40)
figure_list = [square1, square2, rectangle1, rectangle2, rectangle3]

for figure in figure_list:
    print(figure.info())
