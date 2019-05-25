print("*** Question ***"
      "\n"
      "Find a quote from a famous person you admire."
      "\n"
      "Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:"
      "\n"
      "Albert Einstein once said, “A person who never made a mistake never tried anything new.”\n")

author = input("Please enter your author name: ")
quote = input("Please enter quote of your auther: ")

print("{0} once said, \"{1}\".".format(author,quote))