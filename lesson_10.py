# Program that calculates dimeter, perimeter,area of a circle
# def circle(radius):
#   pi=3.14

#   diameter=2*radius
#   perimeter=2*pi*radius
#   area=pi*(radius**2)

#   results={
#     'radius':radius,
#     'diamater':diameter,
#     'perimeter':perimeter,
#     'area':area
#   }

#   return results
# radius=int(input("Enter the radius of a circle: "))
# result=circle(radius)
# print(result)


# function that returns a list of prime numbers in a given range
# def oraliq (m,n):
#   prime_numbers=[]

#   while n<=m:
#     i=n
#     j=1
#     divisor=0

#     while j<=i:
#       if i%j==0:
#         divisor+=1
#       j+=1

#     if divisor==2:
#       prime_numbers.append(i)
#     n+=1
#   return prime_numbers

# n=int(input("n= "))
# m=int(input("m= "))
# print(oraliq(m,n))


def fibonachi(n):
  numbers=[]
  
  for i in range(n):
    if i==0 or i==1:
      numbers.append(1)
    else:
      numbers.append(numbers[i-1]+numbers[i-2])
  return numbers

print(fibonachi(5))
