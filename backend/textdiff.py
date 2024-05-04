all_names = {}

with open('address_id_latlong.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        lin = line.split(' separator ')
        place = lin[0]
        api = lin[1]
        all_names[place] = 1

duplicate = []
with open('address_id_latlong2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        lin = line.split(' separator ')
        place = lin[0]
        api = lin[1]
        if place not in duplicate:
            duplicate.append(place)
        else:
            print(place)
