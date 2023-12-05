import json
import os
import requests
from posthook import Posthook as ph


r = requests.get("https://drgapi.com/v1/deepdives")
web_url = os.environ['URL_VAL']
message = ""

# print(r.status_code)
# print(r.text)

with open("info.json", "w") as file:
  json.dump(
    r.json(), file,
    indent=4,
    separators=(',', ': '), 
    sort_keys=False
  )

with open("info.json", "r") as file:
  data = json.load(file)

# print(data)
variants = data["variants"]
# for i in variants[0]['stages']:
#   print(str(i["id"]) + i["primary"])

dive_type = variants[0]["type"]
dive_codename = variants[0]["name"]
dive_biome = variants[0]["biome"]
dive_seed = variants[0]["seed"]
stage_1 = variants[0]["stages"][0]
stage_2 = variants[0]["stages"][1]
stage_3 = variants[0]["stages"][2]

mydict = {}

print(dive_type)
print(dive_codename)
print(dive_biome)
print(dive_seed)

for key, val in stage_1.items():
  print(str(key) + " : " +str(val))
  

message = ""
# ph(web_url, message)