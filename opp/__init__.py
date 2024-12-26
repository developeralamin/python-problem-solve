#automatically called when a new object is created. It initializes the attributes of the class.
class Register:
    def __init__(initData,name):
        initData.name = name

data = Register("Panbazar")
object = Register("Dhaka")
print(data.name)
print(object.name)

data.name = "Mirpur-12"
print(data.name)
print(object.name)