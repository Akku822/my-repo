i=1
print("No of guess is limited to 9 only")
while(i<=9):
    a = int(input("Please guess the no: "))
    if a<25:
        print("You guess is lower number than expected")
    elif a>25:
        print("You guess is higher number than expected")
    else:
        print("Congratulations you guessed it correctly")
        break
    i=i+1
    print(10-i,"No of guess left")
if(i>9):
    print("You exceeded no of guesses and hence Game is over")