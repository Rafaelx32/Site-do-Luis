from datetime import datetime


a=0


b= datetime.now()

while a < 1000000:
    print(a)
    a+=1

print(datetime.now()-b)