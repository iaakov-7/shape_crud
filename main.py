#link for githab https://github.com/iaakov-7/shape_crud.git
from shape_manager import ShapeManager

manager = ShapeManager()

def show_menu():
    print("===Welcome to 'Shapes World===")
    print("""1. Add shape 
2. Show all shapes 
3. Update shape 
4. Delete shape 
0. Exit""")
    
def main():

    no_exit = True
    while no_exit:
        show_menu()
        choice_user = input("Enter your choice: ")
        match choice_user:
            case "1":
                if manager.create_shape() != "not valid":
                    print("Shape added successfully")                            
            case "2":
                manager.get_all_shapes()
            case "3":
                manager.update_shape()
                print("Shape updated successfully") 
            case "4":
                manager.delete_shape()
                print("Shape deleted successfully")
            case "0":
                no_exit =False
            case _:
                print("Please enter only numbers 0-4")    

main()