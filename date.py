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
k=data["users"][testVar]["callList"]
for i in k.keys():
 if 'calltype' in k[i]:
  b+=1
  if k[i]['calltype']=="OUT":
   if int(k[i]['duration'])>0:
    list3.append(k[i]['number'])
    list1.append(k[i]['timestamp'])
    mydate = list1[c]
    list2.append(mydate[:-14])
    datetime.datetime.strptime(list2[c], "%d-%m-%Y").strftime("%Y-%m-%d")
    c+=1
d=['01-01-2017','31-01-2017']
lo=data["users"][testVar]["contactList"]
for i in lo:
	if 'number1' is not None and 'number1' in i:
	 list4.append((i['number1']))
	 if 'number2' is not None and 'number2' in i:
	  list4.append((i['number2']))
	  if 'number3' is not None and 'number3' in i:
	   list4.append((i['number3']))
	else:
	 pass
s = []
kn=0
ukn=0
ll=0
for i in list3:
 if i not in s:
  ll+=1
  s.append(i)
print "Total out going calls:",c
print "Total persons:",ll
for i in s:
 if i in list4:
  kn+=1
 else:
  ukn+=1  
  
print "Known persons you contacted:",kn
print "UnKnown persons you contacted:",ukn

  #f=list(set(list3) - set(list4)) 
#k=0
#for i in range(0,c):
# if d[0]<list2[i]<d[1]:
#   k+=1
#print k
#print len(f)
#print b 
