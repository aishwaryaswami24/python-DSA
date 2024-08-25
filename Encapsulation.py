class Bankaccount:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return f"{self.__balance} is present in your account"

object=Bankaccount(1000)
print(object.get_balance()) #access using methods only
#print(object.__balance) #throw attributeerror

#here if you use single underscore it will still be accissble in python
#if you use double underscore then it will throw an error saying AttributeError: 'Bankaccount' object has no attribute '__balance'