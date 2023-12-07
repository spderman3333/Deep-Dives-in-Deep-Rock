import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from deepdives import deepDiveInfo
from random import randint

r = requests.get("https://drgapi.com/v1/deepdives")

data = r.json()
variants = data["variants"]

test_list, stage = deepDiveInfo(variants[0])




for s in stage:
  dd_stage = 'stage ', s['id']
  dd_primary = 'primary objective:', s['primary']
  dd_secondary = 'secondary objective:', s['secondary']
  dd_warnings = "warning:", s['warning']
  dd_anomaly = 'anomaly:', s['anomaly']


test_list, stage = deepDiveInfo(variants[1])
for s in stage:
  eed_stage = 'stage ', s['id']
  eed_primary = 'primary objective:', s['primary']
  edd_secondary = 'secondary objective:', s['secondary']
  eed_warning ="warning:", s['warning']
  edd_warning = 'anomaly:', s['anomaly']

         
# Add the webhook stuff

url = "https://discord.com/api/webhooks/1181114522203852800/u60JLs9m5QxNPFZzq-1C4maRJPrtpSWuqgY9jtwDbk4Zg6eroap1yObcnwFb4MpYKHFk"

webhook = DiscordWebhook(url=url)

embed = DiscordEmbed(
  title="Deep Dive Information", 
  description="Information on this weeks DRG's Deep Dives, both elite and regular.",
  color = "13938487"
)

webhook.add_embed(embed)

response = webhook.execute()