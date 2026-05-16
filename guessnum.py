import random 
 
print('Greetings, Welcome to this number guessing game!')
print('You will have 7 chages to guess the number, Lets start')

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound:"))

print(f"You have 7 guesses number between {low} and {high}.")

number = random.randint(low, high)

chances = 7 #total chances
guess_counter = 0  #counter for guesses


while guess_counter < chances:
    guess_counter += 1
    guess = int(input("Enter your guess:"))
    
    if guess == number:
        print(f"Correctly guessed, the number is {number}. You guessed it in {guess_counter} attempts")
        break
    elif guess_counter >= chances:
        print(f"Sorry!, The number was {number}. Better luck next time.")
    elif guess > number:
        print("Too high! Try a lower number.")
    elif guess < number:
        print("Too low! Try a higher number.")    
    