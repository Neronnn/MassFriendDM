import discord

token = "token here"
message = "message here"

client = discord.Client()

@client.event
async def on_connect():
    for friend in client.user.friends:
        try:
            await friend.send(message)
            print(f"Messaged {friend.name}")
        except:
            pass

    for channel in client.private_channels:
        try:
            await channel.send(message)
            print(f"Messaged {friend.name}")
            print("Thanks Neron! :D")
        except:
            pass
            
client.run(token, bot=False)
## run it on VSC, REPLIT or wtv
