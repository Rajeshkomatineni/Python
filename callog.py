import json
def callList(k):
 c=0 
 if type(k)==list:
  for i in k:
   c+=1
  return c
 else:  
  for i in k:
   c+=1
  return c
with open('newdata1.json') as data_file:
	data = json.load(data_file)	
list1 = []
Var =raw_input("Enter Your IMEI Number:")
k=data["users"][Var]["callList"]
c=callList(k)
print "Number of Records:",c
  