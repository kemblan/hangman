from graphics import Graphics
from time import sleep
import random


class Hangman(object):

    def __init__(self, word):
        self.word = word
        self.used_letters = ""
        self.current_letter = ""

    @property
    def grid(self):
        grid = ""
        for i in self.word:
            if i in self.used_letters:
                grid += i
            else:
                grid += "_ "
        return grid

    def show_grid(self):
        print("Used Letters: " + self.used_letters)
        print("\n" + self.grid)

    def ask_letter(self):
        while True:
            letter = input("Guess a letter: ").lower()
            self.current_letter = letter
            if len(self.current_letter) > 1:
                print("\nYou have entered to many letters!")
            else:
                if self.current_letter in self.used_letters:
                    print("This letter has already been used!")
                    continue
                else:
                    self.used_letters += self.current_letter + " "
                    return "Letter Added"

    def check(self):
        if self.current_letter in self.word:
            if "_" in self.grid:
                return "Continue Game"
            else:
                return "Winner"

        else:
            return "Not a letter"

    def winner(self):
        print("\n")
        print("You have won!!")
        print("\nWould you like to play again?")
        reply = input("Y/N?").lower()
        if reply == "y":
            print("\n")
            main()
        else:
            print("Thank you for playing!")
            exit()

    def lost(self):
        print("\n")
        print("You have lost!")
        print(Graphics[0])
        print("The word was: " + self.word)
        sleep(2)
        print("\nWould you like to play again?")
        reply = input("Y/N?").lower()
        if reply == "y":
            print("\n")
            main()
        else:
            print("Thank you for playing!")
            exit()


def main():
    words = ["hello", "goodbye"]
    attempts = 8
    hangman = Hangman(random.choice(words))
    while attempts > 0:
        hangman.show_grid()
        hangman.ask_letter()
        hangman.check()
        if hangman.check() == "Winner":
            hangman.winner()
        if hangman.check() == "Not a letter":
            attempts -= 1
            print(Graphics[attempts])
            print("{0} attempts remain".format(attempts))
            print("\n")
    hangman.lost()


if __name__ == "__main__":
    main() 
