#!/usr/bin/env python3

import sys

def char_class(character):
   if character.isdigit():
      return 'digit'
   elif character.islower():
      return 'lower'
   elif character.isupper():
      return 'upper'
   else:
      return 'special'

def pw_security(password):
   classes = {}
   for char in password:
      if char_class(char) not in classes:
         classes[char_class(char)] = True
   return len(classes)

def main():
   for line in sys.stdin:
      pw = line.strip()
      print(pw_security(pw))

if __name__ == '__main__':
   main()