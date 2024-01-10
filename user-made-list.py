# Application where user can creat a list with the option to
# exclude any item he wants

import os   # To clear console
master_list = []  # The list created by the user
question_master = True   # To repeat or close the application
question_options = ""    # To decide to add or exclude an item
item_to_add = ""   # User input, item to add
number_in_item = None  # If there is a number in the input
item_to_remove = ""     # Item number to be removed

while question_master:

    question_options = input("Would you like to [a]dd item, [r]emove, [l]ist ou [c]lose? ").lower()

    if question_options == "a":
        item_to_add = input("Inform which item you would like to add to the list: ")
        
        # To prohibit an emptly input
        if item_to_add == "":
            os.system("cls")
            print("You didn't inform an item. Try again.")
        
        # To prohibit number or characters that are not a-z 
        elif item_to_add.isalpha() == False:
            os.system("cls")
            print("Please inform only characters from [a] to [z]. Try again.")
            
        else:
            # Adding item to list and reseting the question      
            master_list.append(item_to_add)
            os.system("cls")
            print(f"The item {item_to_add} was added to the list.")
        
    elif question_options == "r":
        item_to_remove = input("Which item would you like to remove, based on the index provided? ")
        
        # Making sure the input is an integer
        try:
            item_to_remove = int(item_to_remove)
            
        except:
            os.system("cls")
            print("You did not insert a number. Try again.")
            continue
        
        if item_to_remove == 0:
            os.system("cls")
            print("There is no number 0 in the index. Try again.")
            continue
        
        if item_to_remove > len(master_list):
            os.system("cls")
            print(f"There isn't a number {item_to_remove} on the list. Try again.")
            continue
        
        # The -1 makes the index start at 1, rather than 0 as is programming normal
        os.system("cls")
        print(f"You removed the item {item_to_remove}, which correspond to {master_list[item_to_remove - 1]}.")
        master_list.pop(item_to_remove - 1)
        
    elif question_options == "l":
        os.system("cls")
        # Showing the index starting from number 1, rather than 0
        for contagem, item in enumerate(master_list):
            print("Índex:", contagem + 1, "Item:", item)
        
    elif question_options == "c":
        os.system("cls")
        print("You shut down the application.")
        question_master = False
        
    else:
        os.system("cls")
        print("You did not input a valid option. Try again.")