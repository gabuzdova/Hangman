import random
class Hangman:
    def __init__(self, word_list, num_lives):
        self.random_word=random.choice(word_list)
        self.word_guessed=list(len(self.word) * "_")
        self.num_letters=len(set(self.word))
        self.num_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]

    def check_guess(self, guess):
        guess=str(guess)
        guess.lower()
        if guess in self.random_word:
            print(f"Good guess! {guess} is in the word.")
            for number, each_letter in enumerate(list(self.random_word)):
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



