import sys

def nearestMultiple(num):
    if num >= 4:
        return num + (4 - (num % 4))
    return 4

def lose1():
    print("\n\nYOU LOST!!")
    print("Until next time, GoodBye!!")
    sys.exit(0)

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i-1]) != 1:
            return False
        i += 1
    return True

def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        
        chance = input('> ').upper()
        
        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                print("\nYour Turn.")
                try:
                    inp = int(input("How many numbers would you wish to enter?(1-3)\n> "))
                except ValueError:
                    inp = 0
                
                if 1 <= inp <= 3:
                    comp = 4 - inp
                else:
                    print("Wrong input. You are disqualified from the game.")
                    lose1()
                    return  # Guard clause to prevent unbound execution
                    
                print("Enter your numbers.")
                for _ in range(inp):
                    xyz.append(int(input('> ')))
                    last = xyz[-1]
                      
                    if not check(xyz):
                        print("\nYou did not enter consecutive integers.")
                        lose1()
                    if last == 21:
                        lose1()
                            
                print("\nComputer's Turn.")
                for j in range(1, comp + 1):
                    xyz.append(last + j)
                print("Numbers after computer's turn:", xyz)
                last = xyz[-1]
                if last == 21:
                    print("\n\nCONGRATULATIONS!! YOU'VE WON!! ")
                    sys.exit(0)
                        
        elif chance == "S":
            comp = 1
            while True:
                print("\nComputer's Turn:")
                for j in range(1, comp + 1):
                    xyz.append(last + j)
                print("Numbers after computer's turn:", xyz)
                last = xyz[-1]
                
                if last == 21:
                    lose1()
                    
                print("\nYour Turn.")
                try:
                    inp = int(input("How many numbers would you wish to enter?(1-3)\n> "))
                except ValueError:
                    inp = 0
                    
                if not (1 <= inp <= 3):
                    print("Wrong input. You are disqualified from the game.")
                    lose1()
                
                print("Enter your numbers:")
                for _ in range(inp):
                    xyz.append(int(input('> ')))
                    last = xyz[-1]
                    
                    if not check(xyz):
                        print("\nYou did not enter consecutive integers.")
                        lose1()
                    if last == 21:
                        lose1()
                
                # Computer calculates its next move *after* the player finishes their entire turn
                near = nearestMultiple(last)
                comp = near - last 
                if comp == 4:
                    comp = 3
        else:
            print("Wrong choice. Please enter F or S")

# Main execution trigger
if __name__ == "__main__":
    print("Player 2 is Computer.")
    ans = input("Do you want to play the 21 number game? (Yes/No) \n> ")
    if ans.lower() == "yes":
        start1()
    else:
        print("You are quitting the game.....")