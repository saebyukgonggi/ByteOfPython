def total(initial=5, *numbers, **keywords):
	count=initial
	print count
	print numbers
	print keywords
	print '---------1-------------'
	for number in numbers:
		print '    #### 1-1 ####'
		print number
		count += number
		print 'count is : ', count
	print '---------2-------------'
	for key in keywords:
		print key
		count += keywords[key]
		print 'count in second for is : ',count
	return count

print total(10,1,2,3, vegetables=50, fruits=100)
