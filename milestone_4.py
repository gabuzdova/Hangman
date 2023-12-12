import random

class Hangman:

    def __init__(self, word_list, num_lives=5):    
        self.word_list=["apple", "pineapple", "pear", "banana", "mangosteen"]
        self.word=random.choice(word_list)
        self.the_letter_guessed_by_the_user=[]
        self.list_of_guesses=[]
        self.num_letters=0
        self.word_guessed=len(self.word) * "_"
    
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

    def check_guess (self, the_letter_guessed_by_the_user):
            self.the_letter_guessed_by_the_user.lower()
            if self.the_letter_guessed_by_the_user in self.word :
                print(f"Good guess! {self.the_letter_guessed_by_the_user} is in the word.")
                for each_letter in self.word:
                     if each_letter == the_letter_guessed_by_the_user:
                        self.word_guessed +=each_letter
                self.num_letters-=1          
            else:
                print(f"Sorry, {self.the_letter_guessed_by_the_user} is not in the word. Try again." )

print(Hangman.word_guessed)

#In the if block of your check_guess method, after your print statement, do the following:

 #   Create a for-loop that will loop through each letter in the word
  #  Within the for-loop, do the following:
   #     Create an if statement that checks if the letter is equal to the guess
    #    In the if block, replace the corresponding "_" in the word_guessed with the guess. HINT: You can index the word_guessed at the position of the letter and assign it to the letter
    #Outside the for-loop, reduce the variable num_letters by 1
