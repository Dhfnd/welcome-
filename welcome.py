from keep_alive import keep_alive
import os
import random
from os import system
import urllib
import json
from json import dumps, load
import argparse
from urllib.request import urlopen
import aminofix as amino, concurrent.futures, getpass
system("pip install gtts")
system("pip install requests")
import amino
import time
from gtts import gTTS
import requests
from uuid import uuid4
keep_alive()
client=amino.Client()
os.system("clear")
print("\t\033[1;32m Alexa1.0  \033[1;36m Community Bot \n\n")
email="e2nupyuol@wwjmp.com"
password="password"

client.login(email=email,password=password)

cid="9269450"
cidy=9269450

adm=[]
self=client.socket
def generate_transaction_id(self):
        return str(uuid4())
transaction=generate_transaction_id(self)

admx=["http://aminoapps.com/p/gwwmuy"]

client.join_community(cid)
for i in admx:
	try:
		w=client.get_from_code(i).objectId
		adm.append(w)
	except:
		print("Invalid link")
subclient=amino.SubClient(comId=cid,profile=client.profile)
msg="""Follow GC rules
1.Do not spam
2.Respect Leaders, curators, Host and Cohosts
3.Don't spread hate
4.Be polite in chatrooms"""
print("Bot joined community")
subclient=amino.SubClient(comId=cid,profile=client.profile)
print("Joining All chatrooms")
subclient=amino.SubClient(comId=cid,profile=client.profile)
chts=subclient.get_public_chat_threads(type="recommended", start=0, size=100).chatId
for chats in chts:
	try:
		subclient.join_chat(chatId=chats)
	except Exception:
		pass   				
print("Joined all chatrooms")
print("Alexa 1.0 Ready")
l=[]
lis = ["It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful","yes","No" ,"Probably","100%", "Not sure"]

@client.event("on_group_member_join")
def on_group_member_join(data):
	if data.comId==cidy:
		try:
			x=data.message.author.icon
			response=requests.get(f"{x}")
			file=open("sample.png","wb")
			file.write(response.content)
			file.close()
			img=open("sample.png","rb")
			subclient.send_message(chatId=data.message.chatId,message=f"""
[C]━━━━━━━━━━━━━━━
[c]Welcome <${data.message.author.nickname}$>
[C]━━━━━━━━━━━━━━━
{msg}
[C]━━━━━━━━━━━━━━━""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
			print(f"\nwelcomed {data.message.author.nickname} to gc ")
		except Exception as e:
			print(e)
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()