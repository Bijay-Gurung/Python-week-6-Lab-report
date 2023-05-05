dict1 = {"a":[4,5,6],"b":[8,4,1]}
dict2 = {}
for key, value in dict1.items():
    dict2[key] = sum(dict1[key])
print(dict2)
