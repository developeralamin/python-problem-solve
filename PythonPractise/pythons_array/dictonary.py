thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["brand"])
print(thisdict["colors"][0])
print(len(thisdict))

thisdict.values()
print(thisdict.keys())

thisdict["year"] = 2020
print(thisdict)

#dictonary comprehension
dictionaryy = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dictionaryy.update({"year": 2020})
print(dictionaryy)