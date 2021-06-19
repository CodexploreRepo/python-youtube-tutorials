import random
def get_choice(choice):
    if choice == "R":
        return "Rock"
    elif choice == "P":
        return "Paper"
    elif choice == "S":
        return "Scissor"
    else:
        return "Not a valid choice"

def main():
    print("Welcome to Rock, Paper, Scissor Game")
    print("[R]=Rock, [P]=Paper, [S]=Scissor and [Q]=Quit Game")

    choices = ["R", "P", "S"]
    counter = 1
    game_on = True

    while game_on:
        user_choice = input(f"Game #{counter}. Please enter your choice: ")
        user_choice = user_choice.upper()

        if user_choice == "Q":
            print('Thanks for joining ! Have a nice day :)')
            game_on = False
        else:
            random_index = random.randint(0,2)
            computer_choice = choices[random_index]

            print(f"You selected {get_choice(user_choice)} vs Computer choice is {get_choice(computer_choice)}")
            
            #Winning Rules:
            if user_choice == "R" and computer_choice == "S":
                print('Congrats, you win. Rock beats Scissor')
            elif user_choice == "P" and computer_choice == "R":
                print('Congrats, you win. Paper covers Rock')
            elif user_choice == "S" and computer_choice == "P":
                print('Congrats, you win. Scissor cuts Paper')
            elif user_choice == "R" and computer_choice == "P":
                print('So sorry, computer wins. Paper covers Rock')
            elif user_choice == "S" and computer_choice == "R":
                print('So sorry, computer wins. Rock beats Scissor')
            elif user_choice == "P" and computer_choice == "S":
                print('So sorry, computer wins. Scissor cuts Paper')
            elif user_choice == computer_choice:
                print(f"Wow ! It's a Draw. Both you and computer selected {get_choice(user_choice)}")
            else:
                print('Invalid option: Please enter [R, P, S or Q] only')

            counter+=1
        print("-"*40)
    
if __name__ == "__main__":
    main()