import random

chosen = input("Paper, scissors or rock? ")
options = ["paper", "scissors", "rock"]
against = random.choice(options)

if chosen == against:
    print("It's " + chosen + " against " + against + ". It's a tie")
elif (chosen == "paper" and against == "scissors") or (chosen == "rock" and against == "paper"):
    print("It's " + chosen + " against " + against + ". You lose :(")
else:
    print("It's " + chosen + " against " + against + ". You win!")

