from collections import defaultdict

nums = [1,2,3,4,5,6,7,8,9,10]
dic = defaultdict(list)

for num in nums:
    dic[num%2].append(num)
print(dic)
