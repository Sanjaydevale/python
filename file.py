fileptr = open("prem.txt","r")    
    
if fileptr:    
    print("file is opened successfully")
    
    
    
    
    
    
    
    
    
    
    
'''   
file = open('balaji.txt','w')  
file.write("Happy Summer-too bore")  
file.write("Take care")  
file.close()
'''

fileptr = open("prem.txt","a")
#content = fileptr.read(15)
fileptr.write(" come to my city- its famous for mango- salem.")    
print(fileptr)

    
if fileptr:    
    print("Opened successfully")    
    
#closes the opened file    
fileptr.close()
