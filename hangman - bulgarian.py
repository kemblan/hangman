#Zmiana importing the time module
import time

#welcoming the user
name = raw_input("Как се казваш?")

print "Здравей" + name, "Време е да играем бесеница?"

print ""

#wait for 1 second
time.sleep(1)

print "Започвай да отгатваш"
time.sleep(0.5)

#here we set the secret
word = "тайна"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print char,    

        else:
    
        # if not found, print a dash
            print "_",     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print "Ти спечели"  

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess = raw_input("познай буквата:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print "грешнно"    
 
    # how many turns are left
        print "ти имаш", + turns, 'още опити' 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "Ти губиш"
            print "Ти губиш" 