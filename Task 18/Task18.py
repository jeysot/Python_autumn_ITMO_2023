class Teacher:
    def __init__(self, name):
        self.name = name

    def assign_task(self, pupil, task):
        pupil.receive_task(task)

    def check_task(self, pupil, task):
        task.solve_task()
        pupil.receive_feedback(task)


class Pupil:
    def __init__(self, name):
        self.name = name
        self.task = None

    def receive_task(self, task):
        self.task = task

    def solve_task(self):
        if self.task:
            self.task.solve_task()

    def receive_feedback(self, task):
        print(f"Ученик {self.name} получил обратную связь по задаче: {task.task_description} - {task.status}")



class Task:
    def __init__(self, task_description):
        self.task_description = task_description
        self.status = "Нерешенная"

    def solve_task(self):
        self.status = "Решенная"


teacher = Teacher("Преподаватель")
pupil1 = Pupil("Ученик 1")
pupil2 = Pupil("Ученик 2")


task_description = "Напишите программу FizzBuzz"
task = Task(task_description)


teacher.assign_task(pupil1, task)
teacher.assign_task(pupil2, task)


pupil1.solve_task()
pupil2.solve_task()


teacher.check_task(pupil1, task)
teacher.check_task(pupil2, task)
