import random


def get_choice():
  # take player choice
  player_choice = input("Enter a choice (rock , paper, scissors) : ")
  # choice for bot
  options = ["rock", "paper", "scissors"]
  # get random choice for bot
  computer_choice = random.choice(options)
  # store both choice
  choices = {"player": player_choice, "computer": computer_choice}

  return choices


def check_win(player, computer):
  print(f"You chose {player}, Bot chose {computer} ")
  # saving conditional messages

  rock = "Rock smashes scissors !"
  paper = "Paper covers rock !"
  scissors = "Scissors cuts paper !"
  you_won = "You Win !"
  you_lost = "You Lose !"
  # checking for conditions

  if player == computer:
    return "It's a tie"
  # checking when player chose rock
  elif player == "rock":
    if computer == "scissors":
      return f"{rock} {you_won}"
    else:
      return f"{paper} {you_lost}"
  # checking when player chose paper
  elif player == "paper":
    if computer == "rock":
      return f"{paper} {you_won}"
    else:
      return f"{scissors} {you_lost}"
  # checkign when player chose paper
  elif player == "scissors":
    if computer == "paper":
      return f"{paper} {you_won}"
    else:
      return f"{rock} {you_lost}"


choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print("\n" + result)
