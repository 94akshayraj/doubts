
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
