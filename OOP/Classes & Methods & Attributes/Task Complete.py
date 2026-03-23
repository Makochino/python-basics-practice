class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True
        print(f"Task ({self.title}) completed :-) ")


task1 = Task("Write shop list")
task2 = Task("Make shoping")
task3 = Task("Go to home after all")
task_list = [task1, task2, task3]
task1.mark_done()
task2.mark_done()
for t in task_list:
    print(f"{t.title} -> {'Done' if t.completed else 'Pending'}")