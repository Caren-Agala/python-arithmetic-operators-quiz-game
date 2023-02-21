import random
guesses = 0  

top_of_range = input("Type a number that is the upper limit of your range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range < 0:
      print("Please enter a number greater than zero. ")  
      quit()
      
else:
    print("Please type a number. ")
    quit()
    
  
random_number = random.randint(0, top_of_range) 
  

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
      
    else:
        print("Please type a number. ")
        continue

    if user_guess == random_number:
        print("Congratulations! You got it right!")
    else:
        print("Incorrect. You got it wrong")
        if user_guess > random_number:
            print("You were above the number range!")
        else:
            print("You were below the number range!")

print("You got it in", guesses, "guesses")









# print(random_number)


# r = random.randrange(-1, 11)

# randrange can be replaced with randint
#randint generates the upper boundary number e.g 11 in this case while randrange does not generate the upper boundary number
# -1 and 11 stand for start and stop
# you can put 11 only and it will generate a random number from zero to either 10 or 11, for randrange

# print(r)
