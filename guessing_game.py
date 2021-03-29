import random


def start_game():
    tries = 0
    high_score = []
    random_no = random.randint(1, 10)

    print( """ 
_____________________________________
Welcome to the Number Guessing Game!
_____________________________________ 

""") 

    while True:

        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if guess <= 0 or guess > 10:
                print("That number isn't between 1 and 10, please try again...")
                continue
        except ValueError:
            print("oh no, That's not a valid value. Try again...")
        else:
            if guess == random_no:
                tries += 1
                high_score.insert(0, tries)
                min_score = min(high_score)
                print("")
                print("You got it! It took you {} tries".format(tries))
                play_again = input("Would you like to play again? [y]es/[n]o:  ")
                if play_again.lower() == 'y':
                    random_no = random.randint(1, 10)
                    print("")
                    print("The HIGHSCORE is {}".format(min_score))
                    print("---------------------")
                    tries = 0
                    continue

                else:
                    print("Closing game, see you again soon!")
                    break
            elif guess > random_no:
                tries += 1
                print("It is Lower!")
                continue
            elif guess < random_no:
                tries += 1
                print("It is Higher!")
                continue

# Kick off the program by calling the start_game function.


start_game()
