def deepDiveInfo(variant):
  """Get information on Deep Dives, make sure to pass 0 for regular deep dives and 1 for elite dives"""
  # Clears list
  dd_list = []

  # General Information, stored as a list in dd_list
  dive_type = variant["type"]
  dive_codename = variant["name"]
  dive_biome = variant["biome"]
  dive_seed = variant["seed"]

  # Stage info is passed as is.
  stages = variant["stages"]

  dd_list = [dive_type, dive_codename, dive_biome, dive_seed]

  return dd_list, stages




def deepDiveStages():
  while True:
    print()
