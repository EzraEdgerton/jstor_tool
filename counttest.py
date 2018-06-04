import json
import sys 

f = open(sys.argv[1], "r")

d = json.load(f)

counts = dict()

for key in d[0]:
	counts[key] = 0
	print key

print counts
total = 0
for a in d:
	if len(a["authors"]) == 0:
		counts["authors"] = counts["authors"] + 1
	for key in counts:

		if a[key] == None:
			counts[key] = counts[key] + 1
	total = total + 1

	
print total
print counts
