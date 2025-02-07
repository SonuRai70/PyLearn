tup=(1,4,9,16,25,36,49,81,100)
x=25
i=0
while i < len(tup):
    if(tup[i]==x):
         print("Number is found at index : ",i)
         break
    else:
        print("finding....")
        i+=1

print("end of loop")
    