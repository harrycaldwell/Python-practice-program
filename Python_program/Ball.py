# import list
import random

# This is the list of responses that can be used in the program
responses = ["It is certain.",
             "It is decidedly so.",
             "Without a doubt.",
             "Yes definitely.",
             "You may rely on it.",
             "As I see it, yes.",
             "Most likely.",
             "Outlook good.",
             "Yes.",
             "Signs point to yes.",
             "Reply hazy, try again.",
             "Ask again later.",
             "Better not tell you now.",
             "Cannot predict now.",
             "Concentrate and ask again.",
             "Don't count on it.",
             "My reply is no.",
             "My sources say no.",
             "Outlook not so good.",
             "Very doubtful."
             ]
choice = "N"
while choice != "Y":
    print("Welcome to the Magic 8 ball!")
    question = input("What is it you would like to know? ")
    print("You said: " + question + ", is this correct? ")
    choice = input("Y=yes, N=No ")
    choice = choice.upper()

# Random list pick
rand = random.randint(0,19)
print(responses[rand])