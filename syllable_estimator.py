
def estimate(s):
	word = s.lower()
	vowels = ['a','e','i','o','u']
	est = 0
	if word[-1] == 'e':
		word = word.rstrip('e')
	elif word[-1] == 'y':
		est +=1
	i = 0
	while i < len(word):
		if word[i] in vowels:
			while word[i] in vowels:
				i +=1
			est +=1
		i +=1
	return est

"""
s = 'thorough'
syl = estimate(s)
print(s)
print(syl)
"""