#program accepting list of numbers and separate then +ve and -ve lists
#continueex4.py
n=int(input("Enter Values u have:")) # 5
if(n<=0):
	print("{} is invalid  input".format(n))
else:
	lst=list() # Create an empty list for adding dynamic list of values
	for i in range(1,n+1):
		val=int(input("Enter {} Value".format(i)))
		lst.append(val)
	else:
		print("------------------------------------------------------------")
		print("List of Values:{}".format(lst))#[-12, -34, 56, 12, -6, -4, 0, 14, 56, -78]
		print("------------------------------------------------------------")
		#Create Posstive List
		pslist=[] #Create an empty list for appending +ve vals
		for val in lst:
			if(val<=0):
				continue
			pslist.append(val)
		else:
			print("List of +VE Values:{}".format(pslist))#[56, 12, 14, 56]
			print("------------------------------------------------------------")
			#Create Posstive List
			nglist=[] #Create an empty list for appending -ve vals
			for val in lst:
				if(val>=0):
					continue
				nglist.append(val)
			else:
				print("List of -VE Values:{}".format(nglist))#[-12,-34,-6,-4,-78]
				print("------------------------------------------------------------")