#Efficient jannitor
arr = [1.01,1.99,2.5,1.5,1.01]
arr.sort()
left = 0
n = len(arr)
minm = 1.01
maxm = 3
sum1 = sum(arr) 
#index = list(range(n))
#index.sort(key = lambda i:arr[i],reverse = True)
count = 0 
for i in range(n-1,-1,-1):
  if arr[i]>=minm and arr[i]<=maxm:
    maxm = maxm-arr[i] 
    if arr[left]<=maxm:
      maxm = maxm-arr[left]
      left+=1 
    if maxm<minm:
      count+=1
      maxm = 3
  if left>=i:
    break


print(count)
