#dictory store multiple values in key:value pair 
# thedic = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964,
#    "year": 2020
# }
# thedic.pop("brand")
# print(thedic)

# dic = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(dic["colors"][0])

formatDic = dict(name="alamin",age=23)
for data in formatDic:
    print(formatDic[data])
# x = formatDic.items()
# x = formatDic.keys()
# x = formatDic.values()
formatDic['class'] = 10
print(formatDic)
formatDic["age"] = 60
print(formatDic)
if "names" not in  formatDic:
    print("No data")