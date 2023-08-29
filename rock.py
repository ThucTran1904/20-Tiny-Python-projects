def rock():
    import random

    exit = False
    user_point = 0
    comp_point = 0

    print('')
    print('This is the Rock, Paper, Scissors games...')
    print('Rule: ')
    print('- Rock wins against scissors.')
    print('- Scissors beats paper')
    print('- Paper take down rock') 

    while exit == False:
        options = ["rock","paper","scissors"]

        user_input = input("Please choose rock, paper, scissors or exit in case you do not want to play anymore: ")
        computer_choice = random.choice(options)
        
        if user_input.lower() == "exit" :
            if user_point > 0 or comp_point > 0:
                if user_point > comp_point:
                    print(f"Score: Your score: {user_point} | Computer score: {comp_point}")
                    print('You win the whole game')
                    print('Thank you for coming')
                    print('Game ended')
                    quit()
                if  user_point < comp_point:
                    print(f"Score: Your score: {user_point} | Computer score: {comp_point}")
                    print('Hahaha computer win the whole game')
                    print('Thank you for coming :))')
                    print('Game ended')
                    quit()
                # exit = True or break or quit() has the same effect in this case
            else: 
                print('Thank you for coming')
                quit()

        if user_input.lower() == "rock":
            if computer_choice == "rock":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("It is a tie!")
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')
            elif computer_choice == "paper":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("Computer wins this round")
                comp_point += 1
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')
            elif computer_choice == "scissors":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("You win this round")
                user_point += 1
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')

        elif user_input.lower() == "paper":
            if computer_choice == "rock":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("You win this round")
                user_point += 1
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')

            elif computer_choice == "paper":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("it's a tie!")
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')

            elif computer_choice == "scissors":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("Computer wins this round")
                comp_point += 1
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')

        elif user_input.lower() == "scissors":
            if computer_choice == "rock":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("computer win!")
                comp_point += 1
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')

            elif computer_choice == "paper":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("You win this round")
                user_point += 1
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')

            elif computer_choice == "scissors":
                print(f"Your input is {user_input}")
                print(f"Computer input is {computer_choice}")
                print("its a tie")
                print(f"Current score: Your score: {user_point} | Computer score: {comp_point}")
                print('')

        elif user_input.lower() != " rock" or user_input.lower() != "paper" or user_input.lower() != "scissors":
            print("Invalid Input, please try it again")

rock()


