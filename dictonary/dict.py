dict = {
    'Name' : 'Sonu Rai',
    'Branch' : 'E.C.E',
    'Roll' : '230425',
    'Language' : ('C', 'Python'),
    'Education' : ['10th', '12th', 'B.tech'],
     12.0 : 12.0, #key will not visible but their value will visible
     12 : 12 #key will not visible but their value will visible
}

null_dict={
    
}           #we can add null dictonary.
null_dict['name']= 'Sonu'


print(dict)
print(dict['Roll'])
print(dict['Education'])
print(dict[12])
dict[12] = 24
print(dict)
print(null_dict)
#Dictonary are unordered, mutable(like list) and we cannot make their duplicate.