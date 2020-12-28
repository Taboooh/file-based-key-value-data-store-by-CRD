import threading #this is for python 3.0 
from threading import*
import time

d={} #'d' is the dictionary in which we store data
l=[]
#for create operation 
#timeout is optional you can continue by passing two arguments without timeout

def create():
    print("Enter the key value pair \n")
    key,value=map(str,input().split())
    key=int(key)
    print("Enter timeout")
    timeout=int(input())
    timeout=timeout*60
    if key in d:
        print("error: this key already exists") #error message1
    else:
        if len(d)<(1024*1020*1024) and key<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
            if timeout==0:
                l=[value,timeout]
            else:
                l=[value,time.time()+timeout]
            if len(value)<=32: #constraints for input key_name capped at 32chars
                d[key]=l
                print(d)
                print("key value pair and timeout is created")
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation

            
def read():
    print("Enter key to read the pair\n")
    key=int(input())
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                res=str(key)+":"+str(b[0])
                print(res)
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            res=str(key)+":"+str(b[0])
            print(res)
        
   


#for delete operation
#use syntax "delete(key_name)"

def delete():
    print("Enter the key to delete\n")
    key=int(input())
    if key not in d:
        print("Error: Key does not Exist\n")
        
    else:
        del d[key]
        print(d)
        print("Successfully deleted\n")

def store():
    f=open("tabu.txt",'w+') #it open and write a file
    strc=str(d)
    f.write(strc)
    f=open("tabu.txt",'r') #it open and read a file
    print(f.read())
    f.close()

print("File based key-value data store\n")
i=1
while(i!=5):
    print("Select the operation you want to do:\n")
    print("\n1. Create \n2. Read \n3. Delete \n4. Exit\n")
    opt=int(input())
    if(opt==1):
        create()
    elif(opt==2):
        read()
    elif(opt==3):
        delete()
    elif (opt==4):
        store()
        exit(0)
    else:
        print("Invalid Operation\n")
print(d)
t1=threading.Thread(target=(create or read or delete)) 
t1.start()
time.sleep(1)
t2=threading.Thread(target=(create or read or delete))
t2.start()
time.sleep(1)
