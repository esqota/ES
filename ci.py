import os
Season = int(input("Season: "))
frome=int(input("From: "))
toe=int(input("To: "))

lnk = "https://www.crunchyroll.com/series/GYGG99WDY/charlotte"
lnk = lnk + "[S" + str(Season)+"E"
output = "\"{episode_number}.ts\""
for ep in range(frome,toe+1):
	d = lnk+str(ep)+"]"	
#	print(d,output)
	os.system(f'crunchy-cli download -a ja-JP -o {output} {d}')