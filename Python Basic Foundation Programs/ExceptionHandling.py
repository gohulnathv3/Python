#1 is divide by zero called infinity so we need to set exeception
import sys #print all the error exception

random=['b',0,5]
for entry in random:
    try:
        print("the entry is ",entry)
        d=1/int(entry)
        break
    except:
        print("oops",sys.exc_info(),"occured")
        print("next entry")
print("The reciprocal of ",entry,"is",d)
