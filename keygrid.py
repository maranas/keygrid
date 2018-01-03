#!/usr/bin/python
# keygrid.py
# Generates a grid of characters and symbols from a key

import hashlib
from getpass import getpass

char_lookup = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!,.:;*=#(){}[]<>%'

def get_hashed_user_key():
  hash_string = hashlib.sha512(getpass('Key: ').encode()).hexdigest()
  again = hashlib.sha512(getpass('Again: ').encode()).hexdigest()
  if hash_string != again:
    print("Key mismatch!")
    exit(0)
  quarter = int(len(hash_string)/4)
  left_hash = (hashlib.sha512(hash_string[:quarter].encode()).digest() +
               hashlib.sha512(hash_string[quarter:quarter*2].encode()).digest())
  right_hash = (hashlib.sha512(hash_string[quarter*2:quarter*3].encode()).digest() +
                hashlib.sha512(hash_string[quarter*3:].encode()).digest())
  return left_hash + right_hash

list_length = len(char_lookup)
hash_bytes = get_hashed_user_key()
row_length = 16
row_string = ''

for i in range(len(hash_bytes)):
  index_to_use = int(hash_bytes[i]) % list_length
  row_string = row_string + char_lookup[index_to_use]
  if ((i + 1) % row_length) == 0:
    print(row_string)
    row_string = ''
  else:
    row_string = row_string + ' '


