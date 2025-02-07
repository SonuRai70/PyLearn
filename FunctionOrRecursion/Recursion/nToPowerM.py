n = int(input("input the number for which you want its power : "))
m = int(input("input the number to which you want the power of that number : "))

# def power(n,m):
#     if m == 0:
#         return 1
#     elif m == 1:
#         return n
#     else:
#         if(m % 2 == 0):
#             y = power(n,m/2)
#             return y*y
#         else:
#             z = power(n,m/2)
#             return z*z*n
# result = (power(n,m))
# print(result)

power = n**m
print(power)