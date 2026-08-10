try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("The 'try except' is finished")

x = 58
if x > 4:
    raise Exception("Sorry number smaller")

b=58
if not type (x) is str:
    raise TypeError("Sorry number smaller")