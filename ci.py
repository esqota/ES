import os
Season = int(input("Season: "))
frome=int(input("From: "))
toe=int(input("To: "))

lnk = "https://www.crunchyroll.com/series/G63K98PZ6/one-punch-man"
lnk = lnk + "[S" + str(Season)+"E"
output = "\"{episode_number}.ts\""
for ep in range(frome,toe+1):
	d = lnk+str(ep)+"]"	
#	print(d,output)
	os.system(f'crunchy-cli download -a ja-JP -o {output} {d}')