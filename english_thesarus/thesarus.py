import os
import json

data_set = {}


def load_data(file_path):
    data = {}
    if os.path.exists(file_path):
        with open(file_path) as file:
            global data_set
            data_set = json.load(file)
            print("Data set is loaded")
    else:
        print("Can't load data set")


def get_word_description(word):
    return data_set[word]


def get_word_from_user():
    word = input("Enter the word to search for: ")
    return word


# loading the dataset
load_data("data.json")

print(get_word_description(get_word_from_user()))
