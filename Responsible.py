# Native python libraries

# Third party libraries

# Self build libraries
from Constants.Constants import ENGLISH_WEEKEND, WEEKEND_DAYS


class Responsible:
    def __init__(
        self,
        firstName: str,
        lastName: str,
        workHours: int = 8,
        workDays: list[str] = ENGLISH_WEEKEND,
    ):
        """
        Initializes our class worker or accountable for a task.
        Args:
            firstName (str): Responsible fist name
            lastName (str): Responsible last name
            workHours (int): Daily working hours
            workDays (list[str], optional): Working days by the weekend. Defaults to ENGLISH_WEEKEND.
        """
        # We set our class attributes.
        self.firstName = firstName
        self.lastName = lastName
        self.fullname = self.firstName + "" + self.lastName
        self.workHours = workHours
        self.workDays = ENGLISH_WEEKEND

        # We validate our attributes are correct
        self.__validateWorkDays__()
        pass

    def __str__(self):
        """
        Provides a string representation of the Responsible object.
        """
        return (
            f"Fullname: {self.fullname}\n"
            f"First Name: {self.firstName}\n"
            f"Last Name: {self.lastName}\n"
            f"Work Hours: {self.workHours}\n"
            f"Work Days: {self.workDays}\n"
        )

    def __validateWorkDays__(self):
        """
        Validates if the given working days are valid days in the weekend.

        Raises:
            ValueError: Invalid weekend days ({invalidDays}), weekend days must be within ({WEEKEND_DAYS}).
        """
        invalidDays = [day for day in self.workDays if day.lower() not in WEEKEND_DAYS]
        if invalidDays:
            raise ValueError(
                f"Invalid work days: {invalidDays}. "
                f"Work days must be within: {WEEKEND_DAYS}."
            )

    pass
