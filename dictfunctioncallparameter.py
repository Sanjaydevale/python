# Python3 code to demonstrate working of 
# Functions as dictionary values
# Using Without params
 
def balaji(a,b):
	print("my result bank balance =",a+b)

# initializing dictionary
# check for function name as key
test_dict = {"fname": balaji, "age" : 50, "address" : "salem"}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# calling function using brackets 
test_dict['fname'](10,20)

# printing result 
#print("The required call result : " + str(res)) 
