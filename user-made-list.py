# Application where user can creat a list with some options:
# add, delete, list, close, undo and redo

import os   # To clear console
import json # To save and retrieve a list on your computer
master_list = []  # The list created by the user
undo_redo_list = [] # List to undo and redo itens into the main list
question_options = ""    # To decide to add or exclude an item
item_to_add = ""   # User input, item to add
item_to_delete = ""     # Item number to be deleted

# Function to present the list of already made itens, used twice in the code
def list():
    if not master_list:
        print("No item to show.")
    # Showing the index starting from number 1, rather than 0
    for contagem, item in enumerate(master_list):
        print("Índex:", contagem + 1, "Item:", item)

question_options = input("Is there a list you want to retrieve? [Y]es or [N]o ").lower()

match question_options:
    case "y":
        os.system("cls")
        try:
            with open("user-made-list_savefile.json", "r") as file:
                master_list = json.load(file)
                print("The data retrieved was the following:")
                list()
                print()
        except:
            print("There is not a save file to load.")
            question_options = None
    case "n":
        os.system("cls")
        question_options = None

while True:

    question_options = input("Please select between: \n[a]dd\n[l]ist\n[d]elete\
\n[u]ndo\n[r]edo\n[c]lose\n-> ").lower()
    
    match question_options:
        
        case "a":
            os.system("cls")
            item_to_add = input("Inform which item you would like to add to the list: ")
            
            # To prohibit an emptly input
            if item_to_add == "":
                os.system("cls")
                print("You didn't inform an item. Try again.")
                print()
            
            else:
                # Adding item to list and reseting the question      
                master_list.append(item_to_add)
                os.system("cls")
                print(f"The item {item_to_add} was added to the list.")
                print()
        
        case "d":
            os.system("cls")
            list()
            item_to_delete = input("Which item would you like to delete, based on the index provided? ")
        
            # Making sure the input is an integer
            try:
                item_to_delete = int(item_to_delete)
            
            except:
                os.system("cls")
                print("You did not insert a number. Try again.")
                print()
                continue

            if item_to_delete == 0:
                os.system("cls")
                print("There is no number 0 in the index. Try again.")
                print()
                continue
        
            if item_to_delete > len(master_list):
                os.system("cls")
                print(f"There isn't a number {item_to_delete} on the list. Try again.")
                print()
                continue
        
            # The -1 makes the index start at 1, rather than 0 as is programming normal
            os.system("cls")
            print(f"You deleted the item {item_to_delete}, which correspond to {master_list[item_to_delete - 1]}.")
            print()
            master_list.pop(item_to_delete - 1)
        
        case "l":
            os.system("cls")
            list()
            print()
            
        case "c":
            
            os.system("cls")
            question_options = input("Do you want to [s]ave your list? ").lower()
            
            match question_options:
                
                case "s":
                    os.system("cls")
                    
                    with open("user-made-list_savefile.json", "w", encoding="utf8") as file:
                        json.dump(master_list, file)
                    print("List saved successfully. Application shutting down now.")
                    break
                case _:
                    os.system("cls")
                    print("You shut down the application.")
                    break
        
        case "u":
            
            if master_list == []:
                os.system("cls")
                print("There isn't any item on the list to undo.")
                print()
                continue
            
            os.system("cls")
            undo_redo_list.append(master_list[-1])
            print(f"You removed the item {master_list[-1]} from the list.")
            master_list.pop()
            
        case "r":
            
            if undo_redo_list == []:
                os.system("cls")
                print("You didn't undo any item to redo.")
                print()
                continue
            
            os.system("cls")
            print(f"You inserted back the item {undo_redo_list[-1]} to the list.")
            master_list.append(undo_redo_list[-1])
            undo_redo_list.remove(undo_redo_list[-1])
            
        case _:
            os.system("cls")
            print("You did not input a valid option. Try again.")
            print()