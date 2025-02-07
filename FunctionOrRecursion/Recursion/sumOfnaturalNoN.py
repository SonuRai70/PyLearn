n = int(input("Enter no to calculate sum of 1st n No "))

def show(num):
    if(num==0):
        return 0
    return show(num-1)+num  

sum=show(n)
print(sum)