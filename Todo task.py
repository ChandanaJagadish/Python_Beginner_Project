import sys
tasks=[]
while True:
    print("Enter your choice\n")
    print("1.Add new task\n 2.Remove existing task\n 3.Print the current tasks\n 4.Quit\n")
    option=int(input("Enter your choice\n"))
    if option==1:
       n=int(input("Enter the number of tasks you want to enter\n"))
       for i in range(n):
        add=input(f"Enter task{i+1}:()")
        tasks.append(add)
    elif option==2:
      if not tasks:
        print("No tasks available")
      else:
         for i,task in enumerate(tasks):
            print(f"{i+1} .{task}")
         removed_task=int(input("Enter the task number to be removed\n"))
         if 1<=removed_task<=len(tasks):
            tasks.pop(removed_task-1)
    elif option==3:
      if not tasks:
        print("Tasks not available\n")
      else:
        for i,task in enumerate(tasks):
            print(f"{i+1}. {task}")
    elif option==4:
      sys.exit()
    else:
      print("Invalid option")