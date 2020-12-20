import mysql.connector
import json
import os


def get_dictionary_from_file(file_name):
    if os.path.exists(file_name):
        with open(file_name) as data_file:
            data_set = json.load(data_file)
            print(">>>>>>>>Data set is loaded")
            return data_set


def create_db_connection():
    connection = mysql.connector.connect(
        user='vitalii',
        password='Silefu_57',
        host='localhost',
        database='thesarus'
    )
    print(">>>>>>>>Database connection is established")
    return connection


def seed_data_from_file(file_name):
    connection = create_db_connection()
    cursor = connection.cursor()
    data_set = get_dictionary_from_file(file_name)
    for item in data_set.items():
        word = item[0].replace('"', '\\"')
        description = ''.join(item[1]).replace('"', '\\"')
        query = """insert into thesarus(word, description) values ("%s", "%s")""" % (word, description)
        print(query)
        cursor.execute(query)
    connection.commit()
    print("Data is loaded to the database")


seed_data_from_file("data.json")
