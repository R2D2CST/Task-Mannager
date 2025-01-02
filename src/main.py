# Native python libraries
from datetime import datetime

# Third party libraries

# Self build libraries
from Constants.Constants import WEEKEND_DAYS, ENGLISH_WEEKEND
from Func.Human.Responsible import Responsible
from Func.Tasks.Task import Task

print(WEEKEND_DAYS)
print(ENGLISH_WEEKEND)

worker = Responsible("Arturo", "Castella")

dueDate = datetime(2025, 1, 15)

Task_1 = Task(
    description="New Task",
    responsible=worker,
    dueDate=dueDate,
    activity="Program a task manager",
)

print(dueDate)
print(worker)
print(Task_1)
