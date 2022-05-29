from base import BaseClass


class User(BaseClass):
    def __init__(self, first_name, last_name, phone_number, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        super().__init__(*args, **kwargs)  # from parent class

    @property  # create a readonly field for class
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
