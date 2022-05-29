from abc import ABC, abstractmethod
from manager import Manager


class BaseClass(ABC):
    id = 0  # unique id for objects
    object_list = None  # object_list for store objects
    manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.store(self)  # for store object in object_list
        self.set_manager()
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)

    @classmethod
    def store(cls, _object):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(_object)

