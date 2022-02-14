# Import the random module
import random

# Generate a pseudo-random integer
random_number = random.randint(1,9)

# Ask the user for its name
name = input("What is your name?: ")

# Ask the user for its question
question = input("What is your question?: ")

answer = ""

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

if name == "":
    print("Question: {question}".format(question=question))
else:
    print("{name} asks: {question}".format(name=name, question=question))

if question == "":
    print("You did not input a question, please try again")
else:
    print("Magic 8-Ball's answer: {answer}".format(answer=answer))