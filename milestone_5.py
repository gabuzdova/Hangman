import random
class Hangman:
    def __init__(self, word_list, num_lives):
        self.word=random.choice(word_list)
        self.word_guessed=list(len(self.word) * "_")
        self.num_letters=len(set(self.word))
        self.num_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]

    def check_guess(self, guess):
        guess=str(guess)
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for number, each_letter in enumerate(list(self.word)):
                if each_letter == guess:
                    templist = list(self.word_guessed)
                    templist[number] = each_letter
                    self.word_guessed= ''.join(templist)
                    print(self.word_guessed)
            self.num_letters-=1
            print(self.num_letters)
        else:
            self.num_lives-=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    def ask_for_input(self):
        
            guess= input("Guess a letter. \n")
            if len(guess)!=1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    def play_game(self,word_list):
        while True:
            if self.num_lives==0:
                print("You lost!")
                break
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break
            



game= Hangman( ["apple", "pineapple", "pear", "banana", "mangosteen"],5)
game.play_game(["apple", "pineapple", "pear", "banana", "mangosteen"])


#Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps

   # Create a variable called num_lives and assign it to 5
    #Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game
    #Pass word_list and num_lives as arguments to the game object
    #Create a while loop and set the condition to True. In the body of the loop, do the following:
     #   Check if the num_lives is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'
      ##  Next, check if the num_letters is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
        #If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'
