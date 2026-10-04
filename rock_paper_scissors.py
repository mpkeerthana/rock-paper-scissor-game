import random
print("Rock-Paper-Scissors Game!")
print("Rules:")
print("1. Rock beats Scissors")
print("2. Scissors beats Paper")
print("3. Paper beats Rock")

while True:

   user=input("Enter Rock, Paper, or Scissors : ").lower()

   if user not in ["rock", "paper", "scissors"]:
       print("Invalid input. Please try again.")
       continue

   computer=random.choice(["rock", "paper", "scissors"])

   print("computer chose: ", computer)

   if user == computer:
       print("It's a tie!")

   elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
       print("You win!")

   else:
       print("Computer wins!")

   while True:
       again = input("Do you want to play again? (yes/no): ").lower()

       if again == "yes":
           break

       elif again == "no":
           print("Game over!")
           exit()

       else:
           print("Invalid input. Please enter 'yes' or 'no'.")