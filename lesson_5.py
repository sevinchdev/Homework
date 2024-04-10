# yosh=int(input('Yoshingiz nechada?'))
# if yosh<5 or yosh>60:
#     price=0
# elif yosh<18:
#     price=15000
# elif yosh>=18:
#     price=25000
# print(f"Sizga kirish {price} so'm")


# num1=int(input("1-sonni kiriting:"))
# num2=int(input("2-sonni kiriting:"))
# if num1>num2:
#     print(f"1-son {num1} 2-son {num2}dan katta.")
# elif num1==num2:
#     print("Sonlar teng")
# else:
#     print(f"2-son {num2} 1-son {num1} dan katta.")


# num=int(input("Butun son kiriitng:"))
# for i in range(3,16):
#     if num%i==0:
#         print(f"{num} soni {i} ga qoldiqsiz bo'linadi.")

users=['sevinchurazmatova', 'jasurovnasevinch', 'sevinch0909', 'urazmatova', 'jasurovna', 'sevinch']
login=str(input("Login tanlang:"))
for i in users:
    if i==login.lower():
        print("Login band, yangi login tanlang!")
    else:
        print("Xush kelibsiz, foydalanuvchi!")