from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_id, width,height,shape_type="Rectangle"):
        super().__init__(shape_id, shape_type)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2    