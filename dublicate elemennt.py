nandan=[10,20,30,40,50]
rathod=[60,70,80,90,100,20]
nandan_rathod=nandan+rathod
print(nandan_rathod)
for i in nandan:
    for j in rathod:
        if i==j:
            print('duplicate element is',i)
         