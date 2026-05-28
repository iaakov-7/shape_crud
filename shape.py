class Shape: 
   def __init__(self, shape_id, shape_type): 
       self.id = shape_id 
       self.shape_type = shape_type 
 
   def get_area(self): 
       pass 
 
   def get_perimeter(self): 
       pass 
 
   def to_dict(self): 
       data = self.__dict__.copy()
       data["area"] = self.get_area() 
       data["perimeter"] = self.get_perimeter() 