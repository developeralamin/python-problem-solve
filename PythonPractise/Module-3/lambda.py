#lambda is function can take number of arguments,can multiple arguments
#lambda arguments : expression

a = lambda x,y:x+y+4
print(a(3,4))

def my_fun(n):
  return  lambda data : data * n 

mytripler  = my_fun(4)

print(mytripler(2))
