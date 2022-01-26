from ast import Return
from random import random


import random
word_list = ["python", "bootstrap","variable","integer","float", "string","print"]
random_word = random.choice(word_list)
print("Our Random Word Is: ")
print("********** WORD GUESSING GAME **********")
user_guesses = "_"
chances = 7
while chances > 0:
    wrong_guesses = 0
    for charecter in random_word:
        if charecter in user_guesses:
            print(f"{charecter}")
        else:
            wrong_guesses += 1
            print("_")
    if wrong_guesses == 0:
        #print("_")
        print(f"The Word Is:{random_word}")
        break
    guess = input("Please Guess A Letter: ")
    user_guesses += guess
    if guess not in random_word:
        chances -= 1
        print(f"Wrong. You Now Have Only {chances} Guesses Left.")
        if chances == 0:
            print(f"The Word Is : {random_word}")
            print("********** GAME OVER **********")
            print("**** THANK YOU FOR PLAYING ****")

print("********** GAME OVER **********")
print("**** THANK YOU FOR PLAYING ****")
