import random

class Hangman:

    def __init__(self, word_list, num_lives=5):    
        self.word_list=["apple", "pineapple", "pear", "banana", "mangosteen"]
        self.word=random.choice(word_list)
        self.word_guessed=[]
        self.list_of_guesses=[]
        self.num_letters=[]
    
    def ask_for_input(self):
            while True:
                guess_the_letter= input("Please guess a letter.\n")
                if guess_the_letter.isalpha():
                    break
                elif guess_the_letter in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess()
                    self.list_of_guesses.append(guess_the_letter)

    def check_guess (self,word_guessed):
            self.word_guessed.lower()
            if self.word_guessed in self.word :
                print(f"Good guess! {self.word_guessed} is in the word.")
            else:
                print(f"Sorry, {self.word_guessed} is not in the word. Try again." )

    ask_for_input(None)


 
    #Create an elif statement that checks if the guess is already in the list_of_guesses
  #  In the body of the elif statement, print a message saying "You already tried that letter!"

#If the guess is a single alphabetical character and it's not already in the list_of_guesses, create an else block and call the check_guess method. Remember to pass the guess as an argument to this method.

#Finally, append the guess to the list_of_guesses.
#Ensure you do this in the else block of this function, rather than inside the check_guess method, so that the letter can be appended to the list_of_guesses in both conditions.

#Step 3:
#Call the ask_for_input method to test your code. 