
fruits = [
    "Apples.",
    "Bananas.",
    "Grape.",
    "Mangos.",
    "Nectarines.",
    "Pears. "
    ]
print(" My favorite fruit: ")
for fruit in fruits:
    print (fruit)
print ("************")

counter = 0
exclude_fruit = "Nectarines."

while counter < len(fruits):
    current_fruit = fruits[counter]
    if current_fruit != exclude_fruit:
        print(current_fruit)
    counter += 1
