from time import *
import random as r 
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
                error =error + 1
    return error 
    
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R =round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)


test =["Strings are defined as an array of characters",
 "The difference between a character array",
 "and a string is the string is terminated with",
 "a special char"]
test1 = r.choice(test)
print(" **** typing speed **** ")
print(test1)
print()
print()

time_1 = time()
testinput=input("Enter : ")
time_2 = time()
print('speed :', speed_time(time_1, time_2, testinput),"w/sec")
print("Error: ",mistake(test1, testinput))

input()
