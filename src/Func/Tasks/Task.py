# Native python libraries
from datetime import datetime

# Third party libraries

# Self build libraries
from Func.Human.Responsible import Responsible


class Task:

    def __init__(
        self,
        description: str,
        responsible: Responsible,
        dueDate: datetime,
        progress: int = 0,
    ):
        self.description = description
        self.responsible = responsible
        self.dueDate = dueDate
        self.progress = progress
        pass

    pass
