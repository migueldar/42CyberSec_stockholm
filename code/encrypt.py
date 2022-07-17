import sys
import os
from cryptography.fernet import Fernet

try:
	with open(sys.argv[1], "r") as file:
		message = file.read()
		os.remove(sys.argv[1])
except Exception:
	if (int(sys.argv[3])):
		print("\033[1;31m" + "Couldn't open " + sys.argv[1])
	exit()

f = Fernet(sys.argv[2].encode())
encrypted_msg = f.encrypt(message.encode())

try:
	with open(sys.argv[1] + ".ft", "wb") as file:
		file.write(encrypted_msg)
		if (int(sys.argv[3])):
			print("\033[1;32m" + sys.argv[1] + " has been encrypted")
except Exception:
	if (int(sys.argv[3])):
		print("\033[1;31m" + "Couldn't open " + sys.argv[1] + ".ft")
if (int(sys.argv[3])):
	print("\033[1;0m", end = "")