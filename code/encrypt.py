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
	with open(sys.argv[1], "r") as file:
		message = file.read()
except Exception:
	print_wrapper("\033[1;31m" + "Couldn't open " + sys.argv[1])
	reset_print_exit()

f = Fernet(sys.argv[2].encode())
encrypted_msg = f.encrypt(message.encode())

try:
	with open(sys.argv[1] + ".ft", "wb") as file:
		file.write(encrypted_msg)
		print_wrapper("\033[1;32m" + sys.argv[1] + " has been encrypted")
except Exception:
	print_wrapper("\033[1;31m" + "Couldn't open " + sys.argv[1] + ".ft")
	reset_print_exit()

try:
	os.remove(sys.argv[1])
except Exception:
	print_wrapper("\033[1;31m" + "Couldn't remove " + sys.argv[1])

reset_print_exit()