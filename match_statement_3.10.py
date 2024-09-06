# name = input("What's your name? ")
#
#   match name:
#       case "Harry" | "Hermione" | "Ron":
#           print("Gryffindor")
#       case "Draco":
#           print("Slytherin")
#       case _:
#           print("Who?")

#getting error bez it availble in 3.10 python version
#  match name:
#           ^
# SyntaxError: invalid syntax

#match is availble in python 3.10 version
# Input from the user
name = input("What's your name? ")

# Match case structure
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
