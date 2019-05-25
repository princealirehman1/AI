print("Question: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.\n")

name = input("Please enter your name: ")

print("Uppercase: {0}\n"
      "Lowercase: {1}\n"
      "Titlecase: {2}".format(name.upper(),name.lower(),name.title()))