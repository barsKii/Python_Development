import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(get_close_matches(w, data.keys())[0]))
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return ["Sorry, your word didn't return a valid response. Please double check your entry"]
        else:
            return ["We didn't understand your entry"]
    else:
        return ["No word was found. Please double check your entry"]

def print_result(response):
    x = 1
    for i in response:
        print(str(x) + ") " + i)
        x += 1

user_input = input("Welcome to the Dictionary\nPlease enter a term you want the definition for: ")


print_result(translate(user_input))