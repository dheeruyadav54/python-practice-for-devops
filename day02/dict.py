details = {
"name" : "Dheeraj Yadav",
"age" : 33,
"city" : "Amsterdam",
"country" : "Netherlands",
"Married" : True,
"certified" : ["AWS", 2.5]
}
print (type (details))
details.update ({"Children" : 1})
# print (details)


for key,value in details.items():
    print (key,value)