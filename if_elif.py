#1st way
# name=input("what is your name: ")
# if name=="Aishwarya":
#     print("TCS")
# elif name=="Shubham":
#     print("UST")
# else:
#     print("DB empty")

#2nd way

# name=input('what is your name: ')
# if name=="Aishwarya":
#     print("TCS")
# elif name=="Shubham":
#     print("UST")
# elif name=="Ratndeep":
#     print("UST")
# else:
#     print("unknown")

#3rd way
# name=input('what is your name: ')
# if name=="Shubham" or  "Ratndeep":
#     print("UST")
# elif name=="Aishwarya":
#     print("TCS")
# else:
#     print("unknown")

#4th way
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
