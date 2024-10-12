# def power(set):
#     elements = list(set)
#     n = len(elements)
    
#     size = 2 ** n
#     power_set = []

#     for i in range(size):
#      subset=[]
    
#      for j in range(n):
#         if i & (1 << j):
#             subset.append(elements[j])
#      power_set.append(subset)
#     return power_set
# set = {5,6,7,2,9,10,98,97,96,95,94,93,92,92,91,80,89,88,87}
# result = power(set)

# for subset in result


# def fac(n):
#     if (n==0 or n==1):
#      return 1
#     return n*fac(n-1)

# n = int(input("Write you number over here _"))
# print(fac(n))




# def dio(n):
#     if n > 1000:
#         return
#     print(n)
#     dio(n+1)
# dio(2)


 # Head : Head recursion starts with the operator and then proceeds to print n. This means that if I enter
# 10 I will get every number from 1-10.


# def head_recursion(n):
#     if n == 0:
#      return
#     head_recursion(n - 1)
#     print(n)
    
# n = int(input("Enter Your Range: "))
# print(head_recursion(n))



# Tail: Tail recursion is where the print statement n comes first and then the code follows. THis means if I entered 10 I would
# get all the numbers for 10-1.

# def tail_recursion(n):
#     if n == 0:
#      return
#     print(n)
#     tail_recursion(n - 1)
  
# n = int(input("Enter Your Range: "))
# print(tail_recursion(n))









def incdec(n,num):
    if(n<1 or n>num):
        return
    print(n)
    incdec(n-1,num)
    print(n)
    

num = int(input("Enter your range n :"))
incdec(num,num)
    
    

