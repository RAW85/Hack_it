import string
import time
import os
import signal
from random import randint

def handler(signum, frame):
    os.system('color F')
    os.system('cls')
    exit(1)

n = 86
s = string.ascii_letters + string.digits + string.punctuation
active = [False]*n
os.system('color A')
signal.signal(signal.SIGINT, handler)

while True:
	for _ in range(int(n*.2)):
		x = randint(0,n-1)
		active[x] = not active[x]
	temp = ""
	for i in range(n):
		x = randint(0,len(s)-1)
		temp += s[x]+" " if active[i] else "  "
	print(temp)
	time.sleep(1/20)