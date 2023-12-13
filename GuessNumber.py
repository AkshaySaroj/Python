from random import randint

lower_num , Higher_num=1, 10  
randomNumber:int =randint(lower_num,Higher_num)

print("Guess a number between 1 to 10")

while True:
    try:
        userGuess:int=int(input("Guess"))

    except ValueError as e:
        print("Please enter a valid number")
        continue

    if userGuess > randomNumber:
        print("your guess is too high , make  a new guess!")
    elif userGuess < randomNumber:
        print("your guess lower than actual number")
    else:
        print("you have correctly guessed.")
        break
  