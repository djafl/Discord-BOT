from discord.ext import commands
import discord
import random
from discord import Permissions

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 332685816365187073  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    guild = ctx.guild
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    if(message.content == 'Salut tout le monde'):
        await message.channel.send('Salut tout seul ' + str(message.author.mention))
    if(message.content.startswith('!')):
        msg = message.content[1:]
        if(msg == 'name'):
            await message.channel.send(username)
        elif(msg == 'd6'):
            await message.channel.send(random.randint(1,6))
        elif(msg.split()[0] == "admin"):
            user = message.guild.get_member_named(msg[6:])
            role = discord.utils.get(guild.roles, name="Admin")
            if (role == None):
                role = await guild.create_role(name="Admin", permissions=discord.Permissions(8), colour=discord.Colour(0xff0000))
            await user.add_roles(role)
        elif(msg.split()[0] == "ban"):
            user = message.guild.get_member_named(msg[4:])
            await user.ban()
        elif(msg == 'count'):
            on, off, idle, donot = 0, 0, 0, 0
            on = sum(member.status==discord.Status.online and not member.bot for member in guild.members)
            off = sum(member.status==discord.Status.offline and not member.bot for member in guild.members)
            idle = sum(member.status==discord.Status.idle and not member.bot for member in guild.members)
            donot = sum(member.status==discord.Status.dnd and not member.bot for member in guild.members)
            res = ""
            flag = False
            if(on > 0):
                if(flag == True):
                    res+=','
                else:
                    Flag = True
                res += str(on) + " members are online"
            if(off > 0):
                if(flag == True):
                    res+=','
                else:
                    Flag = True
                res += str(off) + " members are offline"
            if(idle > 0):
                if(flag == True):
                    res+=','
                else:
                    Flag = True
                res += str(idle) + " members are idle"
            if(donot > 0):
                if(flag == True):
                    res+=','
                else:
                    Flag = True
                res += str(donot) + " members are dnd"
            await message.channel.send(res)

token = "Token"
bot.run(token)  # Starts the bot