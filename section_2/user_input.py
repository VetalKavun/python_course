def temp_react(temperature):
    if temperature > 25:
        return 'hot'
    elif temperature < 15:
        return 'cold'
    else:
        return 'warm'

temperature = float(input("Enter the tamperature: "))
print(temp_react(temperature))