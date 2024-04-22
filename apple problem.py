apple=[10,5,30]
print(apple)
print(apple[1])
print(apple[-1])
print(apple[-3])
#print(apple[4])
print("for interation via access elements")
for i in apple:
    print(i)
print("after changed")
apple[1]=-100
print(apple)