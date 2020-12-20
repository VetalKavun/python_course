import mysql.connector
from difflib import get_close_matches

data_set = {}


def create_connection_to_db():
    connection = mysql.connector.connect(
        user='vitalii',
        password='Silefu_57',
        host='localhost',
        database='thesarus'
    )
    print("Connection to the database established")
    return connection


def get_dict_of_words(word):
    word.replace("'", "\\'")
    query = """select word, description from thesarus where word regexp '^{}|{}|{}' limit 5""" \
        .format(word, word.capitalize(), word.upper())
    connection = create_connection_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.commit()

    data = dict((word, description) for word, description in results)
    word_list = get_close_matches(word, data.keys(), n=3)
    return word_list


def find_word_description():
    word = input("Enter the word to find: ")
    word_list = get_dict_of_words(word)
    if len(word_list) > 0:
        for item in word_list:
            while True:
                user_confirmation = input(
                    "Did you mean {}?. Enter y - to confirm, n - to reject: ".format(item)).lower()
                if user_confirmation == "y":
                    return data_set[item]
                elif user_confirmation != "n":
                    return "Did not understand input. Please try again."
                else:
                    break
        return "Word doesn't exist. Please check your input"
    else:
        return "Word doesn't exist. Please check your input"


print(find_word_description())
