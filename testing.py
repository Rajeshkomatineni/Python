import json
import datetime
import time
with open('newdata.json') as data_file:
	data = json.load(data_file)	
list1 = []
list2 = []
list3 = []
list4 = []
b=0
c=0
testVar =raw_input("Enter Your IMEI Number:")
k=data["users"][testVar]["contactList"]
if type(k)==list:
 for i in k:
  print i
else:
 print "hai"  