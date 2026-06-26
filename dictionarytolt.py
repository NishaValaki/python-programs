mydata={1: 10,20.5: 100,'key': "hello world"}
print(mydata)
print(type(mydata))
print()

new_list1=list(mydata.values())
print(new_list1)
print(type(new_list1))
print()

new_list2=tuple(mydata.values())
print(new_list2)
print(type(new_list2))
print()