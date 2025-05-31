import random
number_to_guess=random.randint(1,100) #import random and it will pick a number between 1 to 100 

while True: #add a while such that the loop continue until user input match the random
    try: #try if the user enter values like characters,etc... to except it 
        guess=int(input("Guess the number between 1 to 100\n"))
        if guess < number_to_guess: 
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulation!You guessed the number correctly")
            break
    except ValueError:
        print("Please enter a valid number")
    






    
    

