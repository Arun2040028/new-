import random

print("🎮 Welcome to Rock–Paper–Scissors!")
print("Choices: rock, paper, scissors")

# Get player choice
player_choice = input("Enter your choice: ").lower()

# Computer choice
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

print(f"\nYou chose: {player_choice}")
print(f"Computer chose: {computer_choice}\n")

# Determine winner
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("🎉 You win!")
else:
    print("💻 Computer wins!")

print("\nThanks for playing!")
