from random import randint


print("""Welcome to the Number Guessing Game! 
I'm thinking of a number between 1 and 100.""")

choice = input("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n""")


chosen = randint(1,100)


match choice.strip().lower():
    case "1" | "easy":
        guesses = 10
    case "2" | "medium":
        guesses = 5
    case "3" | "hard":
        guesses = 3
    case _:
        print("Please enter a valid choice\n")
        exit()

while guesses > 0:
    print(f"you have {guesses} guesses\n")

    try:
        guess = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess == chosen:
        print("You win!")
        exit()
    elif guess < chosen:
        print("Higher\n")   
    else:
        print("Lower\n")
        
    guesses -= 1

print(f"You lose! The number was {chosen}")
