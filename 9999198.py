
def sum(num):
	if (beg + mid) == end:
		# return True
		print("True")
	else:
		print("False")



num = str(input())


if len(num) == 7:
	end = int(num[-3:])
	mid = int(num[2:4])
	beg = int(num[0:2])

else:
	print("False")

print(type(sum(num)))



##############################################

num = input() 
for i in range(len(num)):
	for j in range(i+1,len(j)):
		for k in range(j+1,len(k)):
			if num[i:j] + num[j:k] = num[k:range(len(num))]:
				print True
