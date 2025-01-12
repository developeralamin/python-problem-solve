from abc import  ABC,abstractmethod

class ATM(ABC):

    @abstractmethod
    def card(self):
        pass # This is an abstract method, no implementation here.

class Branch(ATM):

    def card(self):
        return "Mirpur-12"  # Providing the implementation of the abstract method


atm = Branch()
print(atm.card())

#direct create instance for abstract method
atm2 = ATM()
print(atm2.card())
