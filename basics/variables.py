print("-- integer -----------------------------")
i = 5
print("i = " + str(i))

i = i + 5
print("i = i + 5");
print("i = " + str(i));

print("\n-- decimal -----------------------------")
print("the // division is more than two times as fast! it truncates numbers")
d = 10 / 3
print(d)

d = 10 // 3
print(d)

print("\n-- string ------------------------------")
text = "Lists can be accessed via indexes"
print("Text: " + text + ". Length: " + str(len(text)))
print("text[0] + text[1] + text[22] + text[11] = " + text[0] + text[1] + text[22] + text[11])

print("\n-- lists -------------------------------")
capitals = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Vilnius", "Hamburg"]
print(capitals)
print("capitals[5] = " + capitals[5])
print("capitals[-2] = " + capitals[-2])
print("Number of capitals: " + str(len(capitals)))

print("\n-- tuples ------------------------------")
t = ("tuples", "are", "immutable")
print(t)
print("t[0] = " + t[0])

print("\n-- slicing -----------------------------")
print("first three capitals: " + str(capitals[0:3]))
print("last three capitals: " + str(capitals[-3:]))
print("every second capital: " + str(capitals[::2]))


print("\n-- repetitions -------------------------")
hello = "Hello World!"
print(hello)
hello = 2 * hello
print(hello)
print(capitals * 2)
print(t * 3)
