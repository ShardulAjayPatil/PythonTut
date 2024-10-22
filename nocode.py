fruits = ["apple", "banana", "cherry", "kiwi", "mango","aaa","hddhh","gavua","orange","Pineapple"]

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

newlist=[x for x in fruits if "a" in x]
print(newlist)

oddev=[x for x in range(1,10) if x%2 == 0]
print(oddev)
