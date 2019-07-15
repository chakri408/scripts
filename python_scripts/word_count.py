import collections
lst = []
with open("test.txt", "r") as gfile:
	for i in gfile:
		j = i.split()
		cnt = collections.Counter(j)
		lst.append(dict(cnt))
		#print(list(cnt))
print(lst)
result = collections.Counter()

#working solution with different logic. 
#for elem in lst:
#	for k,v in elem.items():
#		result[k] += v
#print(dict(result))
for k in lst:
	result.update(k)
print(dict(result))
	

