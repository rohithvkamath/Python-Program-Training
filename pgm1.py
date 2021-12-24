# Program to append & delete the elements in the list.

str=[]
ch=-1
while ch!=0:
    print("Enter your choice:\n 1.Insert\n 2.Delete\n 0.Exit\n")
    ch=int( input())
    if ch==1:
        n=input("Enter the element you want to insert in the list\n")
        str.append(n)
        print(str)
    if ch==2:
        m=input("Enter the position of the element to be deleted")
        str.remove(m)
        print(str)