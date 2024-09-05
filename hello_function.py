def main():
    name=input("enter your name: ")
    print(f"Your name is ,{name}")
    hello(name)
    hello()

def hello(self='World'):
    print(f"Hello {self}")

main()