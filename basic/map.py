#
# Author: Rohtash Lakra
#
import json
from collections import namedtuple

food_json = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55
}

print()
print("Food's JSON")
print(food_json)
print()

food_dict = {}
for key in food_json:
    food_dict[key] = food_json[key]

print()
print("Food's Dictionary")
print(food_dict)
print()

# food_obj = json.loads(food)
# food_obj = json.loads(food_json, object_hook=lambda entry: namedtuple('Food', entry.keys())(*entry.values()))

# check not empty
if food_dict:
    for key in food_dict:
        print(f"{key} = {food_dict.get(key)}")

#  check emtpy
if not food_dict:
    print("food_dict is emtpy")





data = [{"name":"tobi","class":"1","age":"14", "gender":"m"},{"name":"joke","class":"1","age":"18", "gender":"f"}, {"name":"mary","class":"2","age":"14", "gender":"f"},{"name":"kano","class":"2","age":"15", "gender":"m"},{"name":"ada","class":"1","age":"15", "gender":"f"},{"name":"bola","class":"2","age":"10", "gender":"f"},{"name":"nnamdi","class":"1","age":"15", "gender":"m"}]
