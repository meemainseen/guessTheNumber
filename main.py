#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo
import os
# To display colorized text
from rich import print

# All is contained inside the only function in the code play_game()
def play_game():

  # Print a colorized logo
  print(f"[red]{logo}[/red]")

  # Print welcome statement and let the player choose difficulty level. 
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  level = input("Choose your level of difficulty. 'h' for hard or 'e' for easy: ")

  # Upon choosing easy player gets 10 tries, for level hard number of tries are 5
  if level == 'h':
    turns = 5
  elif level == 'e':
    turns = 10
  
  game_over = False

  # Computer chooses a random number between 1 and 100
  number = random.randint(1, 100)

  #print(f"For Testing Only. Computer chose {number}")

  # Allow the player to submit a guess for a number between 1 and 100.
  guess = int(input("Make a guess: "))
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  while not game_over:
    # If player guessed right the game is over and a winning message is displayed
    if guess == number:
      print(f"[blue]You got it! The answer was {number}[/blue]")
      game_over = True
    else:
      #If guess is greater than the number, print 'Too high', reduce number of tries by 1
      if guess > number:
        print("Too high")
        turns -= 1

      #If guess is less than the number, print 'Too low', reduce number of tries by 1
      elif guess < number:
        print("Too low")
        turns -= 1
      
      # If number of tries have exhausted, game ends and player is notified with the message.
      if turns == 0:
        print("[red]You ran out of tries. You loose[/red]")
        print(f"[red]The number was {number}[/red]")
        game_over = True

      # If number of tries are remaining let player try again.
      else:
        print(f"Number of turns remaining: {turns}")
        guess = int(input("Guess again: "))

# The loop to let the player replay the game or exit. 
while input("Play guess the number? 'y' for yes 'n' for pass: ") != 'n':
  os.system('clear')
  play_game()

  
