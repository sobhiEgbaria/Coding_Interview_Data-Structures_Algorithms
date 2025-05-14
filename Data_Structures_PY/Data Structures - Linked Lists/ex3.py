 
def lenOfLongSubarr(arr):
	maxlength = 0
	indexses = []
	for i in range(len(arr)):
		Sum = 0
		for j in range(i,len(arr)):
			Sum += arr[j]
			if (Sum == 10):
				if maxlength < j - i + 1:
					maxlength = j - i + 1
					indexses = [i,j]
	if len(indexses) == 0:
		return -1
	return indexses

arr = [1,1,1, ]
 
print(lenOfLongSubarr(arr))

