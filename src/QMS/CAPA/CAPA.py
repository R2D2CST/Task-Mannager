# Native python libraries
from datetime import datetime

# Third party libraries

# Self build libraries
from Func.Human.Responsible import Responsible
from Func.Tasks.Task import Task
from Constants.Constants import QMS_SYSTEMS


class CAPA:
    """
    A Corrective Action, Preventive Action is a task where the QMS follows it's compromises.
    """

    def __init__(
        self,
        capaID: str,
        systemOrigin: str,
        responsible: Responsible,
        actionDescription: str,
        effectivityDescription: str,
        actionActivity: str,
        effectivityActivity: str,
        actionDueDate: datetime,
        effectivityDueDate: datetime,
        actionStartDate: datetime = False,
        effectivityStartDate: datetime = False,
        actionProgress: int = 0,
        effectivityProgress: int = 0,
        corrective: bool = True,
    ):

        # We validate our start date for each task
        if not actionStartDate:
            actionStartDate = actionDueDate
        if not effectivityStartDate:
            effectivityStartDate = effectivityDueDate

        # We generate our action plan task and our effectivity verification
        # As so for our class attributes
        self.actionTask = Task(
            description=actionDescription,
            responsible=responsible,
            dueDate=actionDueDate,
            activity=actionActivity,
            startDate=actionStartDate,
            progress=actionProgress,
        )
        self.effectivityTask = Task(
            description=effectivityDescription,
            responsible=responsible,
            dueDate=effectivityDueDate,
            activity=effectivityActivity,
            startDate=effectivityStartDate,
            progress=effectivityProgress,
        )
        self.corrective = corrective
        self.systemOrigin = systemOrigin
        self.capaID = capaID

        self.__systemValidation__()

        pass

        def __str__(self):
            return (
                f"CAPA ID: {self.capaID}\n",
                f"CAPA Status: {self.capaStatus}\n",
                f"CAPA Responsible: {self.action.responsible}\n",
                f"CAPA Origin: {self.systemOrigin}\n",
                f"Corrective CAPA: {self.corrective}\n",
                f"Action Tasks:\n",
                f" -: {self.actionTask.description}\n",
                f" -: {self.actionTask.startDate.strftime('%Y-%m-%d')}\n",
                f" -: {self.actionTask.dueDate.strftime('%Y-%m-%d')}\n",
                f" -: {self.actionTask.activity}\n",
                f" -: {self.actionTask.progress}\n",
                f"Effectivity Task:\n",
                f" -: {self.effectivityTask.description}\n",
                f" -: {self.effectivityTask.startDate.strftime('%Y-%m-%d')}\n",
                f" -: {self.effectivityTask.dueDate.strftime('%Y-%m-%d')}\n",
                f" -: {self.effectivityTask.activity}\n",
                f" -: {self.effectivityTask.progress}\n",
            )

        def __systemValidation__(self):
            if not self.systemOrigin in QMS_SYSTEMS:
                raise ValueError(
                    f"System Origin ({self.systemOrigin}) mus be within {QMS_SYSTEMS}"
                )
            pass

        def __capaStatusValidation__(self):
            if self.actionTask.progress == 100 and self.effectivityTask.progress == 100:
                self.capaStatus = "Closed"
            else:
                self.capaStatus = "Open"
            pass

    pass
