import os
import time

while True:
    if os.path.exists("data.txt"):
        with open("data.txt") as file:
            print(file.read())
    else:
        print("File doesn't exist")
    time.sleep(10)
