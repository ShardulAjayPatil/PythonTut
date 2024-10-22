dict1={"Maharashtra":["pune","Mumbai"],
       "MadhyaPradesh":["bhopal","indore"],
       "Karnataka":["Maysore","Banglore"]
       }
# print(type(dict1))
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1["Maharashtra"])
# print(len(dict1))
# print(dict1.get("MadhyaPradesh"))
# dict1.update({"India":["delhi","mumbai","kolkata","Chennai"]})
# # print(dict1)
# dict1.pop("India")
# print(dict1)
# dict1.popitem()
# print(dict1)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
# print(mydict)

Family={
    "Child":{
        'email':"xyx@gmail.com",
        "Age":12
    },
    "mother":{
        "email":"abc@gmail.com",
        "Age":35
    },
    "father":{
        "email":"pqr@gmail.com",
        "Age":45
    }
}
print(Family)
print(Family["mother"]["email"])
Family.clear()
print(Family)





