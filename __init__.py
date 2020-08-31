from otodomParser import OtodomParser

if __name__ == '__main__':
    url = 'https://www.otodom.pl/sprzedaz/dzialka/krakow/?search%5Bfilter_float_price%3Ato%5D=260000&search%5Bregion_id%5D=6&search%5Bsubregion_id%5D=410&search%5Bcity_id%5D=38&search%5Bdistrict_id%5D=129&search%5Bdist%5D=5'

    parser = OtodomParser(url, 5)
    parser.parse()