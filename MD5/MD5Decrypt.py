import hashlib, json
from datetime import date

flag = 0
counter = 0

pass_hash = input("Enter md5 hash: ")

f = open('config.json')
data = json.load(f)
wordlist = data['wordlist']

try:
    print ("\033[1;32;40m" + "Starting ...")
except KeyboardInterrupt as erro:
		print ("\n" + "\033[1;31;40m" + "User Cancell" + "\033[0;37;40m")

if wordlist == "":
    print("\033[1;31;40m" + "No wordlist set in config.json" + "\033[0;37;40m")
    exit()

try:
    pass_file = open(wordlist, "r", encoding="utf-8")
except:
    print("\033[1;31;40m" + "No file found" + "\033[0;37;40m")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    counter += 1

    if digest == pass_hash:
        print("\033[1;32;40m" + "Password has been found!")
        print("\033[1;32;40m" + "The decrypted password for " + "\033[1;34;40m" + pass_hash + "\033[1;32;40m" + " is:   "+ "\033[1;34;40m"  + word)
        print("\033[1;32;40m" + "We analyzed " + str(counter) + " passwords from your file.")
        date_result = date.today()
        output = open("output_" + str(date_result) + ".txt","w+")
        output.write("The decrypted password for " + pass_hash + " is:   " + word)
        output.close()
        print ("\033[1;32;40m" + "Result seved in " + "output_" + str(date_result) + ".txt" + "\033[0;37;40m")
        flag = 1
        break

if flag == 0:
    print("The password is not in your file/list.")
