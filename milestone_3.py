def ask_for_input():

    while True:
        guess= input("Please guess a letter.\n")
        if guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
word= "hello"
def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again." )
ask_for_input()