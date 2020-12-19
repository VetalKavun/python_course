import time
import os
import pandas

while True:
    if os.path.exists("temperature_data.csv"):
        with open("temperature_data.csv") as file:
            data = pandas.read_csv("temperature_data.csv")
            print(data.mean()["st1"])
    else:
        print("File doesn't exist")
    time.sleep(10)