import random as rnd

x = 6

while True:
    y = input(f"\nD? or press \"ENTER\" to roll again (D{x}): ")
    print()
    
    if (y == "exit" or y == "quit" or y == "q"): 
        break;
    if (y != ""):     
        try:
            x = int(y)
        except:
            print("Please enter a valid whole number.")
            continue

    print(rnd.randint(1,x))
