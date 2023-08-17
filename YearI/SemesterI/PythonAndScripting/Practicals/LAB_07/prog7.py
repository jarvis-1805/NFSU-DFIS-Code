dict={"Patel":"Veg","iver":"non-veg ","jin ":"eggtarian","ima":{"B":"maggie","L":"veg "}}
print(dict)
print(dict['Patel'])
print(dict['ima']['B'])
dict['Ana']='imi'
print(dict)
del dict['Ana']
print(dict)
dict['Patel']='vegi'
print(dict)
print(dict.keys())
print(dict.items())
dict1=dict.copy()
print(dict1)

