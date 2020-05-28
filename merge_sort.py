def merge_sort(s): 
	if len(s)<2:
		return(s)
	else:
		left=merge_sort(s[:len(s)//2])
		right=merge_sort(s[len(s)//2:])
		return(merge(left,right))

def merge(left,right): 
	i,j = 0,0
	result=[]
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		else: 
			result.append(right[j])
			j+=1 

	if i==len(left): result.extend(right[j:])
	if j==len(right): result.extend(left[i:])
	return(result)
