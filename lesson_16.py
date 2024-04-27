class shaxs:
  """Shaxslar haqida ma'lumot"""

  def __init__(self,ism,familiya,passport,tyil):
    self.ism=ism
    self.familiya=familiya
    self.passport=passport
    self.tyil=tyil

  def __repr__(self):
    """shaxs haqida ma'lumot"""
    return f"{self.ism} {self.familiya}. Passport:{self.passport}, {self.tyil}-yilda tug'ilgan."
  
  
  def get_age(self,yil):
    """Shaxsning yoshini qaytaruvchi funksiya"""
    return yil-self.tyil
  


class Talaba(shaxs):
  """Talaba klassi"""

  def __init__(self,ism,familiya,passport,tyil,idraqam):
    """Talabaning xususiyatlari"""
    super().__init__(ism,familiya,passport,tyil)
    self.idraqam=idraqam
    
    
  def __eq__(self,boshqa_tyil):
    return self.tyil==boshqa_tyil.tyil
  
    
  def __lt__(self,boshqa_tyil):
    return self.tyil<boshqa_tyil.tyil
  
    
  def __le__(self,boshqa_tyil):
    return self.tyil<=boshqa_tyil.tyil
    
talaba1=Talaba("Sevinchoy","Urazmatova","12345",2006,"123456")
talaba2=Talaba("Adham","Shernafasov","12345",2006,"123456")
  
if talaba1==talaba2:
  print(f"{talaba1.ism} va {talaba2.ism}ning yoshlari teng")
else:
  print("Ular teng emas.")


