thelists = list(("bangladesh",'india','pakistan','srilanka'))
print(thelists)

print(type(thelists))
thelists.append('nepal')
print(thelists)


# //accessing the list items
list1 = ["abc", 34, True, 40, "male"]
for x in list1:
    print(x)
print(f"the length of the list is {len(list1)}")
print(list1[-1])

# //change the value of the list
list1[1] = 45
print(list1)

# //insert a value in the list
list1.insert(1,"alamin")
print(list1)

# // add a list to a list
list2 = ["bangladesh", "india", "pakistan", "srilanka"]
list1.extend(list2)
print(list1)

# //specific items in the list
list1.remove("abc")
print(list1)
# //pop the last item in the list
list1.pop(1)
print(list1)

# //clear the list 
list1.clear()
print(list1)

# //copy the list
list3 = list2.copy()
print(list3)

# // //loop through the list
for x in list2:
    if x =="indias":
        print(x)
    elif x =="pakistans":
        print(x)
    print("not found")


# join list 
list4 = ["hello", "world", "python"]
list5 = ["is", "awesome"]
list6 = list4 + list5
print(list6)

# sort list  asending default
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse=True)
# print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) #descending order
# thislist.sort()
print(thislist)