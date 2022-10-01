def arrayEquilibriumIndex(arr):
  totalsum=0
  i=0
  while i<len(arr):
    totalsum=totalsum+arr[i]
    i=i+1
  leftsum=0
  index=0
  while index<len(arr):
    rightsum=totalsum-leftsum-arr[index]
    if rightsum==leftsum:
      return index
    leftsum=leftsum+arr[index]
    index=index+1
  return -1


arr=[1,4,9,3,2]
ans = arrayEquilibriumIndex(arr)
print(ans)