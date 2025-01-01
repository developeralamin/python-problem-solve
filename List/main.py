# thelist = ['apple',12,'banana','juice']
# thelist.append('alamin')
# thelist.insert(1,'hanif')
# print(thelist[0:])

# thelist2 =['apple',12,'banana','juice']
# # thelist2.pop()
# (thelist2.clear())
# print(thelist2)


# tropical = ("mango", "pineapple", "papaya")
# thelist2.extend(tropical)
# print(thelist2)


tropical = ("mango", "pineapple", "papaya")
# print(len(tropical))
for i in range(len(tropical)):
    print(tropical[i])
x= 0
while x < len(tropical):
    print(tropical[x])
    x=x+1

#if p not in the list
newlist = []
for data in tropical:
    if "p" not in data:
        newlist.append(data)
print(newlist)

#one line code for iteration
#syntax : expression for item in iterable if conditon ==True

newlist = [x for x in tropical if 'p' in x ]
print(newlist)

#replace with word
replaceList = ['hello' for x in tropical]
print(replaceList)

#sort
print("Sorting the list")
sortingList = ["orange", "mango", "kiwi", "pineapple", "banana"]
sortingList.sort(reverse=True)
sortingList.reverse()
print(sortingList)