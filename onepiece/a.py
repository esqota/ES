from array import *
from pathlib import Path
import os
#import sys
#sys.path.append(os.path.abspath("/usr/local/lib/python2.7/dist-packages"))
#from mega import Mega
#mega = Mega()
x = 0
try:
    f = open("/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf")
    os.system('echo "Starting..."')
    x=1
    # Do something with the file
except IOError:
    os.system('echo "Fonts Not Installed"')
    x=0
#finally:
    #f.close()
    
###############################################################################
#func
def clear():
    os.system('reset')

def doitnow():
    k = 0
    while k < howmany:
     #os.system('youtube-dl -f best --console-title --newline --no-warnings --no-part -o "{1}" --user-agent "Mozilla / 5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko / 20100101 Firefox / 65.0" -v --newline {0}'.format(urlar[k],vidnamear[k]))
     os.system('ffmpeg -i {0} -i logo.png  -filter_complex "overlay=5:5:format=auto,format=yuv420p,ass={1}" -filter:a "volume=2" {2}'.format(vidnamear[k],vidsub[k],vidnameoutar[k]))
     os.system('rm -f {0} && rm -f {1}'.format(vidsub[k],vidnamear[k]))
     try:
        os.system('megadf --config a.megarc | tee qouta.txt')
        f = open("qouta.txt", "r")
        x = f.readline()
        y = f.readline()
        z = f.readline()
        qo = z.split(" ")
        yc = qo[2]
        yyy = int(yc)
        #yyy = yyy / (3 * 1024)
        #os.system('echo "You have {0} bytes free"'.format(yyy))
        
        file= Path(r'{0}'.format(vidnameoutar[k])).stat().st_size
        #fz = file / (3 * 1024)
        #os.system('echo "File size {0} bytes"'.format(file))
        os.system('rm -f qouta.txt')
        if file < yyy:
            os.system('megaput {0} --config a.megarc'.format(vidnameoutar[k]))
            #kont b7awel any lw al mlf mtrf34 arf3o 3n try2 lw el upload mktb4 uploading wkda
            #with open('example.txt') as f:
                #if 'Uploaded' in f.read():
                    #os.system('echo "{0} Uploaded Successfully."'.format(vidnameoutar[k]))
        else:
            os.system('echo "Can not upload will upload to another Account"')
            f = open("a.megarc", "r")
            x = f.readline()
            y = f.readline()
            z = f.readline()
            yy = y.split("=")
            xx = yy[1].split("@")
            xxx = xx[0].split("_")
            x_gdeda = int(xxx[1])
            x_gdeda += 1
            usern = "Username = discinema_" + str(x_gdeda) + "@getnada.com"
            os.system('rm -f a.megarc')
            os.system('printf "[Login]\n{1}\n{2}" > {0}'.format("a.megarc",usern,z))
            os.system('megaput {0} --config a.megarc'.format(vidnameoutar[k]))
    
     except:
        os.system('echo "Error on command, Retrying the Whole Process"')
        os.system('megadf --config a.megarc | tee qouta.txt')
        f = open("qouta.txt", "r")
        x = f.readline()
        y = f.readline()
        z = f.readline()
        qo = z.split(" ")
        yc = qo[2]
        yyy = int(yc)
        #yyy = yyy / (3 * 1024)
        #os.system('echo "You have {0} bytes free"'.format(yyy))
        
        file= Path(r'{0}'.format(vidnameoutar[k])).stat().st_size
        #fz = file / (3 * 1024)
        #os.system('echo "File size {0} bytes"'.format(file))
        os.system('rm -f qouta.txt')
        if file < yyy:
            os.system('megaput {0} --config a.megarc'.format(vidnameoutar[k]))
            #kont b7awel any lw al mlf mtrf34 arf3o 3n try2 lw el upload mktb4 uploading wkda
            #with open('example.txt') as f:
                #if 'Uploaded' in f.read():
                    #os.system('echo "{0} Uploaded Successfully."'.format(vidnameoutar[k]))
        else:
            os.system('echo "Can not upload will upload to another Account"')
            f = open("a.megarc", "r")
            x = f.readline()
            y = f.readline()
            z = f.readline()
            yy = y.split("=")
            xx = yy[1].split("@")
            xxx = xx[0].split("_")
            x_gdeda = int(xxx[1])
            x_gdeda += 1
            usern = "Username = discinema_" + str(x_gdeda) + "@getnada.com"
            os.system('rm -f a.megarc')
            os.system('printf "[Login]\n{1}\n{2}" > {0}'.format("a.megarc",usern,z))
            os.system('megaput {0} --config a.megarc'.format(vidnameoutar[k]))
    
     
     os.system('rm -f {0}'.format(vidnameoutar[k]))
     #os.system('touch {0}.py'.format(vidnameoutar[k]))
     #os.system('printf "import sys\nimport os\nsys.path.append(os.path.abspath(\'/usr/local/lib/python2.7/dist-packages\'))\nfrom mega import Mega\nmega = Mega()\nm = mega.login(\'discinema_1@getnada.com\',\'Lord7418529630\')\nfile = m.upload(\'{0}\')\nos.system(\'rm {0}.py && rm {0} && rm {1} && rm {2}\')" > {0}.py'.format(vidnameoutar[k],vidsub[k],vidnamear[k]))
     #os.system('xfce4-terminal -x sh -c "python3 {0}.py; bash"'.format(vidnameoutar[k]))
     k+=1


def uploadit():
    k=0
    while k < howmany:
     os.system('echo "Uploading {0} ..."'.format(vidnameoutar[k]))
     os.system('python3 {0}.py'.format(vidnameoutar[k]))
     os.system('echo "{0} Uploaded Successfully."'.format(vidnameoutar[k]))
     k+=1 
    

#uploadit()
###############################################################################
#do
if x == 1:
    urlar = []
    vidnamear = []
    vidsub = []
    vidnameoutar = []
    clear()
    s_season = input("Season: \n")
    kam = input("How Many Videos You Will Finish Today :\n")
    howmany = int(kam)
    start_from = input("Your start from :\n")
    in_start = int(start_from)
    end_of = in_start + howmany -1
    i = 0
    
    while i < howmany:
        #url = input("Of VID {0}: Crunchyorll URL:\n".format(i+1))
        #urlar.append(url)
        #va = input("Of VID {0}: Video name:\n".format(i+1))
        #vidnamear.append(va+".mp4")
        #vids = input("Of VID {0}: Video Subtitle:\n".format(i+1))
        #vidsub.append(vids+".ass")
        #bd = input("Of VID {0}: Video Number of EP :\n".format(i+1))
        #vidnameoutar.append("[DisCinema.com]_AOT_EP"+bd+".mp4")
        if in_start <= end_of:
            vidnamear.append(str(in_start)+".mp4")
            vidsub.append(str(in_start)+".ass")
            vidnameoutar.append("[DisCinema.com]_Hunter_X_Hunter_S"+ s_season +"_EP"+str(in_start)+".mp4")
       
        clear()
        in_start+=1
        i+=1
        
    doitnow()
else:
    os.system('echo "closing Will install it manaully"')
    os.system('sudo apt-get --reinstall install ttf-mscorefonts-installer')
