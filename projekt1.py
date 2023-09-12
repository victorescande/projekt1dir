import random
import os

while True:
    os.system("cls")
    rand=(random.randint(1, 100)) 
    print(rand)
    for i in range(7):
        try:
            guess = int(input("skriv in din gissning "))
        except:
            print("invalid input")
            continue
        if guess  == rand:
            print("\nrätt")
            break
        elif guess >= rand:
            print("\nförsök ett lägre tal \n")
        elif guess <= rand:
            print("försök ett högre tal \n")
        
    
    while True:
        answer = input("\nvill du fortsätta spela? (Y/N) ").upper()


        if answer == "Y":
            break
        elif answer == "N":
            exit()
        else:
            print("invalid input")
            pass

            



    

    
