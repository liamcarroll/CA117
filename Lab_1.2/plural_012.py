#!/usr/bin/env python3

import sys

def plural(noun):
	if noun[-2:] in ['ch','sh'] or noun[-1] in ['x','s','z','o']:
		 


def main():
	for line in sys.stdin:
		word = line.strip()
		print(plural(word))