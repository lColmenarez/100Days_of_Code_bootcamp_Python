#Number Guessing Game Objectives:

from art import logo, game_over
from replit import clear
import random
print(logo)

def game(dificulty, attemps):
  """Function thats gets de dificulty and the attemps to get
     the parameters to initiate the logic"""
  game_off = False
  a = attemps
  random_number = random.randint(1,100)
  #print(random_number)
  while a != 0:
    user_number = int(input("please input a number between 1-100: "))
    if user_number == random_number:
      print(f"You got it, the number is: {random_number}")
    elif user_number < random_number:
      a -= 1
      print(f"Too low, you have {a} attemps left")
    else:
      a -= 1
      print(f"Too high, you have {a} attemps left")
      
#welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Chose a difficulty. Type 'easy or 'hard': ")
if choice == 'easy':
  game(choice, 10)
else:
  game(choice, 5)

clear()
print(game_over)