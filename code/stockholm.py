import argparse
import os
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(
	prog = 'python3 stockholm.py', 
	description = 'encrypt/decrypt all files in home dir'
)	
parser.add_argument('-v', '--version', action='version', version='Stockholm 1.0')
parser.add_argument('-r', '--reverse', nargs=1, help='decrypt files', default = None)
parser.add_argument('-s', '--silent', action='store_true', help = 'silent mode', default = False)
args = parser.parse_args()
dict = args.__dict__

silent = int(dict.get("silent"))
key = dict.get("reverse")
if (key):
	os.system("./to_decrypt.sh " + key[0] + " " + "1")
else:
	key = Fernet.generate_key().decode()
	os.system("./to_encrypt.sh " + key + " " + "1")
	print(key)