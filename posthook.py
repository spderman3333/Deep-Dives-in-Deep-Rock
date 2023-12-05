from discord_webhook import DiscordWebhook

def Posthook(user_entered_url, message):
  webhook = DiscordWebhook(
  url=user_entered_url,
  content=message
  )

  response = webhook.execute()
  return response