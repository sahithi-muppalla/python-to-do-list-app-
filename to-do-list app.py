print("~~~TO-DO-LIST~~~")
tasks=["1.Learning a best language according to you","2.Understand with day-to-day examples","3.Clear doubts","4.Learn from mistakes","5.Build projects"]
while True:
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Display")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        task=input("Enter the task you want to add: ")
        tasks.append(task)
        print("Added successfully!")
    elif choice==2:
        if len(tasks)==0:
            print("No tasks are in list")
        else:
            num=int(input("Enter task number to remove: "))
            tasks.pop(num-1)
            print("Removed successfully!")
        
    elif choice==3:
        if len(tasks)==0:
            print("No tasks available")
        else:
            print("\nYour tasks are: ")
            for task in tasks:
                print(task)
    elif choice==4:
        print("Thank you for using To-Do-List Application")
        break
    else:
        print("Invalid choice!. Try again ")

        
