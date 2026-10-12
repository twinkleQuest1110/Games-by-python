
import random

num = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("Guess a number between 1 and 100!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == num:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < num:
        print("📉 Too low! Try a higher number.")
    else:
        print("📈 Too high! Try a lower number.")
