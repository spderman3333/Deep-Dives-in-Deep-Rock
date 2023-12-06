import requests

r = requests.get("https://drgapi.com/v1/deepdives")

data = r.json()
variants = data["variants"]


def deepDive():
  """Get information on Regular Deep Dives"""
  # Clears list
  dd_list = []

  # General Information, stored as a list in dd_list
  dive_type = variants[0]["type"]
  dive_codename = variants[0]["name"]
  dive_biome = variants[0]["biome"]
  dive_seed = variants[0]["seed"]

  # Stage info is passed as is.
  stages = variants[0]["stages"]

  dd_list = [dive_type, dive_codename, dive_biome, dive_seed]

  return dd_list, stages


def eliteDeepDive():
  """Get information on Elite Deep Dives"""
  # Clears list
  edd_list = []

  # General Information, stored as a list in edd_list
  dive_type = variants[1]["type"]
  dive_codename = variants[1]["name"]
  dive_biome = variants[1]["biome"]
  dive_seed = variants[1]["seed"]

  # Stage info is passed as is.
  stages = variants[1]["stages"]

  edd_list = [dive_type, dive_codename, dive_biome, dive_seed]

  return edd_list, stages
