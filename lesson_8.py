#1
# n=int(input('n:'))
# m=int(input('m:'))
# while n<m:
#   if n%3==0:
#     print(n, end="")
#   n=n+1

# #2
# # n=int(input('Sonni kiriting:'))
# i=1
# k=0
# while i<=n:
#   if n%i==0: k=k+1
#   i=i+1
#   if k>2: break
# if k==2: print(f"{n} tub son")
# else: print(f"{n} tub son emas")



#3
a=int(input('a='))
b=int(input('b='))
while a!=0 and b!=0:
  if a>b:
    a%=b
  else:
    b%=a
c=a+b
print(c)