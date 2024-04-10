# kompyuter={
#     'rangi':'qora',
#     'operativ xotira':'8GB',
#     'videoxotira hajmi':'4 GB',
#     'turi':'gaming notebook'
# }
# kompyuter['rangi']="ko'k"
# print(kompyuter)

# komp=kompyuter.get('operativ xotira', "Bunday kalit yo'q")
# print(komp)

# komp_qurilmalar={
#     'sichqoncha':'Lenovo Y',
#     'klaviatura':'Asus',
#     'monitor':'Asus',
#     'kolonka':'LG XBOOM'
# }
# keys_list=list(komp_qurilmalar.keys())
# print(keys_list)

countries={
    'USA':'Washington',
    'Canada':'Ottawa',
    "Germany":'Berlin',
    "Uzbekistan":'Tashkent',
    "South Korea":'Seoul'
}
# print(sorted(countries.keys()))
# print(sorted(countries.values()))

davlat=input("Davlatni kiriting:")
poytaxt=''
for key in countries:
    if key.lower()==davlat.lower():
        key=poytaxt
        print(poytaxt)
else:
    print("Bizda bunday ma'lumot yo'q")