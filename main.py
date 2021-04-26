from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def setDifficulty():
  level = input("Choose a diffulty level: Type e or h: ")
  if level == "e":
    return EASY_LEVEL
  else: 
    return HARD_LEVEL
  if level == "h":
    return HARD_LEVEL
  else:
    return EASY_LEVEL
  

def checkAnswer(guess, answer, turns):
  if guess > answer:
    print("It is too high")
    return
  elif guess < answer:
    print("It is too low")
    return
  else:
    print("You have the correct answer", answer)

def game():
  print("Choose a number between 1 - 100")
  answer = randint(1,100)
  turns = setDifficulty()
  gue
ss = 0
  while guess != answer:
    print("You have this many turns left:", turns)
    guess = int(input("Make a new guess: "))
    turns = checkAnswer(guess, answer, turns)
    if turns == 0:
      print("You have no more turns")
      return 
    elif guess != answer:
      print("Please try again")

game()
