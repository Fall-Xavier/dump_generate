import requests,re,random
ses=requests.Session()

depan = input(" masukan id depan (cth:1008) : ")

for z in range(10000):
	uid = str(depan)+str(random.randint(1111111111,9999999999))
	url = ses.get("https://mbasic.facebook.com/"+uid).text
	nama = re.findall("<title>(.*?)</title>",url)[0]
	if "Konten Tidak Ditemukan" in nama:
		pass
	else:
		if "Masuk Facebook" in nama:
			pass
		else:
			print(uid+"<=>"+nama.replace(" | Facebook",""))
