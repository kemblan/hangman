import time
name = raw_input("Podaj swoje imie?  ")

print "Witaj, " + name, "Czas zagrac w wisielca"

print ""

time.sleep(1)

print "zgadnij litere..."
time.sleep(0.5)

word = "sekret"

guesses = ''

turns = 10

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print char,

        else:
            print "_",

            failed += 1

    if failed == 0:
        print "Wygrales!"

	break

    print

    guess = raw_input("Odgadnij literę:")

    guesses += guess

    if guess not in word:
        turns -= 1
        print "Źle"
        print "Masz", + turns, "wiecej prob"
        if turns == 0:
            print "Przegrales"
