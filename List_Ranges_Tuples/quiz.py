alpha1 = ["A", "B", "C", "D"]

alpha2 = ["A"]
alpha2.append("B")
alpha2.append("C")
alpha2.append("D")

print(alpha1 == alpha2)


trees = ["Larch", "Larch"]
identified_trees = trees

trees.append("Horse Chestnut")
print(identified_trees)

flowers = [["rose", "red"],
           ["snapdragon", "white"],
           ["daisy", "white"],
           ["lily", "yellow"]
           ]

second_flowers = flowers

second_flowers[1] = ["lilac", 'purple']

second_flowers[1][1] = 'pink'
print(flowers)


numbers = range(13)

new_range = numbers[1::2]
for i in new_range:
    print(i, end=', ')

even = range(0, 20, 2)
for number in even[::-1]:
    print(number, end=', ')