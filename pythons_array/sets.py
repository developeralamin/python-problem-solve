mysets = {"apple","kola"}
print(mysets)
# print(mysets[0]) # sets are unordered and unindexed, so we cannot access items by index
# for x in mysets:
#     print(x)
# mysets.add("banana")
# print(mysets)

thissets = {"bs","asdb","asdasdb"}
thissets.update(mysets)
print(thissets)

thissets.remove("bs")
print(thissets)
# join sets 
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1-set2
print(set3)


# join sets

set11 = {"apple", "banana", "cherry"}
set12 = {"google", "microsoft", "apple"}

set3 = set11 ^ set12
print(set3)