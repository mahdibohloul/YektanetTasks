from advertiser import BaseAdvertising, Advertiser



class AdManager:
    __instance = None
    __ads = []

    @staticmethod
    def get_instance():
        if AdManager.__instance == None:
            AdManager()
        return AdManager.__instance
    
    def __init__(self):
        if AdManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AdManager.__instance = self

    def add_ad(self, ad):
        self.__ads.append(ad)
    
    def check_id_for_unique(self, id):
        if all(x.get_id() != id for x in self.__ads):
            return id
        raise Exception("This id is not unique")


class Ad(BaseAdvertising):
    def __init__(self, id: int, title: str, img_url: str, link: str, advertiser: Advertiser) -> None:
        self.__manager = AdManager.get_instance()
        super().__init__(self.__manager.check_id_for_unique(id))
        self.__title = title
        self.__img_url = img_url
        self.__link = link
        self.__advertiser = advertiser
        self.__manager.add_ad(self)


    
    def get_title(self):
        return self.__title
    
    def set_title(self, title: str):
        self.__title = title
    
    def get_img_url(self):
        return self.__img_url
    
    def set_img_url(self, url: str):
        self.__img_url = url
    
    def get_link(self):
        return self.__link
    
    def set_link(self, link: str):
        self.__link = link
    
    def set_advertiser(self, advertiser: Advertiser):
        self.__advertiser = advertiser
        
    def describe_me(self):
        advertiser_name = self.__advertiser.get_name() if self.__advertiser is not None else 'No Advertiser'
        return f'This is {self.__title} Ad with {self.get_id()} identifier. My Advertiser is: {advertiser_name}'

    def inc_clicks(self):
        super().inc_clicks()
        self.__advertiser.inc_clicks()
    
    def inc_views(self):
        super().inc_views()
        self.__advertiser.inc_views()