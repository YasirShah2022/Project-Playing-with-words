### Setup Section ###
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if letter in actual:

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")


  
  



### Main Program ###
# Defining a funtion that will prompt an input from the user and only accept a six letter word and return the user's guessed input
def userGuess():
  guess = ""
  while (len(guess)) != 6:
    guess = input("Enter your guess: ")
  return guess


  
# Title and instructions printed to the console
print("*******Welcome to the word game challange!*******")
print()
print("Please guess a six letter word, you have six chances to guess the correct word.")
print()

# Manually selecting the secret word
secretWord = "accept"

# Setting the counter for attempts to zero
count = 0 


# Loop through the following code block if the count of attempts is less than six
while count < 6:
  # The guessed word will obtained through the use of predefined funtion
  guess = userGuess()
  # The following funtion is predefined to take the guess and the secret word as the argument and return the color coded response to the console showing the accuracy of letters/word
  printGuessAccuracy(guess, secretWord)
  print()
  if guess != secretWord:
    count += 1
  elif guess == secretWord:
    print("Congratulations you guessed correctly!")
    break
print()
if count == 6:
  print("Sorry you ran out of chances and lost :-(")   