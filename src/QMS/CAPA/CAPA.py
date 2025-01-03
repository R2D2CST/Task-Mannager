# Native python libraries
from datetime import datetime

# Third party libraries

# Self build libraries
from Func.Human.Responsible import Responsible
from Func.Tasks.Task import Task


class CAPA(Task):
    """
    A Corrective Action, Preventive Action is a task where the QMS follows it's compromises.
    """

    def __init__(
        self,
        description: str,
        responsible: Responsible,
        dueDate: datetime,
        activity: str,
        systemOrigin: str,
        progress: int = 0,
    ):
        super().__init__(
            description=description,
            responsible=responsible,
            dueDate=dueDate,
            activity=activity,
            progress=progress,
        )
        self.systemOrigin = systemOrigin
        pass

    def __str__(self):
        return (
            super().__str__(),
            f"System Origin: {self.systemOrigin}",
        )

    pass
