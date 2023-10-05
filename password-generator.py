#!/bin/env python3

import os
import random
import string
from sys import argv

all_chars = string.ascii_letters + string.digits + '''!@#$%&*()-=+?~{}'''

random.seed = os.urandom(2048)

def generate(length=16):
  password = ""
  for _ in range(int(length)):
    password += random.choice(all_chars)
  return password

def helper():
  txt = '''Password Generator By AliSawari
Generate secure random passwords

use -h to show this help message

usage:
  python3 password-generator.py [length]

- length (number) (optional): specifies the length of the password, default is 16'''
  print(txt)

def main():
  if argv and len(argv) > 1:
    if argv[1] == '-h' or argv[1] == '--help':
      helper()
      return
    else:
      try:
        new_pass = generate(argv[1])
        print(new_pass)
      except:
        print("Wrong Type of arguments, use -h to for help")
  else:
    new_pass = generate()
    print(new_pass)
    

  
main()
