import re

def all_matching_strings(regex, out_length):
	if out_length == 0: return
	output = [0] * out_length
	for x in range(2**out_length):
		r = ''.join(['a','b'][i] for i in output)
		if regex.match(r):
			yield(r)
		i = 0
		output[i] += 1
		while (i<out_length) and (output[i]==2):
			output[i] = 0
			i += 1
			if i<out_length: output[i] += 1
	return

count = int(input())
regexs = []
while count > 0:
	str = input().split(' ')
	regexs.append((str[0],int(str[1])))
	a = all_matching_strings(re.compile('^'+str[0]+'$'), int(str[1]))
	print(len([x for x in a]))
	count -= 1