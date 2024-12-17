# Native python libraries

# Third party libraries

# Self build libraries
from Constants.Constants import ENGLISH_WEEKEND


class Responsible:
    def __init__(
        self,
        firstName: str,
        lastName: str,
        workHours: int,
        workDays: list[str] = ENGLISH_WEEKEND,
    ):
        self.firstName = firstName
        self.lastName = lastName
        self.fullname = self.firstName + "" + self.lastName
        self.workHours = workHours
        self.workDays = workDays
        pass

    def __str__(self):
        return f"First Name: {self.firstName}\nLast Name: {self.lastName}\nFullname: {self.fullname}"

    pass
