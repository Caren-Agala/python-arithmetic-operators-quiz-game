import pdb
import time
print("Welcome to my math quiz!")

playing = input("Do you want to play the game? (y/n): ")
score = 0

if playing.lower() != "y":
    quit()
print("Sure! Let\'s play : )") 

# if playing.lower() != "yes":
#     quit()
# print("Sure! Let\'s play : )") 

time.sleep(1)

answer = input("What is 4**2? ")
if answer == "16":
    print("Correct!")
    score += 1
    print("Score: " + str(score))
else:
    print("Incorrect!")
    score = score
    print("Score: " + str(score))
time.sleep(1)    

answer = input("What is 4*2? ")
if answer == "8":
    print("Correct!")
    score += 1
    print("Score: " + str(score))
else:
    print("Incorrect!")
    score = score
    print("Score: " + str(score))
time.sleep(1)   
    
answer = input("What is 4/2? ")
if answer == "2":
    print("Correct!")
    score += 1
    print("Score: " + str(score))
else:
    print("Incorrect!")
    score = score
    print("Score: " + str(score))
time.sleep(1)   
    
answer = input("What is 4%2? ")
if answer == "0":
    print("Correct!")
    score += 1
    print("Score: " + str(score))
else:
    print("Incorrect!")
    score = score
    print("Score: " + str(score))
time.sleep(1)

print("Your final score is: " + str(score))
print("Your final score is: " + str((score/4)*100) + " %")
print("Congratulations!")