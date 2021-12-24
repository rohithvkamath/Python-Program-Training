import os
import time as t
clear = lambda: os.system('cls')

import getpass as gp

class username:                                 #using a class to store and compare the data.
    def __init__(self,user_name,password):      #in-built function for storing the data.
        self.user_name=user_name
        self.password=password
    def verification(user,pas):                 #function to compare the datails and give the output
        if user==p1.user_name or user== p2.user_name or user== p3.user_name and pas==p1.password or pas==p2.password or pas==p3.password:
                print("Welcome\n",user)
        else:
            print("Entered credentials are wrong")  
choice=-1                   #initialization of choice variable
n=1
i=2
while(choice!=4):
    clear()
    print("Enter your choice\n1.Sign-up\n2.Log-in\n3.Log-out\n4.Exit")
    choice=int(input())
    if choice==1:
        a=input("Enter the USERNAME\n")
        b=gp.getpass("Enter the PASSWORD\n")
        c=gp.getpass("Confirm the PASSWORD\n")
        if b==c:
            if n==1:
                p1=username(a,c)
                print("User 1 signned up")
            elif n==2:
                p2=username(a,c)
                print("User 2 signned up")
            elif n==3:
                p3=username(a,c)
                print("User 3 signned up")
            else:
                clear()
                print("user full\n")
                t.sleep(2)
            n+=1
            i=1
        else:
            clear()
            print("Passwords do not match\n")
            t.sleep(2)
    if choice==2:
        if i==1:
            x=input("Enter the USERNAME\n") 
            y=gp.getpass(("Enter the PASSWORD\n"))
            username.verification(x,y)
            i=0
        elif(i==2):
            clear()
            print("Please sign up to continue.\n")
            t.sleep(2)
        else:
            clear()
            print("log-out to continue\n")
            t.sleep(2)
    if choice==3:
        if i ==0:
            i=1
            clear()
            print("You have logged out successfully")
            t.sleep(2)

        else:
            clear()
            print("You have not logged-in\n") 
            t.sleep(2)
clear()
