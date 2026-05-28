from math import pi
from shape import Shape


class Circle(Shape):
    def __init__(self, shape_id,radius, shape_type="Circle"):
        super().__init__(shape_id, shape_type)
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius  