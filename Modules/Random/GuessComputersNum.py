import random 

computer_number = random.randint(1, 50)
print("Computer gussed number from 1 to 50.")
attempts = 1

while attempts <= 5:
    try:
        guessing_number = int(input(f"Attempt {attempts}/5 - Your guess: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if guessing_number > computer_number:
        print("Your number is greater then computer number!!!")
    elif guessing_number < computer_number:
        print("Your number is smaller then computer number!!!")
    else:
        print(f"Congratulations!!! You guessed the number {computer_number} in {attempts} attempts!!!")
        break

    attempts += 1

if attempts > 5:
    print("Your used your attempts :(\nTry again another time :)")