import random
player = input("ENTER rock , paper or scissors :")
choices = ["rock","paper","scissors"]
other_player = random.choice(choices)

if player == other_player:
    print("IT IS A DRAW ") 
elif player == "rock" and other_player == "scissors":
    print("YOU ARE A WINNER")   
elif player == "paper" and other_player == "rock":
    print("YOU ARE A WINNER")   
elif player == "scissors" and other_player == "paper":
    print("YOU ARE A WINNER")  
else:
    print("OTHER PLAYER WIN")
