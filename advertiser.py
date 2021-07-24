from base_model import BaseAdvertising


class AdvertiserManager:
    __instance = None
    __advertisers = []

    @staticmethod
    def get_instance():
        if AdvertiserManager.__instance == None:
            AdvertiserManager()
        return AdvertiserManager.__instance
    
    def __init__(self):
        if AdvertiserManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AdvertiserManager.__instance = self

    def add_advertiser(self, ad):
        self.__advertisers.append(ad)
    
    def check_id_for_unique(self, id):
        if all(x.get_id() != id for x in self.__advertisers):
            return id
        raise Exception("This id is not unique")

    @classmethod
    def get_total_clicks(cls):
        return sum(adv.get_views() for adv in cls.__advertisers)

class Advertiser(BaseAdvertising):

    def __init__(self, id: int, name: str):
        self.__manager = AdvertiserManager.get_instance()
        super().__init__(self.__manager.check_id_for_unique(id))
        self.__name: str = name
        self.__manager.add_advertiser(self)


    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    @classmethod
    def help(cls):
        help = 'This is Advertiser class, it has some peroperties: id, name, clicks, views.' \
               'The Id fields is unique and the clicks is equal to numbers of clicks on this advertiser' \
               'and the views is equal to number of times this advertiser have been seen'
        return help

    @classmethod
    def get_total_clicks(cls):
        return AdvertiserManager.get_total_clicks()

    def describe_me(self):
        return f'This is {self.__name} advertiser with {self.get_id()} identifier'
