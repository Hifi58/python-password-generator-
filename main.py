import random

# Variables
characteres = list("abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789" + "!&£$€?=+-%¥#§")

# Calculation
random.shuffle(characteres)

password = []
for i in range(16):
    password.append(random.choice(characteres))

random.shuffle(password)

# result
print("".join(password))