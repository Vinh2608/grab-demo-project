from collections import Counter
import requests
import json

def print_duplicates(lst):
    counter = Counter(lst)
    for item, count in counter.items():
        if count > 1:
            print(item)

# Example usage


# ls = []
# with open('address_id.txt', 'r', encoding = 'utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         ls.append(line.split(' separator ')[0])
# print_duplicates(ls)
url = 'http://camera.thongtingiaothong.vn/api/snapshot/63ae7a50bfd3d90017e8f2b2     '
response = requests.get(url)
print(response.text)
