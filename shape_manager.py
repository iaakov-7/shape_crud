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
        print("Choose shape:\n1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Hexagon")
        choice = input("enter your choice: ") 
        match choice:
            case "1":
                shape_id = self.handle_id_for_create()
                side = self.get_positive_int("Enter square side:  ")
                square_object = Square(shape_id,side)
                self.shapes.append(square_object)
                self.save_to_json()
            case "2":
                shape_id = self.handle_id_for_create()
                width = self.get_positive_int("Enter rectangle width:  ")
                height = self.get_positive_int("Enter rectangle height:  ")
                rectangle_object = Rectangle(shape_id,width,height)
                self.shapes.append(rectangle_object)
                self.save_to_json()
            case "3":
                shape_id = self.handle_id_for_create()
                base = self.get_positive_int("Enter triangle base:  ")
                height = self.get_positive_int("Enter triangle height:  ")
                side_a = self.get_positive_int("Enter triangle side_a:  ")
                side_b = self.get_positive_int("Enter triangle side_b:  ")
                side_c = self.get_positive_int("Enter triangle side_c:  ")                                
                triangle_object = Triangle(shape_id,base,height,side_a,side_b,side_c)
                self.shapes.append(triangle_object)
                self.save_to_json() 
            case "4":
                shape_id = self.handle_id_for_create()
                radius = self.get_positive_int("Enter circle radius:  ")
                circle_object = Circle(shape_id,radius)
                self.shapes.append(circle_object)
                self.save_to_json() 
            case "5":
                shape_id = self.handle_id_for_create()
                side = self.get_positive_int("Enter hexagon side:  ")
                hexagon_object = Hexagon(shape_id,side)
                self.shapes.append(hexagon_object)
                self.save_to_json()    
            case _:
                print("You can enter only numbers 1-5")
                return "not valid"                                                  
    
    def get_all_shapes(self):
        if not self.shapes:
            print("There are no shapes to show") 
        for shape in self.shapes:
            shape = shape.to_dict()
            for key, value in shape.items():
                print(f"{key}: {value}") 
            print("*****")
    
    def update_shape(self): 
        shape_id = self.handle_id_for_delete_or_update() 
        for shape in self.shapes:
            if str(shape.id) == shape_id:
                shape_to_update = shape
                match shape_to_update.shape_type:
                    case "Rectangle":
                        shape_to_update.width = self.get_positive_int("Enter a new width: ")
                        shape_to_update.height = self.get_positive_int("Enter a new height: ")
                    case "Square":    
                        shape_to_update.side = self.get_positive_int("Enter a new side: ")
                    case "Triangle":
                        shape_to_update.base = self.get_positive_int("Enter a new base: ")
                        shape_to_update.height = self.get_positive_int("Enter a new height: ")
                        shape_to_update.side_a = self.get_positive_int("Enter a new side_a: ")
                        shape_to_update.side_b = self.get_positive_int("Enter a new side_b: ")
                        shape_to_update.side_c = self.get_positive_int("Enter a new side_c: ")
                    case "Circle":
                        shape_to_update.radius = self.get_positive_int("Enter a new radius: ")  
                    case "Hexagon":      
                        shape_to_update.side = self.get_positive_int("Enter a new side: ")
                self.save_to_json()
              
    def delete_shape(self): 
        shape_id = self.handle_id_for_delete_or_update()
        for shape in self.shapes:
            if str(shape.id) == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                return            
    
    def get_positive_int(self,message):
        while True:  
            try:
                value = int(input(message))
                if value > 0:
                    return value
                print("Number must be > 0")
            except ValueError:
                print("Please enter a valid number")    
    
    def validate_id(self,_id):
        return _id.isdigit()
            
          
    def is_id_exists(self,_id):    
        for shape in self.shapes:
            if str(shape.id) == _id:
                return True
              
    def handle_id_for_delete_or_update(self):
        is_not_valid = True
        while is_not_valid:
            shape_id = input("Enter shape id: ")
            if not self.validate_id(shape_id):
                print("ID must be a number")
            elif not self.is_id_exists(shape_id):
                print(f"ID: {shape_id} is not exists")
            else:
                is_not_valid = False
        return shape_id
    
    def handle_id_for_create(self):
            is_not_valid = True
            while is_not_valid:
                shape_id = input("Enter shape id: ")
                if self.is_id_exists(shape_id):
                    print("ID already exists choose another")
                else:
                    if self.validate_id(shape_id):
                        is_not_valid = False
                    else:
                        print("ID must be a number")   
            return int(shape_id)        
    
    def save_to_json(self): 
        with open("shapes.json","w",encoding="utf-8") as f:
            list_for_json = [shape.to_dict() for shape in self.shapes]
            json.dump(list_for_json,f)

 
    def load_from_json(self):
        try:   
            with open("shapes.json","r",encoding="utf-8") as f:
                content = json.load(f)
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

    