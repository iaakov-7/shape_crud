from math import sqrt
from shape import Shape


class Hexagon(Shape):
    def __init__(self, shape_id,side, shape_type="Hexagon"):
        super().__init__(shape_id, shape_type)
        self.side = side
            
    def get_area(self):
        return (3 * sqrt(3) * self.side ** 2) / 2
    
    def get_perimeter(self):
        return self.side * 6       
