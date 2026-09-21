def player_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()

    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()

    return choice