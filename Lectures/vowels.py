vowels = 'aeiou'

def allvowels(word):
	for c in vowels:
		if c not in word:
			return False
	return True


def extractwords(l):
	return [w for w in l if allvowels(word.casefold())]