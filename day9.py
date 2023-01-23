programming_dictionary = {
    "bug": "A programming error that prevents the program from running as expected",
    "function": "A piece of code that you want to reuse after call"
}

print(programming_dictionary["function"])


# add a new item to the dictionary
programming_dictionary["loop"] = "the act of doing something over and over again"
print(programming_dictionary)


for thing in programming_dictionary:
    print(programming_dictionary[thing])