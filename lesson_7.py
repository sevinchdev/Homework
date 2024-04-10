# 1
# Dost = {
#     'xushida':['lol', 'sir', 'men','aso'],
#     'hayriniso':['men', 'andalus fotihlari'],
#     'og\'abek':['atom odatlari', 'dor ostidagi odam'],
#     'sanjar':['tungi suhbatlar', 'tongi suhbatlar']
# }
# ism=''
# name=input('Ismni kiriting:').lower()
# for key,value in Dost.items():
#   if key.lower()==name:
#     key=ism
#     break
# if ism:
#   print(f"{name}ning sevimli kitoblari quyidagilar:", end="")
#   for book in Dost[ism]:
#     print(f"{book}", end="")

# 2
davlatlar = {
    'uzbekistan':{
        'poytaxt':'Toshkent',
        'dTil':'uzbek tili',
        'joylashuv':'o\'rta osiyo',
        'aholi':'37 mln'
    },
    'rossiya':{
        'poytaxt':'Moskva',
        'dTil':'rus tili',
        'joylashuv':'yevropa',
        'aholi':'350 mln'
    },
    'Xitoy':{
        'poytaxt':'Pekin',
        'dTil':'xitoy tili',
        'joylashuv':'osiyo',
        'aholi':'1 mlrd 450 mln'
    },
    'Germaniya':{
        'poytaxt':'Berlin',
        'dTil':'nemis tili',
        'joylashuv':'yevropa',
        'aholi':'84 mln'
    }
}
# for key, value in davlatlar.items():
#   print(f"{key.title()}: " ,end=""
#         f"Poytaxti {value['poytaxt']} shaxri, ", end=""
#         f"Davlat tili {'value(dTil)'}, ", end=""
#         f"{'value[joylashuv]'} qit\'asida joylashgan, ", end=""
#         f" Aholi soni {'value[aholi]'}.", end="")


# 3
davlat=""
country=input("Davlatni kiriting:").lower()
for key,value in davlatlar.items():
  if key.lower()==country:
    key=davlat
    break

dict={}

if davlat:
  print(davlatlar[davlat])
  dict=davlatlar[davlat]
  print(f"{davlat.title()}:")
  print(f"Poytaxti {davlatlar[davlat]['poytaxt']} shaxri."
        f"Davlat tili {davlatlar[davlat]['dTil']}."
        f"{davlatlar[davlat]['joylashuv']} qit\'asida joylashgan."
        f"Aholi soni {davlatlar[davlat]['aholi']}")
else: print('Bizda bunday ma\'lumot yo\'q.')