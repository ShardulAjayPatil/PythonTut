tup=("Apple",23,"bus",2+3j)
# print(type(tup))
# print(tup[0])
# tup[1]=67 # TypeError: 'tuple' object does not support item assignment

s={"apple","banana","apple","Kiwi"}
# print(s)

# print(len(tup))

s="t"
# print(type(s))
l=["tuple"]
# print(type(l))
d=(45,)
# print(type(d))

q=(12,23,65)
w=("Sun","moon","mars")
e=(True,False,True,False)


# Declaration by constructer
thisTuple=tuple((12,45,"basket","45"))
# print(type(thisTuple))



# print(thistuple1[1])

# print(thistuple1)

# for x in thistuple1:
#     print(x)

# print(thistuple1[-1])
# print(thistuple1[2:100])
# print(thistuple1[::-1])
# print(thistuple1[-4:-2])


thistuple1 = ("apple", "banana", "cherry","mango","kiwi","Cat","Lion")
newtup=("hello","hi")
thistuple1=thistuple1+newtup
# print(thistuple1)

# print(thistuple1)
thistuple1=list(thistuple1)
thistuple1.append("Goat")
thistuple1=tuple(thistuple1)
# print(thistuple1,type(thistuple1),sep="\n")

#unpacking of Tuples
tup=("cat","tiger","goat","Whale","goldfish")
# a,b,*c=tup
# print(a,b,c)

print(tup[2]*2)
# del tup
# print(tup)






