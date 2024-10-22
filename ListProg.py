# basket=["apple","mago","orange"]
# print(len(basket))
# print(basket[0])
# basket[0]="pen"
# print(basket)

# x=[]
# x.append("table")
# x.append("cup")
# print(x)
# x.insert(0,"Shardul")
# print(x)
# x.pop(0)
# print(x)
# x.append("helllo")
# x.append("lock")
# x.append("key")
# # print(x)
# x.remove("cup")
# print(x)
# del x[0]
# print(x)
# del x
# print(x)

# a=45,"golf","tree",43.89
# b=list(a)
# print(type(a))
# print(type(b))
# print(b)
# print(a)

# l=[["candy","Ptraick","babu"],(34,78),"Shardul",45.7]# multidimnsional
# print(l)
# print(l[0])

list1=[1,2,34,1,2]
# print(list1)
# print(list1[0])
# print(list1[4])

# print(list1[6])#IndexError: list index out of range

bucket=["water","mud","mug","Juice","fish"]
# print(bucket)
bucket[1]="Clay"
# print(bucket)
#Accessing of List
# print(bucket[0])
# print(bucket[-1])
# print(bucket[3])
# Slicling of list
# list [start:end-1:step]
# print(bucket[2:4])
# print(bucket[::-1])
# print(bucket[::2])
# print(bucket[-2])
# print(len(bucket))
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[4:])
# print(thislist[:6])

# print("kiwi" in thislist)

# print(thislist)

# for x in thislist:
#     print(x)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# new=["Grapes","Avacado"]
# thislist[1:3]=new
# print(thislist)
thislist.insert(1,"potato")
# print(thislist)
new1=[]
new1.append("cup")
new1.append('car')
new1.append("cat")
new1.append('dog')
# print(new1)

# thislist.extend(new1)
# print(thislist)
# print(new1)

#Remove elements
# print(thislist)
# thislist.remove("Cherry")#ValueError: list.remove(x): x not in list
# print(thislist)

thislist1 = ["apple", "banana", "cherry"]
# thislist1.pop()#removes last item when not given index
# thislist1.pop(1)# removes specified item
# print(thislist1)

# del thislist1[2]
# print(thislist1)


# test=[12,23,45,67,89]
# test.clear()
# print(test)

# x=[2,4,6,8,10,12]
# print(x)
# for i in x:
#     print(i)



# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)


# newlist=[x for x in fruits if "a" in x]
# print(newlist)

# oddev=[x for x in range(1,10) if x%2 == 0]
# print(oddev)

# thislist = ["orange", "mango", "kiwi", "pineapple","Mango", "banana","apple","Zebra"]
# thislist.sort(key=str.lower)
# print(thislist)

# numbers=[45,89,23,90,12,67,34,39,46]
# numbers.sort(reverse=True)
# print(numbers)


orgnal=[45,89,12,67,34,39,46]
cpy=orgnal.copy()
print(orgnal)
print(cpy)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3=list1+list2
print(list3)