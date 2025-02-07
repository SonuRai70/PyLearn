dict = {
    'Name' : 'Sonu Rai',
    'Branch' : 'E.C.E',
    'Roll' : '230425',
    'Language' : ('C', 'Python'),
    'Education' : ['10th', '12th', 'B.tech'],
     '12.0' : '12.0', #key will not visible but their value will visible
     '12' : '12' #key will not visible but their value will visible
}
print(tuple(dict.keys()))
print(list(dict.keys()))
print("length of dictonary is : " , len(dict))