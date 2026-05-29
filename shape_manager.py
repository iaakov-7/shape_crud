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
        print("Choose shape:\n1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Hexagon\n0. Exit")
        choice = input("enter choice: ") 
        match choice:
            case "1":
                shape_id = self.handele_new_id()
                side = int(input("Enter square side:  "))
                square_object = Square(shape_id,side)
                self.shapes.append(square_object)
                self.save_to_json()
            case "2":
                shape_id = self.handele_new_id()
                width = int(input("Enter rectangle width:  "))
                height = int(input("Enter rectangle height:  "))
                rectangle_object = Rectangle(shape_id,width,height)
                self.shapes.append(rectangle_object)
                self.save_to_json()
            case "3":
                shape_id = self.handele_new_id()
                base = int(input("Enter triangle base:  "))
                height = int(input("Enter triangle height:  "))
                side_a = int(input("Enter triangle side_a:  "))
                side_b = int(input("Enter triangle side_b:  "))
                side_c = int(input("Enter triangle side_c:  "))                                
                triangle_object = Triangle(shape_id,base,height,side_a,side_b,side_c)
                self.shapes.append(triangle_object)
                self.save_to_json() 
            case "4":
                shape_id = self.handele_new_id()
                radius = int(input("Enter circle radius:  "))
                circle_object = Circle(shape_id,radius)
                self.shapes.append(circle_object)
                self.save_to_json() 
            case "5":
                shape_id = self.handele_new_id()
                side = int(input("Enter hexagon side:  "))
                hexagon_object = Hexagon(shape_id,side)
                self.shapes.append(hexagon_object)
                self.save_to_json()
            case _:
                print("Please enter numbers 0-5.")                                                  
    
    def get_all_shapes(self): 
        for shape in self.shapes:
            shape = shape.to_dict()
            for key, value in shape.items():
                print(f"{key}: {value}") 
            print("*****")
    
    def update_shape(self, shape_id, new_data): 
        pass 
 
    def delete_shape(self): 
        is_not_valid = True
        while is_not_valid:
            shape_id = input("Enter shape id: ")
            if not self.validate_id(shape_id):
                print("ID most be a number")
            elif not self.is_id_exists(shape_id):
                print(f"ID: {shape_id} is not exists")
            else:
                is_not_valid = False
        for shape in self.shapes:
            if str(shape.id) == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                return            

    def validate_id(self,_id):
        return _id.isdigit()
            
          
    def is_id_exists(self,_id):    
        for shape in self.shapes:
            if str(shape.id) == _id:
                return True
              
    
    def handele_id_for_create(self):
            is_not_valid = True
            while is_not_valid:
                shape_id = input("Enter shape id: ")
                if self.is_id_exists(shape_id):
                    print("ID already exists choose another")
                else:
                    if self.validate_id(shape_id):
                        is_not_valid = False
                    else:
                        print("ID most be a number")   
            return int(shape_id)        
    
    def save_to_json(self): 
        with open("shapes.json","w",encoding="utf-8") as f:
            list_for_json = [shape.to_dict() for shape in self.shapes]
            json.dump(list_for_json,f)

 
    def load_from_json(self):
        try:   
            with open("shapes.json","r",encoding="utf-8") as f:
                content = json.load(f)
                if content == [None]:
                    return
                for shape in content:
                    shape_id = shape["id"]
                    if shape["shape_type"] == "Square":
                        shape_object = Square(shape_id,shape["side"])
                        self.shapes.append(shape_object)
                    elif shape["shape_type"] == "Rectangle":
                        shape_object = Rectangle(shape_id,shape["width"],shape["height"])
                        self.shapes.append(shape_object)
                    elif shape["shape_type"] == "Triangle":
                        shape_object = Triangle(shape_id,shape["base"],shape["height"],shape["side_a"],shape["side_b"],shape["side_c"])
                        self.shapes.append(shape_object)
                    elif shape["shape_type"] == "Circle": 
                        shape_object = Circle(shape_id,shape["radius"])
                        self.shapes.append(shape_object)
                    elif shape["shape_type"] == "Hexagon": 
                        shape_object = Hexagon(shape_id,shape["side"]) 
                        self.shapes.append(shape_object) 
        except (FileNotFoundError,json.JSONDecodeError):
            self.shapes = []                                        
if __name__ == "__main__":
    maneger = ShapeManager()
    maneger.delete_shape()
    