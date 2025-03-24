#!/usr/bin/python3

# Generates the new_225.json file.

bltid = 1

# start of the array
print("[\n")

# 1. 12 Licenses for anywhere in the city

for i in range(1,13):
    print('''  {
    "releaseYear": 2025,
    "restrictzip": "",
    "restrictdetail": "Anywhere",
    "bltID": "''' + str(bltid) + '''",
    "businessID": ""
  },''')
    bltid += 1

# 2. 3 Licenses for Oak Sq. in Brighton

for i in range(1,4):
    print('''  {
    "releaseYear": 2025,
    "restrictzip": "",
    "restrictdetail": "OakSq",
    "bltID": "''' + str(bltid) +'''",
    "businessID": ""
  },''')
    bltid += 1


# 3. 15 licenses for non-profits and theaters
for i in range(1,16):
    print('''  {
    "releaseYear": 2025,
    "restrictzip": "",
    "restrictdetail": "NonProfitAndTheater",
    "bltID": "''' + str(bltid) + '''",
    "businessID": ""
  },''')
    bltid += 1

# 4. 5 licenses per targeted zip code x 3 years x 13 zip codes = 195 licenses
zips = ["02118", "02119", "02121", "02122", "02124", "02125", "02126", "02128", "02129", "02130", "02131", "02132", "02136"]
years = [2025, 2026, 2027]


for y in years:
    for z in zips:
        # print(z)
        for i in range(1,6):
            print('''  {
    "releaseYear": ''' + str(y) + ''',
    "restrictzip": "''' + str(z) + '''",
    "restrictdetail": "zipcode",
    "bltID": "''' + str(bltid) + '''",
    "businessID": ""
  }''' + ("," if bltid < 225 else "") )
            bltid += 1


# end array
print("]")
