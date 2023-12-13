# import block
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import dateutil.parser as dp
import os

# Request api
r = requests.get("https://drgapi.com/v1/deepdives")

# Deal with json
data = r.json()
variants = data["variants"]

# Replace "url" with your own webhook url
url = os.environ['URL_VAL']
# Replace "role_id" with the id of the role you want mentioned
role_id = os.environ['ROLE_ID']

# Parse start time stamp
starttimezulu = data["startTime"]
starttime = dp.parse(starttimezulu)
startstamp = starttime.timestamp()
startstamp = int(startstamp)

# Parse end time stamp
endtimezulu = data["endTime"]
endtime = dp.parse(endtimezulu)
endstamp = endtime.timestamp()
endstamp = int(endstamp)

# Set webhook url
webhook = DiscordWebhook(url=url)

# Set embed main info
embed = DiscordEmbed(
  title="Deep Dive Information", 
  description=f"""<@&{role_id}> New Deep Dive just dropped.
  Deep Dive start time: <t:{startstamp}>
  Deep Dive end time: <t:{endstamp}>
  """,
  color = "d4af37"
)

embed.set_timestamp()

# Add Deep Dive information
dd_stage = variants[0]["stages"]

embed.add_embed_field(
  name=f'''
  {variants[0]["type"]}:
  {variants[0]["name"]}
  {variants[0]["biome"]}''',
  
  value=f"""
  > **Stage {variants[0]["stages"][0]["id"]}**
  > Primary Objective: {dd_stage[0]["primary"]}
  > Secondary Objective: {dd_stage[0]["secondary"]}
  > Warning: {dd_stage[0]["warning"]}
  > Anomaly: {dd_stage[0]["anomaly"]}

  > **Stage {variants[0]["stages"][1]["id"]}**
  > Primary Objective: {dd_stage[1]["primary"]}
  > Secondary Objective: {dd_stage[1]["secondary"]}
  > Warning: {dd_stage[1]["warning"]}
  > Anomaly: {dd_stage[1]["anomaly"]}

  > **Stage {variants[0]["stages"][2]["id"]}**
  > Primary Objective: {dd_stage[2]["primary"]}
  > Secondary Objective: {dd_stage[2]["secondary"]}
  > Warning: {dd_stage[2]["warning"]}
  > Anomaly: {dd_stage[2]["anomaly"]}
  """
)

# Add Elite Deep Dive information
edd_stage = variants[1]["stages"]

embed.add_embed_field(
  name=f'''{variants[1]["type"]}:
  {variants[1]["name"]}
  {variants[1]["biome"]}''',
  
  value=f"""
  > **Stage {variants[1]["stages"][0]["id"]}**
  > Primary Objective: {edd_stage[0]["primary"]}
  > Secondary Objective: {edd_stage[0]["secondary"]}
  > Warning: {edd_stage[0]["warning"]}
  > Anomaly: {edd_stage[0]["anomaly"]}

  > **Stage {variants[1]["stages"][1]["id"]}**
  > Primary Objective: {edd_stage[1]["primary"]}
  > Secondary Objective: {edd_stage[1]["secondary"]}
  > Warning: {edd_stage[1]["warning"]}
  > Anomaly: {edd_stage[1]["anomaly"]}

  > **Stage {variants[1]["stages"][2]["id"]}**
  > Primary Objective: {edd_stage[2]["primary"]}
  > Secondary Objective: {edd_stage[2]["secondary"]}
  > Warning: {edd_stage[2]["warning"]}
  > Anomaly: {edd_stage[2]["anomaly"]}
  """
)

# Add the embed and post the webhook.

webhook.add_embed(embed)

response = webhook.execute()
