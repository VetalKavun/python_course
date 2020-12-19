import time

pause = int(input("Enter the value of delay: "))
print("execution will be paused on %d second(s)" % pause)
time.sleep(pause)
print("program execution finished")
