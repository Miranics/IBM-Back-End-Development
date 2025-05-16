testfile= ["bycpp" , "byjava", "bypython", "bycsharp"]
testfile2= ["bycpp" , "byjava", "bypython", "bycsharp"]
testfile3= ["bycpp" , "byjava", "bypython", "bycsharp"]

for x in testfile:
    print(x)
    if x == "bypython":
        break
for x in testfile2:
    print(x + " is a programming language")


mytest= 75
while mytest < 100:
    print(mytest)
    mytest += 2


mytest01= 71
if mytest01 > 90:
    print("Excellent Job!")
elif mytest01 > 80:
    print("Good work, keep it up")
elif mytest01 > 70:
        print("Good")
else:
    print("You need to work harder")

