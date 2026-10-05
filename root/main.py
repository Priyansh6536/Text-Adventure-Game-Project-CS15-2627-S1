import time

science_code = False
janitor_code = False
janitor_key = False
security_code = False
principal_key = False
exit_key = False
flashlight_found = False
map_acquired = False
win = False
start_time = time.monotonic()
position = "library"
one_room_choice = "1"
two_room_choices = ["1", "2"]
three_room_choices = ["1", "2", "3"]
four_room_choices = ["1", "2", "3", "4"]


def show_map():
    print("\n=============== SCHOOL MAP ==================")
    print("        [ Main Entrance ]     ")
    print("                |             ")
    print("        [Security Office]--[ Principal's Office]    ")
    print("                |             ")
    print("[Art Room]--[Main Hall]--[Comp Lab]")
    print("    |           |            |    ")
    print("[Janitor]   [Library]    [Science]")
    print("                |             ")
    print("           [Cafeteria]--[ Gym ]--[ Storage ]")
    print("===============================================\n")


print("You fell asleep in the school library!")
print("It's 9pm and everyone's gone home.")
print("You must find the code to the safe,")
print("acquire the master key and escape.")

while True:
    if position == "library":
        print("\nYour choices in the library are:")
        print("1. Go to the main hallway")
        print("2. Go to the cafeteria")
        if map_acquired:
            print("3. Check the map")
        else:
            pass
        response = input("\nWhat would you like to do?\n")
        if map_acquired:
            two_room_choices = ["1", "2", "3"]
        if response in two_room_choices:
            if response == "1":
                position = "main"
            elif response == "2":
                position = "cafeteria"
            elif response == "3":
                show_map()

        else:
            print("Invalid choice")

    elif position == "cafeteria":
        if flashlight_found:
            print("\nYour choices in the cafeteria are:")
            print("1. Go to the library")
            print("2. Go to gymnasium")
            if map_acquired:
                print("3. Check the map")
            else:
                pass
            response = input("\nWhat would you like to do?\n")
            if map_acquired:
                two_room_choices = ["1", "2", "3"]
            if response in two_room_choices:
                if response == "1":
                    position = "library"
                elif response == "2":
                    position = "gym"
                elif response == "3":
                    show_map()
            else:
                print("Invalid choice")
        else:
            print("\nYour choices in the cafeteria are:")
            print("1. Go to the library")
            print("2. Go to gymnasium")
            print("3. Look around for anything useful")
            response = input("\nWhat would you like to do?\n")
            if response in three_room_choices:
                if response == "1":
                    position = "library"
                elif response == "2":
                    position = "gym"
                elif response == "3":
                    flashlight_found = True
                    print("You found a working flashlight, perhaps it'll let you enter some previously inaccessible places!")
            else:
                print("Invalid choice")

    elif position == "gym":
        print("\nYour choices in the gym are:")
        print("1. Go to the storage shed")
        print("2. Go to the cafeteria")
        if map_acquired:
            print("3. Check the map")
        else:
            pass
        response = input("What would you like to do?\n")
        if map_acquired:
            two_room_choices = ["1", "2", "3"]
        if response in two_room_choices:
            if response == "1":
                position = "storage"
            elif response == "2":
                position = "cafeteria"
            elif response == "3":
                show_map()
        else:
            print("Invalid choice")

    elif position == "storage":
        if flashlight_found:
            if map_acquired == False:
                print("\nYour choices in the storage shed are:")
                print("1. Look around for anything useful")
                print("2. Go to the gymnasium")
                response = input("What would you like to do?\n")
                if response in two_room_choices:
                    if response == "1":
                        print("You look around and find an old map")
                        map_acquired = True
                    elif response == "2":
                        position = "gym"
                else:
                    print("Invalid choice")
            else:
                print("Your choices in the storage shed are:")
                print("1. Go to the gymnasium")
                if map_acquired:
                    print("2. Check the map")
                else:
                    pass
                response = input("What would you like to do?\n")
                if map_acquired:
                    one_room_choice = ["1", "2"]
                if response in one_room_choice:
                    if response == "1":
                        position = "gym"
                    elif response == "2":
                        show_map()
                else:
                    print("Invalid choice")
        else:
            print("You cannot explore this area yet, it isn't properly")
            print("lit so you go back to the gymnasium")
            position = "gym"

    elif position == "main":
        print("\nYour choices in the main hallway are:")
        print("1. Go to the library")
        print("2. Go to the art room")
        print("3. Go to the computer lab")
        print("4. Go to the security office")
        if map_acquired:
            print("5. Check the map")
        else:
            pass
        response = input("What would you like to do?\n")
        if map_acquired:
            four_room_choices = ["1", "2", "3", "4", "5"]
        if response in four_room_choices:
            if response == "1":
                position = "library"
            elif response == "2":
                position = "art"
            elif response == "3":
                position = "computer"
            elif response == "4":
                position = "security"
            elif response == "5":
                show_map()
        else:
            print("Invalid choice")

    elif position == "computer":
        if janitor_key is False:
            print("\nYour choices in the computer lab are:")
            print("1. Go to the science lab")
            print("2. Go to the main hallway")
            print("3. Search for something useful")
            if map_acquired:
                print("4. Check the map")
            else:
                pass
            response = input("\nWhat would you like to do?\n")
            if map_acquired:
                three_room_choices = ["1", "2", "3", "4"]
            if response in three_room_choices:
                if response == "1":
                    position = "science"
                elif response == "2":
                    position = "main"
                elif response == "3":
                    janitor_key = True
                    print(f"You find a key labeled 'Janitor' ")
                elif response == "4":
                    show_map()
            else:
                print("Invalid choice")
        else:
            print("\nYour choices in the computer lab are:")
            print("1. Go to the science lab")
            print("2. Go to main hallway")
            if map_acquired:
                print("3. Check the map")
                two_room_choices = ["1", "2", "3"]
            response = input("\nWhat would you like to do?\n")
            if response in two_room_choices:
                if response == "1":
                    position = "science"
                elif response == "2":
                    position = "main"
                elif response == "3":
                    show_map()
            else:
                print("Invalid choice")

    elif position == "science":
        if flashlight_found:
            if science_code is False:
                print("\nYour choices in the science lab are:")
                print("1. Look around for anything useful")
                print("2. Go to the computer lab")
                if map_acquired:
                    print("3. Check the map")
                    two_room_choices = ["1", "2", "3"]
                response = input("What would you like to do?\n")
                if response in two_room_choices:
                    if response == "1":
                        print("You look around and find a note")
                        print("It reads: '1st two are 37'")
                        science_code = True
                    elif response == "2":
                        position = "computer"
                    elif response == "3":
                        show_map()
                else:
                    print("Invalid choice")
            else:
                print("\nYour choices in the science lab are:")
                print("1. Go to the computer lab")
                print("2. Look at the strange note again")
                if map_acquired:
                    print("3. Check the map")
                response = input("What would you like to do?\n")
                if map_acquired:
                    two_room_choices = ["1", "2", "3"]
                if response in two_room_choices:
                    if response == "1":
                        position = "computer"
                    elif response == "2":
                        print("The note reads: '1st two are 37'")
                    elif response == "3":
                        show_map()
                else:
                    print("Invalid choice")
        else:
            print("You cannot explore this area yet, it isn't properly")
            print("lit so you go back to the computer lab")
            position = "computer"

    elif position == "art":
        print("\nYour choices in the art room are:")
        print("1. Go to the main hallway")
        print("2. Go to the Janitor's room")
        if map_acquired:
            print("3. Check the map")
        else:
            pass
        response = input("\nWhat would you like to do?\n")
        if map_acquired:
            two_room_choices = ["1", "2", "3"]
        if response in two_room_choices:
            if response == "1":
                position = "main"
            elif response == "2":
                position = "janitor"
            elif response == "3":
                show_map()

        else:
            print("Invalid choice")

    elif position == "janitor":
        if janitor_key:
            if janitor_code is False:
                print("\nYour choices in the janitor's room are:")
                print("1. Look around for anything useful")
                print("2. Go to the art room")
                if map_acquired:
                    print("3. Check the map")
                    two_room_choices = ["1", "2", "3"]
                response = input("What would you like to do?\n")
                if response in two_room_choices:
                    if response == "1":
                        print("You look around and find a note")
                        print("It reads: '2nd two are 90'")
                        janitor_code = True
                    elif response == "2":
                        position = "art"
                    elif response == "3":
                        show_map()
                else:
                    print("Invalid choice")
            else:
                print("\nYour choices in the janitor's room are:")
                print("1. Go to the art room")
                print("2. Look at the strange note again")
                if map_acquired:
                    print("3. Check the map")
                response = input("What would you like to do?\n")
                if map_acquired:
                    two_room_choices = ["1", "2", "3"]
                if response in two_room_choices:
                    if response == "1":
                        position = "art"
                    elif response == "2":
                        print("The note reads: '2nd two are 90'")
                    elif response == "3":
                        show_map()
                else:
                    print("Invalid choice")
        else:
            print("You cannot explore this area yet, it isn't unlocked")
            print("so you go back to the art room")
            position = "art"

    elif position == "security":
        if security_code is False:
            print("\nYour choices in the security office are:")
            print("1. Try to enter the code to the safe")
            print("2. Go to the main hallway")
            print("3. Go to the principal's office")
            print("4. Go to the entrance")
            if map_acquired:
                print("5. Check the map")
                four_room_choices = ["1", "2", "3", "4", "5"]
            response = input("What would you like to do?\n")
            if response in four_room_choices:
                if response == "1":
                    enter_code = input("What is the code to the safe")
                    if enter_code == "3790":
                        security_code = True
                        print("\nYou unlock the safe and find the key to the principal's office")
                        principal_key = True
                    else:
                        print("Invalid code")
                elif response == "2":
                    position = "main"
                elif response == "3":
                    position = "principal"
                elif response == "4":
                    position = "entrance"
                elif response == "5":
                    show_map()
            else:
                print("Invalid choice")
        elif security_code:
            print("\nYour choices in the security office are:")
            print("1. Go to the main hallway")
            print("2. Go to the principal's office")
            print("3. Go to the entrance")
            if map_acquired:
                print("4. Check the map")
                three_room_choices = ["1", "2", "3", "4"]
            response = input("What would you like to do?\n")
            if response in three_room_choices:
                if response == "1":
                    position = "main"
                elif response == "2":
                    position = "principal"
                elif response == "3":
                    position = "entrance"
                elif response == "4":
                    show_map()

    elif position == "principal":
        if principal_key is False:
            print("\nYou cannot access the principal's office,")
            print("to enter you must find the key locked in the safe")
            position = "security"
        elif principal_key:
            if exit_key:
                print("\nYour choices in the principal's office are:")
                print("1. Go to the security office")
                if map_acquired:
                    print("2. Check the map")
                    one_room_choice = ["1", "2"]
                response = input("What would you like to do?\n")
                if response in one_room_choice:
                    if response == "1":
                        position = "security"
                    elif response == "2":
                        show_map()
            else:
                print("\nYour choices in the principal's office are:")
                print("1. Go to the security office")
                print("2. Look around for anything useful")
                if map_acquired:
                    print("3. Check the map")
                    two_room_choices = ["1", "2", "3"]
                response = input("What would you like to do?\n")
                if response in two_room_choices:
                    if response == "1":
                        position = "security"
                    elif response == "2":
                        exit_key = True
                        print("You found the key to unlock the door at the front entrance")
                    elif response == "3":
                        show_map()

    elif position == "entrance":
        if exit_key:
            print("You now have the key to unlock the front door and leave.")
            print("Nice job escaping, you win the game.")
            win = True
            break
        else:
            print("You cannot do anything here yet,")
            print("find the key to the lock and come back to leave")
            position = "security"

elapsed_time = time.monotonic() - start_time
final_time = elapsed_time
print(f"Your time: ", {final_time}, "seconds")