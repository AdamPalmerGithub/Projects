task_lst = []

class TaskManager:
    

    def __init__(self, subject, contact, description, status):
    
        self.subject = subject
        self.contact = contact
        self.description = description
        self.status = status


    def close_task(self):
        self.status = "closed"


    def view_tasks(self):
        for i, task_manager in enumerate(task_lst):
            print(f"Task {i}: ID = {task_manager.task_id} This task is about {task_manager.subject}.")


    def add_task(task_id, subject, contact, status):
        task_lst.append(TaskManager(task_id, subject, contact, status))
        return task_lst

TaskManager.add_task(1, "Friday meeting", "John Doe", "pending")



# task_manager_instance = TaskManager(0, "", "", "")
# task_manager_instance.view_tasks()


def list_tasks():
    for i, tasks in enumerate(task_lst):
        print(f"Task {i}:  {task.subject} {task.contact} {task.status}")

def read_task(x):
    i = task_lst[x]
    print(f"{i.task_id} {i.description}")

# def create_task(a, b, c):
#     a = input("Enter task subject")
#     b = input("Enter the contact name")
#     c = input("Enter a description")

def update_task(i):
    for task in task_lst:
        if task.task_id == i:
            

            



task_lst.append(TaskManager(a, b, c))




while True:
    j = int(input("Choose an option from the following: \n1. view tasks\n2. create a task\n3. update a task\n4. delete a task\n5. logout"))

    if j == 1:
        list_tasks()
        read_task(int(input("Please input a number to see the task.")))

    elif j == 2:
        
