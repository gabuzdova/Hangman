import random
word_list = ["apple", "pineapple","pear","cherry","peach"]
print(word_list)
word= random.choice(word_list)
print(word)
guess=input("Enter a single letter")
if len(guess)==1 and guess.isalpha()==True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
print("just trying to do change")
