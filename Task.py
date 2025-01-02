# Native python libraries
from datetime import datetime

# Third party libraries

# Self build libraries
from Func.Human.Responsible import Responsible


class Task:
    """
    Class describes the main elements for a task to been created.
    Attributes:

    """

    def __init__(
        self,
        description: str,
        responsible: Responsible,
        dueDate: datetime,
        activity: str,
        progress: int = 0,
    ):
        """
        Initializes class object creation
        Args:
            description (str): Brief task description or task name.
            responsible (Responsible): Person accountable/responsible for the task.
            dueDate (datetime): Due date for the task to be completed.
            activity (str): Actual activity.
            progress (int, optional): Activity progress. Defaults to 0.
        """
        # Set class attributes
        self.description = description
        self.responsible = responsible
        self.dueDate = dueDate
        self.activity = activity
        self.progress = progress

        # Validate valid entry's
        self.__validProgress__()
        pass

    def __str__(self):
        """
        Provides a string representation of the Task object.
        """
        return (
            f"Task Description: {self.description}\n"
            f"Responsible: {self.responsible}\n"
            f"Due Date: {self.dueDate.strftime('%Y-%m-%d')}\n"
            f"Activity: {self.activity}\n"
            f"Progress: {self.progress} %"
        )

    def __validProgress__(self):
        """
        Function validates if set attribute is a valid entry, raises Value Error instead.
        Raises:
            ValueError: Task attribute progress ({self.progress}) must be between 0 an 100 percent (%)
        """
        if not (0 <= self.progress <= 100):
            raise ValueError(
                f"Task attribute progress ({self.progress}) must be between 0 an 100 percent (%)"
            )

    def __validDatetime__(self):
        """
        Function validates if set datetime is a valid object datetime.
        Raises:
            ValueError: Datetime attribute dueDate ({self.dueDate}) must be a datetime object
        """
        if not isinstance(self.dueDate, datetime):
            raise ValueError(
                f"Datetime attribute dueDate ({self.dueDate}) must be a datetime object"
            )

    pass
