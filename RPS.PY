import random
username=input("what's your name?")
while True:
    choices= ["rock", "paper", "scissor"]
    alex=random.choice(choices)
    player=None

    while player not in choices:
        player=input("rock, paper or scissor:  ?").lower()

    if player == alex:          
        print("alex: ", alex)
        print("player: ",player)
        print("tie...!")
    elif player == "rock":
        if alex == "paper": 
            print("alex: ", alex)
            print("player: ", player)
            print("you loose! don't worry try again")
        if alex == "scissor":
            print("alex: ", alex)
            print("player: ", player)
            print("bravo!",username, "you won!")

    elif player == "scissor":
        if alex == "rock": 
            print("alex: ", alex)
            print("player: ", player)
            print("you loose! don't worry try again")
        if alex == "paper":
            print("alex: ", alex)
            print("player: ", player)
            print("bravo!",username, "you won!")

    elif player == "paper":
        if alex == "scissor": 
            print("alex: ", alex)
            print("player: ", player)
            print("you loose! don't worry try again")
        if alex == "rock":
            print("alex: ", alex)
            print("player: ", player)
            print("bravo!",username, "you won!")
    play_again=input("wanna play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("bye",username, "have a nice day!")
