import requests
from bs4 import BeautifulSoup


class OtodomParser:
    def __init__(self, address_string, last_page_number=1, file_name="offers.csv"):
        if type(address_string) is not str:
            raise Exception("Address string can't be empty or not str type.")

        self.actual_page = 1
        self.last_page_number = last_page_number
        self.address_string = '{0}&page={1}'.format(address_string, "{}")
        self.file_name = file_name

    @staticmethod
    def remove_blank_strings(l):
        return [e for e in l if e and str(e).strip()]

    @staticmethod
    def remove_unnecessary_elements(_offer):
        result = []
        for el in _offer:
            new_el = el.strip()

            if el.startswith('Działka na sprzedaż: '):
                new_el = el.replace('Działka na sprzedaż: ', '')

            result.append(new_el)
        return result

    @staticmethod
    def prepare_list_from_offer(_offer):
        return list(_offer.children)[3].text.split('\n')

    def parse(self):
        result_list = ["Opis;Miejsce;Cena;Powierzchnia;Cena za m2;Link do ogloszenia"]
        r = requests.get(self.address_string.format(self.actual_page))

        while self.actual_page <= self.last_page_number:
            print("Parsing page {}".format(self.actual_page))
            soup = BeautifulSoup(r.content, 'html.parser')
            offers = soup.find_all('article')

            for offer in offers:
                offer_as_list = self.prepare_list_from_offer(offer)
                offer_as_list = self.remove_blank_strings(offer_as_list)
                offer_as_list = self.remove_unnecessary_elements(offer_as_list)
                offer_as_list.append(offer.find('a').attrs['href'])
                result_list.append(';'.join(offer_as_list[1:]))

            self.actual_page += 1
            r = requests.get(self.address_string.format(self.actual_page))

        with open(self.file_name, 'w') as file:
            for el in result_list:
                file.write("{}\n".format(el))
