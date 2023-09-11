import os
os.system("pip install telebot -y")
from telebot import (TeleBot,types)
from json import (loads,dumps)
from os import path
from time import sleep
import urllib.request,datetime,string
from random import choice,randint
alEx = TeleBot("6424883209:AAFVfPpeanKNSn3QE5DjbtG2J1Lqtz51tKg")
@alEx.message_handler(commands=['start'])
def Start(message):
	K = types.InlineKeyboardMarkup()
	Login = types.InlineKeyboardButton(text="Add Id 📲",callback_data="Login")
	SEND = types.InlineKeyboardButton(text="Send GB❕",callback_data="Send")	
	K.add(SEND,Login)
	
	Name = message.chat.first_name
	alEx.reply_to(message,f'''
Hi bro ( {Name} ) •

- I can increase Gb in ( Warb 1.1.1.1 ) app •

''',reply_markup=K)
@alEx.callback_query_handler(func=lambda call:True)
def ALEX(call):
	if call.data == "Login":
		Back = types.InlineKeyboardMarkup()
		Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
		Back.add(Bback)
		alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''Give me your Id Acc •			
''',reply_markup=Back),Warb)
	
	elif call.data == "Send":
		a,S,s=0,0,0
		if path.exists(f'{call.message.chat.id}warb.json') == False:
			Back = types.InlineKeyboardMarkup()
			Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
			Back.add(Bback)
			alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="You Must login First ❗",reply_markup=Back)
			
		elif path.exists(f'{call.message.chat.id}smtp.json') == True:
			Back = types.InlineKeyboardMarkup()
			Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
			Back.add(Bback)
			with open(f'{call.message.chat.id}warb.json','r') as c:
						Read=loads(c.read())
			IDW = Read['warb']['Id']
			while 1:
				try:
					letters=string.ascii_letters+string.digits
					digit = string.digits
					D = ''.join((choice(digit) for i in range(3)))
					Post = (f'https://api.cloudflareclient.com/v0a{D}/reg')
					key = ''.join(choice(letters) for i in range(43))
					body = {"key": f'{key}=',
"install_id": ''.join(choice(letters) for i in range(22)),"fcm_token": "{}:APA91b{}".format(''.join(choice(letters) for i in range(22)), ''.join(choice(letters) for i in range(134))),"referrer":str(IDW),"warp_enabled": False,"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00","type": "Android","locale": "es_ES"}
					data = dumps(body).encode('utf8')
					headers = {'Content-Type':'application/json; charset=UTF-8','Host': 'api.cloudflareclient.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/3.12.1'}
					reqe = urllib.request.urlopen(urllib.request.Request(Post, data, headers))	
					if reqe.getcode()== 200:
						a+=1			
						Alex = types.InlineKeyboardMarkup()
						Ca = types.InlineKeyboardButton("Cancel •",callback_data="Cancel")
						Sended = types.InlineKeyboardButton(f'''[ 🟢 Sended GB ] > {a}''',callback_data="S")
						UnSended = types.InlineKeyboardButton(f'''[ 🔴 Not Send ] ~> {s}''',callback_data="S")
						Sleep = types.InlineKeyboardButton(f'''[ 🔘 Sleep ] > {S}''',callback_data="S")
						
						Alex.add(Sended)
						Alex.add(UnSended)
						Alex.add(Sleep)
						Alex.add(Ca)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- Im Sending GB …''',reply_markup=Alex)
						sleep(int(randint(8,10)));S+=1
					else:
						
						s+=1			
						Alex = types.InlineKeyboardMarkup()
						Ca = types.InlineKeyboardButton("Cancel •",callback_data="Cancel")
						Sended = types.InlineKeyboardButton(f'''[ 🟢 Sended ] ~> {a}''',callback_data="S")
						UnSended = types.InlineKeyboardButton(f'''[ 🔴 Not Send ] ~> {s}''',callback_data="S")
						Sleep = types.InlineKeyboardButton(f'''[ 🔘 Sleep ] > {S}''',callback_data="S")				
						Alex.add(Sended)
						Alex.add(UnSended)
						Alex.add(Sleep)
						Alex.add(Ca)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- Im Sending GB …''',reply_markup=Alex);sleep(int(randint(8,10)));S+=1
				except Exception as e:
					if "Too Many Requests" in str(e):
						s+=1
						Alex = types.InlineKeyboardMarkup()
						Ca = types.InlineKeyboardButton("Cancel •",callback_data="Cancel")
						Sended = types.InlineKeyboardButton(f'''[ 🟢 Sended ] ~> {a}''',callback_data="S")
						UnSended = types.InlineKeyboardButton(f'''[ 🔴 Not Send ] ~> {s}''',callback_data="S")
						Sleep = types.InlineKeyboardButton(f'''[ 🔘 Sleep ] > {S}''',callback_data="S")				
						Alex.add(Sended)
						Alex.add(UnSended)
						Alex.add(Sleep)
						Alex.add(Ca)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- Im Sending GB …''',reply_markup=Alex);sleep(int(randint(11,15)));S+=1
						
				
					
				
				
	elif call.data == 'Cancel':
		alEx.delete_message(call.message.chat.id,call.message.message_id)
		K = types.InlineKeyboardMarkup()
		Login = types.InlineKeyboardButton(text="Add Id 📲",callback_data="Login")
		SEND = types.InlineKeyboardButton(text="Send GB❕",callback_data="Send")	
		K.add(SEND,Login)
		Name = call.message.chat.first_name
		alEx.send_message(call.message.chat.id,f'''
Hi bro ( {Name} ) •

- I can increase Gb in ( Warb 1.1.1.1 ) app •

''',reply_markup=K)

	elif call.data == 'Back':
		K = types.InlineKeyboardMarkup()
		Login = types.InlineKeyboardButton(text="Add Id 📲",callback_data="Login")
		SEND = types.InlineKeyboardButton(text="Send GB❕",callback_data="Send")	
		K.add(SEND,Login)
		Name = call.message.chat.first_name
		alEx.edit_message_text(text=f'''
Hi bro ( {Name} ) •

- I can increase Gb in ( Warb 1.1.1.1 ) app •

''',chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=K)


def Warb(message):	
	msg = message.text
	Id = message.chat.id
	email={};warb='warb'
	email[warb]= {"Id":str(msg)}
		
	with open(f'{Id}warb.json','w') as s:
			s.write(dumps(email))
	Back = types.InlineKeyboardMarkup()
	Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
	Back.add(Bback)
	alEx.reply_to(message,"Your Id Has Been Saved ❕ ",reply_markup=Back)
			
alEx.polling()