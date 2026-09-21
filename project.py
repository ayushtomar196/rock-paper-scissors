import random
player_score = 0
other_player_score = 0
for i in range(1,6):
    print("\n ROUND",i)
    player = input("ENTER rock , paper or scissors :")
    choices = ["rock","paper","scissors"]
    other_player = random.choice(choices)

    print("YOU CHOSE :",player)
    print("OTHER PLAYER CHOSE :",other_player)
    if player == other_player:
        print("IT IS A DRAW ") 
    elif player == "rock" and other_player == "scissors":
        print("YOU ARE A WINNER")
        player_score = player_score + 1
    elif player == "paper" and other_player == "rock":
        print("YOU ARE A WINNER")
        player_score = player_score + 1
    elif player == "scissors" and other_player == "paper":
        print("YOU ARE A WINNER")
        player_score = player_score + 1
    else:
        print("OTHER PLAYER WIN")
        other_player_score = other_player_score +1


    print("YOUR SCORE ",player_score)
    print("OTHER PLAYER SCORE ",other_player_score)
print("\n ========== FINAL SCORE ==============")
print("YOUR SCORE ",player_score)
print("OTHER PLAYER SCORE ",other_player_score)

if player_score > other_player_score:
    print("YOU WIN THE MATCH!")
elif other_player_score > player_score:
    print("OTHER PLAYER WINS THE MATCH!")
else:
    print("MATCH DRAW!")
