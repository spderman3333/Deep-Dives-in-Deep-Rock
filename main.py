import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

r = requests.get("https://drgapi.com/v1/deepdives")

data = r.json()
variants = data["variants"]

# Change this out for your webhook url
# replace (your_role_id_here) with the role id of the role you want to be mentioned when used.
url = "put_webhook_url_here"
role_id = "your_role_id_here"


webhook = DiscordWebhook(url=url)



embed = DiscordEmbed(
  title="Deep Dive Information", 
  description=f"<@&{role_id}> New Deep Dive just dropped.",
  color = "d4af37"
)

dd_stage = variants[0]["stages"]

embed.set_timestamp()

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

edd_stage = variants[1]["stages"]

embed.add_embed_field(
  name=f'''{variants[1]["type"]}:
  {variants[1]["name"]}
  {variants[1]["biome"]}''',
  
  value=f"""> **Stage {variants[1]["stages"][0]["id"]}**
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
  > Anomaly: {edd_stage[2]["anomaly"]}"""
)



webhook.add_embed(embed)

response = webhook.execute()
