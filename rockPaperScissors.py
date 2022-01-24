import random, sys
print("Rock, Paper, Scissors")
wins = 0
losses = 0
ties = 0
while True:
    status = str(wins) + (" WINS, ") + str(losses) + (" LOSSES, ") + str(ties) + (" TIES")
    print(status)
    guide = "Enter your move: (r)ock (p)aper (s)cissor or (q)uit"
    print(guide)
    playerMove = input()

    if playerMove == ("r"):
        print("Rock versus...")
    elif playerMove == ("p"):
        print("Paper versus...")
    elif playerMove == ("s"):
        print("Scissors versus...") 
    elif playerMove == ("q"):
        print("Ara Ara Sayonara :)")
        sys.exit()     
    else: 
        print("please type r, p, s or q")

    gameGuess = random.randint(1, 3)
    if gameGuess == 1:
        computerMove = "r"
        print("Rock")
    elif gameGuess == 2:
        computerMove = "p"
        print("Paper") 
    elif gameGuess == 3:
        computerMove = "s"
        print("Scissors")

    if playerMove == computerMove :
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose")
        losses = losses + 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose")
        losses = losses + 1
    