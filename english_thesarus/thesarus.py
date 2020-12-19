import os
import json

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
    if word in data_set:
        return data_set[word]
    else:
        return "Word is not exists! Please double check this one"


def get_word_from_user():
    word = input("Enter the word to search for: ").lower()
    return word


# loading the dataset
load_data("data.json")

print(get_word_description(get_word_from_user()))
