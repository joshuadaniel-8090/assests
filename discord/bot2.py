import discord
import subprocess
import os

# Your bot token from the Discord Developer Portal
TOKEN = 'MTI5ODkxMTI4MjU4OTg1OTg2MA.GhC2-U.9ABQ-dsZxwbaidFmaOxtbI40V4TQrMi0VwNRIA'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Set the working directory
os.chdir("C:\\Users\\jjosh")  # Set this to the directory you want

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    cmd = message.content.strip()
    print(cmd)

    if not cmd:
        await message.channel.send("Please provide a command to execute.")
        return

    try:
        # Execute the command in the specified directory
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        # If the command is successful, send the output
        if result.returncode == 0:
            await message.channel.send(f"Output:\n{result.stdout}")
        else:
            await message.channel.send(f"Error:\n{result.stderr}")
    except Exception as e:
        # In case of any exception, send it back to the channel
        await message.channel.send(f"An error occurred: {str(e)}")

# Run the bot
client.run(TOKEN)







































# import discord
# import subprocess
# import os

# TOKEN = 'MTI5ODkxMTI4MjU4OTg1OTg2MA.GhC2-U.9ABQ-dsZxwbaidFmaOxtbI40V4TQrMi0VwNRIA'

# intents = discord.Intents.default()
# client = discord.Client(intents=intents)

# # COMMAND_PREFIX = '!'

# @client.event
# async def on_ready():
#     print(f'Logged in as {client.user}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     # if message.content.startswith(COMMAND_PREFIX):
#     cmd = message.content #[len(COMMAND_PREFIX):].strip()
#     print(cmd)

#     if not cmd:
#         await message.channel.send("Please provide a command to execute.")
#         return

#     try:
#         result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

#         if result.returncode == 0:
#             await message.channel.send(f"Output:\n{result.stdout}")
#         else:
#             await message.channel.send(f"Error:\n{result.stderr}")
#     except Exception as e:
#         await message.channel.send(f"An error occurred: {str(e)}")

# client.run(TOKEN)
