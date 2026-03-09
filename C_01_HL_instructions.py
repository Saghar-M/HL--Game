# checks users enter yes (y) or no (n)

def yes_no(question):

    """checks user response to a question is yes/ no(y/n), returns 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        # check the user says yes/no / y / n
        if response == "yes" or response == "y":
            return"yes"

        elif response == "no" or response == "n":
             return"no"
        else:
            print("please enter yes/no")

def instructions():
    """prints instructions"""

    print("""
*** Instructions ****

Roll the dice and try to win!    
    """)




# Main routine
print()
print("🔼🔼🔼 Welcome to the Higher Lower game🔻🔻🔻")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to see the instructions? ")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print()
print("program continues")






