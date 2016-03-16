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

print("\n-- dictionaries ------------------------")
en_lt = { "red" : "raudona", "yellow" : "geltona", "black" : "juoda" }
print(en_lt)
print("en_lt[\"red\"] = " + en_lt["red"])
en_lt["blue"] = "mėlyna"
print(en_lt)
poppedWord = en_lt.pop("blue")
print("popped '" + poppedWord + "' from the list")
print(en_lt)
poppedNonExistingWord = en_lt.pop("doesntExist", "no capital")
print("tried to pop non-existing '" + poppedNonExistingWord + "' from the list")
print(en_lt)
(english, lithuanian) = en_lt.popitem()
print("(english, lithuanian) = " + str((english, lithuanian)))
print(en_lt)
print("get() non existing item: " + str(en_lt.get("not existing")))
print("get() existing item: " + str(en_lt.get("black")))
shallow_dictionary_copy = en_lt.copy()
print("copied dictionary: " + str(shallow_dictionary_copy))
shallow_dictionary_copy["yellow"] = "geltona geltona"
print("updated dictionary copy: " + str(shallow_dictionary_copy))
print("original dictionary: " + str(en_lt))
merged_dictionary = {}
merged_dictionary.update(en_lt)
merged_dictionary.update(shallow_dictionary_copy)
print("merged dictionary: " + str(merged_dictionary))
