class GuessNumber:

    def GuessGame(self,guessNumber):
        Guess = ""
        print("""
Number Guess game 
for Numbers between 1 to 15   
Give five chances...
        """)
        counter = 0
        Found = False
        while True:
            counter =counter+1
            if counter ==5:
                Found =True
                break
            Guess = int(input("Enter the Guess {}:-".format(counter)))
            if (Guess == guessNumber):
                Found= True
                print("You have find the Number ")
                break
            else:
                if(Guess > guessNumber):
                    print("Enter Lesser Number !")
                else:
                    print("Enter Bigger Number !")
        else:
            print("Game Over !")
