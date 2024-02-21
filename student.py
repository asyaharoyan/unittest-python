from datetime import date, timedelta
import requests

class Student:
    """
    A student class as base for method testing
    """
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def email(self):
        return f"{self.__first_name.lower()}.{self.__last_name.lower()}@email.com"


    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    def alert_santa(self):
        self.naughty_list = True

    
