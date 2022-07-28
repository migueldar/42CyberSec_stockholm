import sys
import os
from cryptography.fernet import Fernet

silent = int(sys.argv[3])

def reset_print_exit():
	if (not silent):
		print("\033[1;0m", end = "")
	exit()

def print_wrapper(prt):
	if (not silent):
		print(prt)

try:
	with open(sys.argv[1], "rb") as file:
		en_message = file.read()
except Exception:
	print_wrapper("\033[1;31m" + "Couldn't open " + sys.argv[1])
	reset_print_exit()

try:
	f = Fernet(sys.argv[2].encode())
	msg = f.decrypt(en_message)
except Exception:
	print_wrapper("\033[1;31m" + "Decryption error for " + sys.argv[1])
	reset_print_exit()

try:
	with open(sys.argv[1][0:-3], "wb") as file:
		file.write(msg)
		print_wrapper("\033[1;32m" + sys.argv[1] + " has been decrypted")
except Exception:
	print_wrapper("\033[1;31m" + "Couldn't open " + sys.argv[1][0:-3])
	reset_print_exit()

try: 
	os.remove(sys.argv[1])
except Exception:
	print_wrapper("\033[1;31m" + "Couldn't remove " + sys.argv[1])

reset_print_exit()