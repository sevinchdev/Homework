class avto:
  def __init__(self,model,rang,korobka,narx):
    self.model=model
    self.rang=rang
    self.korobka=korobka
    self.narx=narx
    self.kilometer=0

  def get_info(self):
    return f" modeli: {self.model}\
    rangi:{self.rang}\
    korobka:{self.korobka}\
    narxi:{self.narx}. {self.kilometer} km yurgan."
  
  def update_km(self,kilometer1):
    self.kilometer+=kilometer1


class avtosalon:
  def __init__(self,salon_nomi):
    self.salon_nomi=salon_nomi
    
    self.mashinalar_soni=0
    self.mashinalar=[]

  def add_cars(self,mashina):
    self.mashinalar.append(mashina)
    self.mashinalar_soni+=1

  def get_cars(self):
    return [car.get_info() for car in self.mashinalar]


salon=avtosalon('salon')
mashina1=avto("gentra","oq","avtomat",150_000_000)
mashina2=avto("matiz","qora","korobka",50_000_000)
mashina3=avto("spark","qora","korobka",100_000_000)
salon.add_cars(mashina1)
salon.add_cars(mashina2)
salon.add_cars(mashina3)

cars=salon.get_cars()
print(cars)

# print(mashina1.get_info())


# def see_methods(klass):
#   return [method for method in dir(klass) if method.startswith('__')]


