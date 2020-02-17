
def entering_code(item=None):
    door_unlocked = False
    if not door_unlocked:
        if item is None:
            password = ""
            print("It's asking for a password.")
            while len(password) < 6:
                number = input("")
                for digit in number:
                    if digit not in "0123456789":
                        print("ERROR!")
                        print("Oops! Wrong button.")
                        break
                else:
                    password += number

            if password == "404167":
                print("That Password is accepted. The door is open now!")
                door_unlocked = True
                return False
            else:
                print("That was not accepted... I wonder what the code is?")
                return False
        elif item == "soda":
            print("You dump the soda on the code box.")
            print("It fizzles and sparks. The door opens.\nHuh? Can't believe that worked.")
            door_unlocked = True
            return True
        else:
            print("That doesn't help me...")
            return False
    else:
        print("It's open. I don't have to do anything else with it.")
        return False


print("the correct code is 404167.")
entering_code()
