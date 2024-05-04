import unicodedata
import json
from response import dic
ls = dic
count=[]
all_names = {}

for item in ls["value"][1][1][1]:
    all_names[item[13]] = [item[7], item[4][1][0][1]]

count = 0
with open('address_id.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
         lin = line.split(' separator ')
         place = lin[0]
         api = lin[1]
         if place in all_names:
            with open('address_id_latlong.txt', 'a+', encoding='utf-8') as f:
                all_names[place][1] = all_names[place][1][6:-1].split(' ')[::-1]
                all_names[place][1]= ' '.join(all_names[place][1])
                f.write(place + ' separator ' + all_names[place][1] + ' separator ' + all_names[place][0] + ' separator ' + api)
         else:
             print(place)
print(count)



