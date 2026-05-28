import json
from square import Square
from rectangle import Rectangle
from hexagon import Hexagon
from triangle import Triangle
from circle import Circle


class ShapeManager: 
    def __init__(self): 
        self.shapes = [] 
        self.load_from_json() 
 
    def create_shape(self): 
        print("Choose shape:\n1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5.Hexagon")
        choice = input("enter choice: ") 
        match choice:
            case "1":
                shape_id = self.handele_id()
                side = int(input("Enter square side:  "))
                square_object = Square(shape_id,side)
                self.shapes.append(square_object)
                self.save_to_json()

    def get_all_shapes(self): 
        pass 
 
    def update_shape(self, shape_id, new_data): 
        pass 
 
    def delete_shape(self, shape_id): 
        pass 

    def validate_id(self,id):
        if not isinstance(id,int):
            raise ValueError("ID most be a number")
        for shape in self.shapes:
                if int(shape.id) == id:
                    raise ValueError("ID already exists choose another")
    
    def handele_new_id(self):
            is_not_valid = True
            while is_not_valid:
                try:
                    shape_id = int(input("Enter shape id: "))
                    self.validate_id(shape_id)
                    is_not_valid = False
                except ValueError as e:
                    print(f"Error: {e}")
            return shape_id        
    
    def save_to_json(self): 
        with open("shapes.json","w",encoding="utf-8") as f:
            list_for_json = [shape.to_dict() for shape in self.shapes]
            json.dump(list_for_json,f)

 
    def load_from_json(self): 
        with open("shapes.json","r",encoding="utf-8") as f:
            content = json.load(f)
            if content == [None]:
                return
            for shape in content:
                shape_id = shape["id"]
                if shape["shape_type"] == "Square":
                    shape_object = Square(shape_id,shape["side"])
                    self.shapes.append(shape_object)

if __name__ == "__main__":
    maneger = ShapeManager()
    maneger.create_shape()
    