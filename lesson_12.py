# 1 Function that returns positive integers in a list

# def numbers(*sonlar):
#   list1=list(filter(lambda x: x>0, sonlar))
#   return list1
# result=numbers(-1,3,4,7,-9,-90,60)
# print(result)

# 2 Function that returns the list in a reversed version

# def numbers(*sonlar):
  
#   list1=list(sonlar)
#   list1.sort(key=lambda x:-x)
#   return list1

# result=numbers(4,6,8,0,1,4,7,9,12,14,1,6)
# print(result)

# 3 Function that returns square of even integers in a list
# def numbers(*sonlar):
#   list1=[]
#   list1.append(filter(lambda i: pow(i,2),sonlar))
#   # for i in sonlar:
#   #   if i%2==0:
#   #     list1.append(pow(i,2))
#   #   else:
#   #     list1.append(i)
#   return list1
# result=numbers(2,3,4,5,6,7,8,9)
# print(result)    

# def numbers(*sonlar):
#   return [(lambda x:x**2 if x%2==0 else x)(i) for i in sonlar]
# result=numbers(2,3,4,5,6,7,8,9)
# print(result)    
