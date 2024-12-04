# Guess the Number
import random
correctAnswer = random.randint(1, 100)
gameOver = False
compareAnswer = correctAnswer
while gameOver == False: 

    PlayerGuess = int(input("Guess a Number Between 1 and 100: "))

    if PlayerGuess == correctAnswer:
         compareAnswer = "Right"
         gameOver = True
    elif PlayerGuess > correctAnswer:
         compareAnswer = "High"
    elif PlayerGuess < correctAnswer:
         compareAnswer = "Low"

    if compareAnswer == "Right":
         print("Correct! You Win")
    elif compareAnswer == "High":
         print("it's Too High! Guess Again!")
    elif compareAnswer == "Low":
         print("Too Low! Guess Again!")