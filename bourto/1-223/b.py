from array import *
import os
#import sys
#sys.path.append(os.path.abspath("/usr/local/lib/python2.7/dist-packages"))
#from mega import Mega
#mega = Mega()
def clear():
    os.system('reset')
urlar = []
vidnamear = []
vidsub = []
vidnameoutar = []
clear()
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
         vidnameoutar.append("[DisCinema.com]_Naruto_Shippuden_S1_EP"+str(in_start)+".mp4")
       
    clear()
    in_start+=1
    i+=1


def doitnow():
    k = 0
    while k < howmany:
     #os.system('youtube-dl -f best --console-title --newline --no-warnings --no-part -o "{1}" --user-agent "Mozilla / 5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko / 20100101 Firefox / 65.0" -v --newline {0}'.format(urlar[k],vidnamear[k]))
     os.system('ffmpeg -i {0} -i logo.png  -filter_complex "overlay=5:5:format=auto,format=yuv420p,ass={1}" {2}'.format(vidnamear[k],vidsub[k],vidnameoutar[k]))
     #os.system('ffmpeg -i {0} -i logo.png  -filter_complex "overlay=3:3:format=auto,format=yuv420p,ass={1}" {2}'.format(vidnamear[k],vidsub[k],vidnameoutar[k]))
     #os.system('rm -f {0} && rm -f {1}'.format(vidsub[k],vidnamear[k]))
     #os.system('megaput {0} --config a.megarc'.format(vidnameoutar[k]))
     #os.system('echo "{0} Uploaded Successfully."'.format(vidnameoutar[k]))
     #os.system('rm -f {0}'.format(vidnameoutar[k]))
     #last way
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
    
    
doitnow()
#uploadit()
