import random


def rollDice(amount:int=2) -> list[int]:

    if amount<=0:
        raise ValueError
    
    rolls: list[int]=[]

    for i in range(amount):
        randomRoll:int=random.randint(1,6)
        rolls.append(randomRoll)
        
    return rolls


def main():

    while True:
        try:
            userInput: str= input("how many dice would you like to roll")

            if userInput.lower()=='exit':
                print("Thanks for Playing !")
                break
            
            print(rollDice(int(userInput)))
        

        except ValueError:
            print("Please enter a Valid Number")


if __name__=='__main__':
    main()
