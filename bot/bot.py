import discord
import logging

logging.basicConfig(level=logging.INFO)

cli = discord.Client()

intents = discord.Intents.default()

p_channels = [797634311905738783, 797634937594708038, 797635544255168522, 797635705755926538, 
797636051836993546, 797637409458094140, 797637561992085514, 797637707597742095,
797637802182574110, 797637926397673472, 797688928865091625, 801615042201124864]

new_messages = []

profanity = ['fuck', 'fuckery', 'wtf', 'fucking', 'fucks', 'FUCK', 'shit', 'bullshit', 'bullshittery', 'bullshitting', 'motherfucker', 'MOTHERFUCKER', 'bitch', 'BITCH', 'ass', 'assfuckery', 'assfucking a bitch', 'ok that wasnt even a swear word i just wanted to type that']

#async def process_command(command):


@cli.event
async def on_message(message):
    global new_messages
    words = message.content.split()
    for i in words:
        if i in profanity:
            await message.channel.send("Woah there! Watch the profanity " + message.author.mention)
            await message.delete()
            break
    if "orz" in message.content:
        await message.channel.send("https://cdn.discordapp.com/attachments/798804481062993924/804575054117208084/745513885523509330.png")
    if message.channel.id == 796911223668998144 and message.content.startswith("> "):
        await message.add_reaction('\u2611')
        await message.add_reaction('\u274C')
    if message.channel.id == 796911223668998144 and message.content.startswith("item:"):
        await message.add_reaction('\u274C')
    if message.author == cli.user:
        return
    if message.channel.id == 796911223668998144 and message.content.startswith("$send"):
        for i in new_messages:
            await cli.get_channel(798055248962256936).send(i)
        new_messages = []
        await message.channel.send("sent & cleared boiiiss")
    if message.channel.id == 796911223668998144 and message.content.startswith("$clear"):
        new_message = []
        await message.channel.send("cleared boiiiss")
    if message.channel.id == 796911223668998144 and message.content.startswith("$title"):
        await cli.get_channel(798055248962256936).send(message.content[7:])
    if message.channel.id == 796911223668998144 and message.content.startswith("$queue"):
        await cli.get_channel(796911223668998144).send("Current Queue:")
        for i in new_messages:
            await cli.get_channel(796911223668998144).send("item: " + i)
    if message.content.startswith("no u"):
        await message.channel.send('no u')
    if message.content.startswith("how to life"):
        await message.channel.send('just don\'t')
    #if message.content.startswith("miku"):
    #    await message.channel.send('kawaiiiiiiiiiii')
    
    new_message = '> ' + message.content + '\n -' + message.author.mention
    for i in p_channels:
        if i == message.channel.id:
            await cli.get_channel(796911223668998144).send("NEW MESSAGE")
            await cli.get_channel(796911223668998144).send(new_message)
            #await message.delete()
            return

@cli.event
async def on_reaction_add(reaction, user):
    global new_messages
    if user == cli.user:
        return
    
    message = reaction.message
    roles = user.roles
    if message.channel.id != 796911223668998144:
        return
    
    ok = 0
    for i in roles:
        if i.name == 'Officer':
            ok = 1
            break
    if ok == 0: 
        return

    #new_message = message.author.display_name + ' said:\n' + message.content

    if(reaction.emoji == '\u2611'): # and (message.content,user) not in new_messages
        new_messages.append(message.content)
         #copy this to the send messages function
         #await message.delete()
    elif (reaction.emoji == '\u274C'):
        if (message.content.startswith("item:")):
            for i in new_messages:
                if (message.content[6:] == i):
                    new_messages.remove(i)
                    break
            await message.delete()
        elif (message.content.startswith("> ")):
            await message.delete()
    #elif (reaction.emoji == '\U0001F595'): 
    #await message.delete()
cli.run('Nzk3NzI1NTI4MjU3MDY5MDU3.X_qpyg.7zliG4DBTn_CQlssa97Knc6dkj0')
