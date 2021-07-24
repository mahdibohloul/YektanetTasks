from abc import ABC, abstractmethod


class BaseAdvertising(ABC):
    def __init__(self, id) -> None:
        self.__id = id
        self.__views = 0
        self.__clicks = 0
    
    @abstractmethod
    def describe_me(self):
        pass

    def get_clicks(self):
        return self.__clicks

    def get_views(self):
        return self.__views

    def inc_clicks(self):
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1

    def get_id(self):
        return self.__id
