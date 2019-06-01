print("\n"
      "*** Question ***"
      "Write an input line to ask a user whether they want to take the red pill or the blue pill."
      "\n"
      "If they write “red” then print “You stay in wonderland and see how far the rabbit hole goes”."
      "\n"
      "Elif they write “blue” then print “You wake up in your bed and believe what you want to believe.”."
      "\n"
      "Else print “That’s not an option Neo.”")

pill = input("Would you like to have the RED PILL or the BLUE PILL: ").lower()

if pill.__contains__("red"):
    print("You stay in wonderland and see how far the rabbit hole goes")
elif pill.__contains__("blue"):
    print("You wake up in your bed and believe what you want to believe.")
else:
    print("That’s not an option Neo.")
