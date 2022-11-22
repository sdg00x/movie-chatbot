import random
# This is a list of responses the bot would give to a user when it doesn't understand the user inputs
def random_responses():
    random_list = [
        "Please try being more descriptive",
        "Sorry I do not understand that",
        "Could you please rephrase that ",
        "I am sorry, I didn't get that ",
        "Could you please rephrase that?",
        "Sorry I didn't catch that, is there anything else I could help you with?",
        ]

    list_count = len(random_list)   # this function is used to get all the input elements and count it.
    random_item = random.randrange(list_count)  # here, the randrange helps to calculate and avoid response repititon

    return random_list[random_item]
print(random_responses())
