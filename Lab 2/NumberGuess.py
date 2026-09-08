import random
def number_guessing_game():
    secret_no=random.randint(1,100)
    attempts=0
    max_attempts=7

    print("I have chosen a number")
    print("you have 7 chances to guess it")

    while attempts<max_attempts:
        guess=int(input("enter you guess"))

        if guess<1 or guess>100:
            print("please enter the number between 1 and 100")
            continue

        attempts+=1

        if guess<secret_no:
            print("number is too low")
        elif guess>secret_no:
            print("number is too high")
        elif guess==secret_no:
            print("CONGRATULATIONS!!!!! you guessed it right")
            print("Number of attempts:",attempts)
            return 
        
    print("\nYou have used all 7 attempts.")
    print("Better luck next time!")
    print("The correct number was:", secret_no)

if __name__=="__main__":
        number_guessing_game()