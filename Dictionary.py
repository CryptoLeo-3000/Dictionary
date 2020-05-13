import json
import difflib

def dictionary():    
    data = open("data.json","r+")
    words = json.load(data)
    word = input("Enter word to be searched in Dictionary\n")
    if word.lower() in words:
        meaning = words[word]
        for mean in meaning:
            print(mean)
    elif word.upper() in words:
        meaning = words[word]
        for mean in meaning:
            print(mean)
    elif word.isdigit():
        print("You entered number(s)\nPlease enter a meaningful word")
        dictionary()
    elif len(difflib.get_close_matches(word, words.keys())) > 0:
        prob = difflib.get_close_matches(word, words.keys())[0]
        ch = input(f"Did you mean {prob} ?\n").lower()
        if ch == "y" or ch == "yes":
            print(words[prob])
        else:
            ch = input(f"Would you like to enter {word} in my database?\n").lower()
            if ch == "y" or ch == "yes":
                meaning = input("Enter meaning of the word\n")
                updates = {word:meaning}
                words.update(updates)
                data.seek(0)
                json.dump(words,data)
            else:
                print("Sharam karo Sharam machine tumse zyada smart hai 😁")
    else:
        print("Word does not exist")
        ch = input("Do you want to search again?\n").lower()
        if ch == "y" or ch == "yes":
            dictionary()