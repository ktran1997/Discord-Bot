import discord
import audioread
from time import sleep

from discord.ext import commands
from discord.utils import get

TOKEN = 'Key'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	#allows bot to change status
	activity = discord.Game(name="with the API")
	#allows bot to change its presence, offline to online
	await client.change_presence(status=discord.Status.idle, activity=activity)
	print('Bot online.')

#checks to see if the member's state changed
@client.event
async def on_voice_state_update(member, before, after):
	if before.channel == after.channel:
		return 
	if before.channel is None:
		#uncomment and comment below code if you want to just send a textchannel message
		#instead of using an audio file. 
		#change tts to false or true if you want to allow text to speech
		#await member.guild.system_channel.send("Hello!", tts=True)
		channel = member.voice.channel
		vc = await channel.connect()
		sleep(0.5)
		vc.play(discord.FFmpegPCMAudio("audioFile1.mp3"))
		with audioread.audio_open("audioFile1.mp3") as f: 
			sleep(f.duration)
		await vc.disconnect()
	elif after.channel is None: 
		await member.guild.system_channel.send("Bye Bye")#,tts=True) 

client.run(TOKEN)
