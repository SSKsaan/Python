# Dictionary is similar to sets but with key,value pairs
dic = {'name':'Sadik', 'age':20, 'gender':'male'}
print(dic) # shows all pairs in dictionary format
print(dic.keys()) # shows all keys only
print(dic.values()) # shows all value only

print(dic['name']) # keys are like index in dictionary
dic['name'] = 'San' # mutable, so can update value
dic['income'] = 0 # can add new key value pair like this
print(dic)

dic = {
    'name': 'samin',
    'age': 20,
    'age': 21, # won't keep duplicate keys, last value prevails
    'income': '0 tk'
}
print(dic)
print("Size of this", type(dic), ":", len(dic)) # type & len works

# Using dict() constructor [it won't even take duplicate key]
dic = dict(name = 'Sadik', gender = 'male', income = 0)

print('Befor Deleting Income:',dic)
del dic['income'] # deletes the key & its value
print('After Deleting Income:',dic)

print("\nNormal Loop Only Iterates for Key:", end=" ")
for key in dic: print(key, end=' ')

print("\nSpecial looping for Dictionary:")
for (key, val) in dic.items(): print(key,'=',val)

print("\nFinding a specific 'key' in Dictionary:")
if 'name' in dic: print(f"'name' = {dic['name']}") # throws KeyError if not found
print(dic.get('key', 'Key Not Found')) # safer way to search in dictionary
# get returns the key's value if found, else returns 2nd parameter
# 2nd parameter is optional, by default returns 'None'

if 'Sadik' in dic.values(): # searching for a specific value (case sensitive)
    print("'Sadik' found in values") 

# Sorting: (outputs as list)
print("Sorted Dictionary Keys:", sorted(dic)) # returns new list, in ascending order
print("Reversed Sorted Dictionary:", sorted(dic.items(), reverse=True))
print("Sorted Dictionary Values:", sorted(dic.values()))
# getting full dict sorted by values, using optional key parameter:
print("Custom Sorted Dictionary:", sorted(dic.items(), key=lambda x: x[1]))

# Dictionary Comprehension:
print("Dictionary Comprehension:", {x: x**2 for x in range(1,11)})

# Counter (returns a dictionary of characters & their occurances)
from collections import Counter
print("Frequency Counter of a List:", Counter([2,1,2,1,3,1]))
print("Frequency Counter of a String:", dict(Counter('212131')))
