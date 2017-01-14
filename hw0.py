import sys
import datetime

print ("ahusse21@uic.edu")
name = ["Abdulrahman", "Hussein"]
print (name)

i = datetime.datetime.now()

print("%s" % i)

def four(start, stop, step):
    result = []
    while(start < stop):
        result.append(start)
        start = start + step
    return result

print (four(17, 40, 6))


print (sys.version)
