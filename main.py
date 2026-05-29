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
        choice_user = input("Enter yuor choice: ")
        match choice_user:
            case "1":
                try:
                    manager.create_shape()
                    print("Shape added successfully")
                except ValueError:
                    print("Error: All shape data must be numbers.")                            
            case "2":
                manager.get_all_shapes()
            case "3":
                try:
                    manager.update_shape()
                    print("Shape updated successfully") 
                except ValueError:
                    print("Error: All shape data must be numbers.")
            case "4":
                manager.delete_shape()
                print("Shape deleted successfully")
            case "0":
                no_exit =False

main()