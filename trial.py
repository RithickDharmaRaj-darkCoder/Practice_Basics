# practice section...

f1 = open('my_data',"a")
#f1.write("1234567890")
f2 = open('trial.py','r')

for data in f2:
    f1.write(data)