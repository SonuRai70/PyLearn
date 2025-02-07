with open("monu.txt","r") as f:
    data=f.read()
    print(data)
    count=0
    num = data.split(",")
    print(num)
    for val in num:
        if(int(val)%2 == 0):
            count+=1
print(count)   
