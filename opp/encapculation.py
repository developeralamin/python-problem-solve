class Dog:
    def __init__(self,name,breed,age):
        self.name = name ## public attributes
        self._breed = breed ## protected attributes
        self.__age = age ##private attributes 

    def geInfo(self):
        return f"{self.__age}"
    
object = Dog('Lele',"Ruti",23)
# print(type(object))
print(object.name)
print(object.geInfo())
print(object._breed)
        