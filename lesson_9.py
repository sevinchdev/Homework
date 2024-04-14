# Program for checking whether number is prime or not.

# Solution 1
# def check_number():
#   n=int(input("Enter the number: "))
#   k=0
#   for i in range(1,n+1):
#     if n%i==0:
#       k+=1
#     if k>2:
#       break
#   if k==2:
#     return f"{n} is a prime number."
#   else:
#     return f"{n} is not a prime number."
      
# result=check_number()
# print(result)


# Solution 2
# def check_number():
#   n=int(input("Enter the number: "))
  
#   divisors=[i for i in range(1,n+1) if n%i==0]

#   if len(divisors)==2:
#     return f"{n} is a prime number."
#   else:
#     return f"{n} is not a prime number."
   
# result=check_number()
# print(result)



# Program that determines the greatest common divisor (GCD) (EKUB in uzbek)
# of two given positive integers "a" and "b"

def find_gcd(a,b):
  if a<b:
    a,b=b,a
  
  while b != 0:
    a,b=b, a%b
  
  return a

a=int(input("Enter the first positive integer: "))
b=int(input("Enter the second positive integer: "))

gcd_result=find_gcd(a,b)
print(f"The greatest common divisor (EKUB in uzbek) of {a} and {b} is {gcd_result}")
  