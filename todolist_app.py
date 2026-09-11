class Task:
	def __init__(self,name):
		self.name=name
		self.done=False
tasks=[]
while True:
	print("1) Add Task")
	print("2)Exit")
	print("3)View Tasks")
	print("4)Mark as done")
	print("5)Delete task")
	print("6)Save & Exit")
	choice =input("Enter your choice :")
	if choice=="1":
		task_name=input("Enter your Task:")
		task1=Task(task_name)
		tasks.append(task1)
	if choice=="2":
		print("Exit")
		break
	if choice=="3":
		for index,i in enumerate(tasks):
			print(index+1,i.name)
			if i.done==True:
				print("Done")
			else:
				print("Not Done")
	if choice=="4":
		mark=input("Enter your task number:")
		mark=int(mark)
		selected_task=tasks[mark-1]
		selected_task.done=True
	if choice=="5":
		delete=input("Enter task number:")
		delete=int(delete)
		del tasks[delete-1]
		print("Deleted")
	if choice=="6":
		f = open("tasks.txt", "w")
		for i in tasks:
			f.write(i.name + "\n")
		f.close()
		break