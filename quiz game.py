print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's Play! :)")
score = 0
answer = input(" Which movie won 7 Oscars in 2022? ")
if answer.lower() == "everything everywhere all at once":
    print ("Correct!")
    score += 1
else:
    print("Incorrect! the right answer is everything everywhere all at once")

answer = input(" Who are the producers of the oscar awarded shortfilm The Elephant Whisperers? ")
if answer.lower() == "guneet monga and kartiki gonsalves":
    print ("Correct!")
    score += 1
else:
    print("Incorrect! the right answer is guneet monga and kartiki gonsalves")

answer = input(" Who is the Author of Pride and Prejudice? ")
if answer.lower() == "jane austen":
    print ("Correct!")
    score += 1
else:
    print("Incorrect! the right answer is Jane Austen")

answer = input(" Who wrote Looking For Alaska? ")
if answer.lower() == "john green":
    print ("Correct!")
    score += 1
else:
    print("Incorrect! the right answer is John Green")

answer = input(" How many Oscars did India win in the year 2022? ")
if answer.lower() == "two":
    print ("Correct!")
    score += 1
else:
    print("Incorrect! the right answer is Two")

print ("You got "+ str(score) +" questions correct!")
