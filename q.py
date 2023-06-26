from array import *
import subprocess
import os
from pynada import Pynada
import time


nada = Pynada()

def clear():
    os.system('reset')
em = []

clear()
kam = input("How Many Accounts You Will Create Today :\n")
howmany = int(kam)
start_from = input("Start From discinema_??@getnada.com write the number only:\n")
in_start = int(start_from)
end_of = in_start + howmany -1

i = 0

while i < howmany:
        
    if in_start <= end_of:
        em.append("discinema_" + str(in_start) + "@getnada.com")
        
    clear()
    in_start+=1
    i+=1



def register_megatools(email):
    command = 'megatools reg --register --email {0} --name "Dis Cinema" --password "Lord7418529630"'.format(email)
    output = subprocess.check_output(command, shell=True, encoding='utf-8')
    return output

def extract_registration_command(output):
    start_index = output.index('megatools reg --verify')
    end_index = output.index('@LINK@')
    command = output[start_index:end_index].strip()
    return command

def append_link_in_command(command, link):
    return command +" "+ link

def doitnow():
    k = 0
    while k < howmany:
        #os.system('megatools reg --register --email {0} --name "Dis Cinema" --password "Lord7418529630"'.format(em[k]))
        output = register_megatools(em[k])
        cmd = extract_registration_command(output)
        # Wait for 5 seconds
        print("will wait 5 seconds to get email\n")
        time.sleep(5)
        newLink = ""
        for email in nada.inbox(em[k]).get_emails():
            email_contents = email.get_contents()
            #print(email_contents)
            if email_contents[0].startswith("https://mega"):
                newLink = email_contents[0]
                email.delete()
        if newLink.startswith("https://mega"):
            cmd = append_link_in_command(cmd,newLink)
            output = subprocess.run(cmd, shell=True)
            print(output)
        else: 
            print("Error: no link, please envolve!")
        
        clear()
        k+=1
       
    
doitnow()
