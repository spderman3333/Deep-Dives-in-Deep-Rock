import json
import os
import requests


r = requests.get("https://drgapi.com/v1/deepdives")

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
stages = variants[0]["stages"]
stage_1 = variants[0]["stages"][0]
stage_2 = variants[0]["stages"][1]
stage_3 = variants[0]["stages"][2]


# print(dive_type)
# print(dive_codename)
# print(dive_biome)
# print(dive_seed)

list = []
for i in range(3):
  # print(stages[i])
  list.append(stages[i])
print(list)



# message = f"""{dive_type} | {dive_codename} | {dive_biome} | {dive_seed}
# Dive Stages:
# Stage 1:
# Primary: {stage_1["primary"]}
# Secondary: {stage_1["secondary"]}
# Anomaly: {stage_1["anomaly"]}
# Warning: {stage_1["warning"]}"""
# print(message)