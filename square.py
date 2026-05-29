from shape import Shape


class Square(Shape):
    def __init__(self, shape_id, side,shape_type="Square"):
        super().__init__(shape_id, shape_type)
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4   

