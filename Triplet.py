arr = [1,2,2,4,2]
n = 4 #n0. of elemnets 
m = 5#max value of element 
#for i in range(n):
  #arr.append(int(input()))
#triplet
freq = {}
rem = {}
l = []
for item in arr:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1
count = 0
total = 0
temp1=0
#for key, value in freq.items():
    #print ("% d : % d"%(key, value)) 
print(freq)
#for i in range(len(arr)-1):
  #if arr[i] == arr[i+1] or arr[i] == arr[i+1]+1       
for key,value in freq.items():
  rem[key] = value%3
  temp = value//3
  temp1 += temp
  count+=temp 
for key,value in rem.items():
  total = total+value 
count+=total//3 
  #else:
    #for key,value in freq.items():
      #rem[key] = value%3
      #temp = value//3
      #count+=temp
temp = False
for i in range(len(arr)-1):
  if arr[i] == arr[i+1] or arr[i] == arr[i+1]+1:
    temp = True
  else:
    temp = False
if temp == True:
  print(count)
else:
  print(temp1)
