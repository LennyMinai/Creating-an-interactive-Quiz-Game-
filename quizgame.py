print ("Welcome to the Quiz Game!")
playing= input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("awesome! Let's Go...")
score=0

answer = input("What is the capital city of France? ")
if answer.lower()==("paris"):
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("Who was the former president of the USA before Biden? ")
if answer.lower()==("trump"):
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the most popular language in the USA? ")
if answer.lower()==("english"):
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("Which is the largest planet in our solar system? ")
if answer.lower()==("jupiter"):
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")

print("Congrats! That's " + str((score/4)*100) + "% of the questions")

