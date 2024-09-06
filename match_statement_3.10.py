name = input("What's your name? ")

  match name:
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
#getting error bez it availble in 3.10 python version
#  match name:
#           ^
# SyntaxError: invalid syntax