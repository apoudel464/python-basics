# import random module
import random
# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user
    # sem = input("enter your choice  Either \n  Rock   \t Paper \t scissors").lower()
    
    sem1  = input("enter your choice  Either \n  Rock-1   \t Paper-2 \t scissors-3 :\n")
    if sem1 == "rock" or sem1 == "1" or sem1 == "1":
        choice = 1
    elif sem1 == "paper" or sem1 == "2" or sem1 == "2":
        choice = 2
    elif sem1 == "scissors" or sem1 == "3" or sem1 == "3":
        choice = 3
    else :
        print("Invalid choice")

    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value

    # looping until user enter invalid input
    while choice == 3 or choice == 1 or choice == 2:
        choice = int(input('Enter a valid choice please '))

        # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

        # print user choice
    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

     # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Rock'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower()
    choice_name = " "
    if ans == 'n':
        break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
