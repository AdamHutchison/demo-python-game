from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        end("You should really learn how to type a number!")
        
    if how_much < 50:
        print("Nice you're not greedy, you win")
        exit(0)
    else:
        end("You knew this was too good to be true, you wake up.")

def unicorn_room():
    print("There is a unicorn here.")
    print("The unicorn has a bunch of flowers.")
    print("The unicorn is sat in front of another door.")
    print("How are you going to move the unicorn?")
    unicorn_moved = False

    while True:
        choice = input("> ")

        if choice == "take flowers":
            end("The unicorn looks at you in disgust. He sprinkles you with fairy dust and you wake up!")
        elif choice == "taunt unicorn" and not unicorn_moved:
            print("The unicorn has moved from the door.")
            print("You can go through it now.")
            unicorn_moved = True
        elif choice == "taunt unicorn" and unicorn_moved:
            end("The unicorn gets annoyed at you and makes you eat the flowers.")
        elif choice == "open door" and unicorn_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
    
def crocodile_room():
    print("Here you see a crocodile brushing his teath")
    print("He, turns and smiles at you with a menacing glare in his eyes")
    print("Do you flee for your life or ask it politely to come for lunch?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "ask" in choice:
        end("The crocodile comes to lunch and you spend the entire afternoon talking about politics. You become life long friends.")
    else:
        unicorn_room()

def end(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("The door to your left has a unicorn on it")
    print("The door to your right has a crocodile on it")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        unicorn_room()
    elif choice == "right":
        crocodile_room()
    else:
        end("You realise this is all a dream and wake up")

start()