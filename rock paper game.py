import random

def play_round():
    options = ["stone", "paper", "scissors"]

    print("\nChoose your move:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")

    choice = int(input("Enter choice (1-3): "))

    if choice == 1:
        user = "stone"
    elif choice == 2:
        user = "paper"
    elif choice == 3:
        user = "scissors"
    else:
        print("Invalid choice!")
        return None

    comp = random.choice(options)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {comp}")

    if user == comp:
        print("Result: Draw")
        return 0
    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        print("Result: You Win 🎉")
        return 1
    else:
        print("Result: Computer Wins 💻")
        return -1

def game():
    user_score = 0
    comp_score = 0
    round_no = 1 

    while True:
        result = play_round()

        if result == 1:
            user_score += 1
        elif result == -1:
            comp_score += 1

        print("\n--- SCORE BOARD ---")
        print(f"You: {user_score} | Computer: {comp_score}")
        
        round_no += 1   

        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {comp_score}")
            print("Game Over ")
            break


game()