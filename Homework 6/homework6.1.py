import random

player1: str = str(input("enter your name:"))
player2: str = str(input("enter your name:"))
player3: str = str(input("enter your name:"))
player4: str = str(input("enter your name:"))
players = [player1, player2, player3, player4]
winner = random.choice(players)
print(f"the winner is:{winner}!")
