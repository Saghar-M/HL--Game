import math


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



# cheks for na integer with optional upper /
# lower limits and an optional exit code for infinite mode
# quitting the game

def int_check(question, low=None, high=None, exit_code=None):
    while True:

        error = "please enter an integer that is 1 or more. "

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than / equal to 1
            if response <1:
                 print(error)
            else:
                return response


        except ValueError:
             print(error)


# calculate the maximum number of guesses
def calc_guesses(low,high):
    num_range = high - low + 1
    max_raw =math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses= max_upped + 1
    return max_guesses


# main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0


print("🔼🔼🔼 Welcome to the Higher Lower game🔻🔻🔻")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite:",
                       low=1,exit_code="")

if num_rounds == "infinite":
    mode ="infinite"
    num_rounds = 5

# Get Game parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings ( based on mode)
    if mode == "infinite":
        rounds_heading = f"\n 💿💿💿 Round {rounds_played +1} (infinite Mode) 💿💿💿 "
    else:
        rounds_heading = f"f\n 💿💿💿 Round {rounds_played +1} of {num_rounds} 💿💿💿 "

    print(rounds_heading)
    print()

    user_choice =  input("Choose: ")

    # if user choose, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area