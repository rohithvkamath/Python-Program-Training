# Program to append & delete the elements in a dummy list.

choice=-1
dummy_list=['apple','bun','car']
while choice!='3':
    choice=input("Enter your choice\n 1. Insert\n 2. Delete \n 3. Exit\n")
    if choice=='1':
        x=input("Enter the element you want to insert\t")
        dummy_list.append(x)
        print("\n\nNew list is\n:",dummy_list,"\n\n")
    if choice=='2':
        print(dummy_list)
        y=input("Enter the element you want to delete\t")
        dummy_list.remove(y)
        print("\n\nNew list is:\n",dummy_list,"\n\n")
    if(choice>'3'): 
        print("Choose the correct choice\n")
        