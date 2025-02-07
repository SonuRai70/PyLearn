import random

def get_choices():
    player_choice = input("Enter the choice Rock,Paper, Or Scissor.")
    option = ['rock','paper','scissor']
    computer_choice = random.choice(option)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices


def check_win(player,computer):
    print("Your choice: ",player ,"\nComputer choice: ",computer)
    if player == computer: 
        return "its a tie"
    elif player == "rock":
        if computer == "scissor":
            return "rock smashes scissors you win"
        else:
            return "paper covers rock! you loose"
    elif player == "paper":
            if computer == "rock":
                return "paper covers rock you win "
            else:
                return "scissors cut paper you loose"
    elif player == "scissor":
        if computer == "rock":
            return "rock smashes scissors you win"
        else:
            return "scissors cut paper you win"
        
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
        
        
    

    
