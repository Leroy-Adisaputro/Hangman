from random_word import RandomWords
from string import ascii_lowercase

r = RandomWords()
r.get_random_words()
guesses = " "

def attempts():
  while True:
      no_attempts = int(input("How many wrong guesses would you like to get? Please select a number between 1 and 20\n"))
      if 1 <= no_attempts <= 20:
        print("You have chosen", no_attempts, "tries!")
        return no_attempts
      elif no_attempts <= 1:
        print("That is too little attempts!")
      elif no_attempts >= 20:
        print("That is too many attempts!")
      else:
        print("Error")

def min_word_len():
  while True:
    min_len = int(input("Choose a minimum word length! Please select a number between 4 and 8\n"))
    if 4 <= min_len <= 8:
      print("You have chosen a minimum length of", min_len)
      return min_len
    elif min_len <= 4:
      print("That is too short of a minimum length!")
    elif min_len >= 8:
      print("That is too long of a minimum length!")
    else:
      print("Error")

def guessing():
  global guesses
  attempts_remaining = attempts()
  diff = min_word_len()
  print("Selecting random word...")
  word = r.get_random_word(minLength = (diff - 1))
  while attempts_remaining > 0:
    failed = 0
    for char in word:
      if char in guesses:
        print(char)
      else:
        print("_")
        failed += 1

    if failed == 0:
      print("You win!")
      choice = input("Would you like to play again? Yes//No\n").lower()
      if "yes" in choice:
        play_hangman()
      elif "no" in choice:
        exit()
      else:
        print("Error")

    guess = input("Guess a character:")
    guesses += guess

    if guess not in word:
      attempts_remaining -= 1
      print("Wrong!")
      print(guess, " was not a letter!")
      print("You have", attempts_remaining,  "more guesses.")
      
      if attempts_remaining == 0:
        print("You lose!")
        choice = input("Would you like to play again? Yes//No\n").lower()
        if "yes" in choice:
          play_hangman()
        elif "no" in choice:
          exit()
        else:
          print("Error")

def play_hangman():
  key = input("Play hangman? Yes//No\n").lower()
  if key == "yes":
    guessing()
  elif key == "no":
    print("Exiting game!")
    exit()
  else:
    print("Error that is an invalid choice!")

play_hangman()