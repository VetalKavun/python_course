temps = [221, 223, 225, 220, -9999, 234]

new_temp = [temp / 10 for temp in temps if temp != -9999]

print(new_temp)