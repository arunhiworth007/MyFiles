from random import randint
from guessRandonvalue import GuessNumber


class MyClass:
    @staticmethod
    def GuessGame():
        guessNumber = randint(1, 15)
        obj = GuessNumber()
        obj.GuessGame(guessNumber)


MyClass.GuessGame()
