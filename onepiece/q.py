from array import *
import os
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


def doitnow():
    k = 0
    while k < howmany:
        os.system('megareg --register --email {0} --name "Dis Cinema" --password "Lord7418529630"'.format(em[k]))
  
        k+=1
       
    
doitnow()
