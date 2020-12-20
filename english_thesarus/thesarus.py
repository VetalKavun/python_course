import os
import json
import difflib
from difflib import get_close_matches

data_set = {}


def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path) as file:
            global data_set
            data_set = json.load(file)
            print("Data set is loaded")
    else:
        print("Can't load data set")


def get_word_description(word):
    if word.upper() in data_set.keys():
        return data_set[word.upper()]
    if word.capitalize() in data_set.keys():
        return data_set[word.capitalize()]
    if word in data_set.keys():
        return data_set[word]
    else:
        best_matches_word = get_close_matches(word, data_set.keys(), n=5)
        if len(best_matches_word) > 1:
            for item in best_matches_word:
                while True:
                    user_confirmation = input("Did you mean: %s? Enter y - to confirm, "
                                              "n - to cancellation: " % item).lower()
                    if user_confirmation == 'y':
                        return item
                    elif user_confirmation != 'n':
                        print("Did not understand your request")
                    else:
                        break
        return "Word is not exists! Please double check this one"


def get_word_from_user():
    word = input("Enter the word to search for: ").lower()
    return word


# loading the dataset
load_data("data.json")

print(get_word_description(get_word_from_user()))
