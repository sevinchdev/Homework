# Arifmetik amalni bajaruvchi funksiya

# def arifmetik_amal(*sonlar):
#   amal1='+'
#   amal2='-'
#   amal3='/'
#   amal4='*'
#   amal=input("Amalni kiriting: ")
#   if amal==amal1:
#     return sum(sonlar)
  
#   elif amal==amal2:
#       return sonlar[0]-(sum(sonlar)-sonlar[0])
  
#   elif amal==amal3:
#       natija=sonlar[0]
#       for i in sonlar:
#         natija=natija/i
#       return natija

      
#   elif amal==amal4:
      
#       natija=1
#       for i in sonlar:
#         natija=natija*i
#       return natija
  
# result=arifmetik_amal(9,8,7,6,5)
# print(result)


def royxat_qoshish(*lists):
    royxat = []
    
    for list in lists:
        royxat.extend(list)
    
    return royxat

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

qoshma_royxat = royxat_qoshish(list1, list2, list3)
print("Birlashgan ro'yxat:", qoshma_royxat)
