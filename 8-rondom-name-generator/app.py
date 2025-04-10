import random

first_parts = ["sky", 'Star', 'Moon,' 'Sun']
last_parts = ['rider', 'Walker', 'hunter',]

print(" Fantasy name generator")

count = int(input("How many names do you want "))

for i in range(count):
    first_name = random.choice(first_parts)
    last_name = random.choice(last_parts)
    print(f"{first_name}{last_name}")