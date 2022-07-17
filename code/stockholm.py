import argparse
import os
from cryptography.fernet import Fernet
import socket

#socket
#que hacer cuando las keys empiezan por guion

def parse():

	parser = argparse.ArgumentParser(
		prog = 'python3 stockholm.py', 
		description = 'encrypt/decrypt all files in home dir'
	)	
	parser.add_argument('-v', '--version', action='version', version='Stockholm 1.0')
	parser.add_argument('-r', '--reverse', nargs=1, help='decrypt files', default = None)
	parser.add_argument('-s', '--silent', action='store_true', help = 'silent mode', default = False)
	args = parser.parse_args()
	return args.__dict__


if __name__ == "__main__":
	dict = parse()
	silent = str(int(dict.get("silent")))
	key = dict.get("reverse")
	if (key):
		os.system("./to_decrypt.sh " + key[0] + " " + silent)
	else:
		key = Fernet.generate_key().decode()
		os.system("./to_encrypt.sh " + key + " " + silent)
		print(key)