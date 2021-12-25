num =[1,2,3,4,5,6,7,8,9,10]
# for n in num:
#     print(n)
#slicing
print(num[-3])
print(num[0:4])# 0 inclusive     4 exclusive 
print(num[:4])
print(num[4:])


#striving
print(num[0:10:2])
print(num[::3])
print(num[::-1])# first element : last element or index : gap between each

for i in range(len(num)):
    print(num[i])
