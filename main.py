from art import logo
import random

"""
Checks the number greater than the guessed number or less.
"""

def intervalControl(number, guess):
  if guess < number:
    return "Too Low!\nGuess Again!"
  else:
    return "Too High!\nGuess Again!"
    
"""
Ask the start and end point to the user and return a random number for given interval.
"""

def randomNumReturner():
  
  start = int(input("Enter the start point of the interval."))
  end = int(input("Enter the end point of the interval."))
  
  randomNum = random.randint(start, end)

  return randomNum
  
print(logo)

print("Welcome to the NUMGUESS!\nI'm thinking of a number between 1 and 100!\n\n")


def play_game(attempts):
  randomNum = randomNumReturner()
  while attempts!=0:
    guess =int(input(f"You have {attempts} attempts remaining for guess the number!\nYour Guess :"))  
    if randomNum == guess:
      print(f"You found it! The actual number is {randomNum}.")
      break
    print(intervalControl(randomNum, guess))
    attempts-=1
  if attempts == 0:
    print(f"You lose! The actual number is {randomNum}.")

difficulty = input("Choose game difficulty.Write 'easy' or 'hard'.Your Choice :")
while difficulty !="easy" and difficulty !="hard":
  difficulty = input("Invalid Process!\nChoose game difficulty.Write 'easy' or 'hard'.Your Choice :")
  
if difficulty =="easy":
  play_game(10)
else:
  play_game(5)

  