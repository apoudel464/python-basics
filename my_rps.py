
while True:
    
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user
    # sem = input("enter your choice  Either \n  Rock   \t Paper \t scissors").lower()
    
    sem1  = input("enter your choice  Either \n  Rock-1   \t Paper-2 \t scissors-3 :\n")
    if sem1 == "rock" or sem1 == "1" or sem1 == "1":
        choice = 1
        print(choice)
        print('rock')
    elif sem1 == "paper" or sem1 == "2" or sem1 == "2":
        choice = 2
        print(choice)
        print('paper')
    elif sem1 == "scissors" or sem1 == "3" or sem1 == "3":
        choice = 3
        print(choice)
        print('scissor')
    else :
        print("Invalid choice")