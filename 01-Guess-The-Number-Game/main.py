
import random

computer = random.randint(1, 100)

while True:


    user = input(
      "Guess the number between 1 to 100 "
     " Quit(Q) :"
    )

    if (user.upper() == "Q"):
        print(
            "you quit the game"
            )
        
        break

    try:
        user = int(user)

        if user == computer:

            print(
                "correct guess"
                )
            
            break
            
        elif user > computer:

            print(
                "guess smaller number"
                )
            
        else:

            print(
                "guess bigger number"
                )
               
    except ValueError:

        print(
            "Invalid input! "
            " Please enter a number or Q."
            )
    
print("-------GAME OVER-------")                 
