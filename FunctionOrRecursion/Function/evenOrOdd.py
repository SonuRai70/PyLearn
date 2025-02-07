num=int(input("Enter the number to check Even Or Odd "))
def check(n):
    if(n%2==0):
        print('Number is Even')
    elif(n%2!=0):
        print('Number is Odd')
    else:
        print('Number is not matching the condition')


check(num)