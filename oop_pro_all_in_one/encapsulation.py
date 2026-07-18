class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number  # Private attribute
        self.__account_holder = account_holder    # Private attribute
        self._balance = 0.0                      # protected attribute

#get private property value
    def get_account_holder(self):
        return self.__account_holder

object = BankAccount("123456789", "John Doe")
print(object.account_number) #public attribute
print(object.get_account_holder()) #private attribute
print(object._balance) #protected attribute