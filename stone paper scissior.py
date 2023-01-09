print("welcome to the game ")
print('rule for the game'
      'rock>>scissor '
      "scissor>>paper"
      "paper>>>rock")
print("rock = R ")
print("paper = P")
print("scissor = S")
player1 = input("chance of player 1")
player2 =input("chance of player 2")
if player1 == "R" and player2 == "S":
    print("player 1 WON")
break
if player1 == "R" and player2 == 'P':
    print("player 2 WON")

if player1 == " P" and player2 == " R":
    print("player 1 WON ")
elif player1 == "P" and player2 == "S":
    print("player 2 WON")
elif player1 == "S" and player2 == 'R':
    print("player 2 WON")
elif player1 == "S" and player2 == "P ":
    print("player 1 WON ")
elif player2 == "R" and player1 == "S":
    print("player 2 WON")
elif player2 == "R" and player1 == 'P':
    print("player 1 WON")
elif player2 == " P" and player1 == "R ":
    print("player 2 WON ")
elif player2 == "P" and player1 == "S":
    print("player 1 WON")
elif player2 == "S" and player1 == 'R':
    print("player 1 WON")
elif player2 == "S" and player1 == "P ":

    print("player 2 WON ")
