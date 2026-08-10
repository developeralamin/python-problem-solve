import json 
import re
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

txt = "this is alamon"
searc = re.findall("alamon", txt)
print(searc)


