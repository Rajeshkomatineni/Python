import json
with open('sample.json') as data_file:
	data = json.load(data_file)
list1 = []
k=data["users"]["352136067843470"]["contactList"]
for i in k:
	if 'number1' in i:
	 list1.append((i['number1']))
print list1	 
	 