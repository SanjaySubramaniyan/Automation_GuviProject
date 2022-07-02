from typing import List, Any
from bs4 import BeautifulSoup
import requests


class Sanjay:
    url = "https://www.zenclass.in/class"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'lxml')

    def sidebar(self):
        list: list[Any] = []

        for data in self.soup.findAll('div', class_='session-container'):
            list_ribbon = data.find('div', class_='preread-head')
            list.append(list_ribbon.text)

        print(list)
        print("-------------------------------------------------------------------")


s = Sanjay()

s.sidebar()
