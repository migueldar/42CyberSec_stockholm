import sys
import os
from cryptography.fernet import Fernet

try:
	with open(sys.argv[1], "rb") as file:
		en_message = file.read()
		os.remove(sys.argv[1])
except Exception:
	if (int(sys.argv[3]) == 0):
		print("\033[1;31m" + "Couldn't open " + sys.argv[1])
	exit()

f = Fernet(sys.argv[2].encode())
msg = f.decrypt(en_message)

try:
	with open(sys.argv[1][0:-3], "w") as file:
		file.write(msg.decode())
		if (int(sys.argv[3]) == 0):
			print("\033[1;32m" + sys.argv[1] + " has been decrypted")
except Exception:
	if (int(sys.argv[3]) == 0):
		print("\033[1;31m" + "Couldn't open " + sys.argv[1][0:-3] + ".ft")
if (int(sys.argv[3]) == 0):
	print("\033[1;0m", end = "")