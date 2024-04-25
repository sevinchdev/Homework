class User:
  def __init__(self,ism,foydalanuvchi_ismi,email):
    self.ism=ism
    self.username=foydalanuvchi_ismi
    self.email=email

  def get_info(self):
    print(f"Foydalanuvchi:{self.username}, ismi:{self.ism}, email:{self.email}")
  
user1=User('Sevinch','Sevinch0909',"sevinchurazmetova009@gmail.com")
user2=User('Xurshida','Xurshida07','xurshidakarimboyeva@gmail.com')

user1.get_info()
user2.get_info()
