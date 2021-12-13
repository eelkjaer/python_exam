from modules import eksamen_class
from modules import eksamen_csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
import bs4
import json
import re
import operator


def search_input():
    brand = ''
    cpu = ''
    processor = ''
    ram = ''
    ssd = ''
    screen = ''
    price_range = ''
    url = ''
    ssd_size = ''
    screen_size = ''
    isMac = False

    # brand = input('Computer brand: ')
    model = input('Model: ')
    # cpu = input('Cpu manufacture: ')
    # processor = input('Processor: ')
    while type(ram) is not int:
        try:
            ram = int(input('Number of Ram: '))
        except ValueError as e:
            print('Please write a whole number...')
    while type(ssd) is not int:
        try:
            ssd = int(input('Size of SSD: '))
        except ValueError as e:
            print('Please write a whole number...')
    while type(screen) is not int:
        try:
            screen = int(input('Screen size: '))
        except ValueError as e:
            print('Please write a whole number...')
    while type(price_range) is not float:
        try:
            price_range = float(input('Target price: '))
        except ValueError as e:
            print('Please write a number...')

    if ssd < 10:
        ssd_size = ' TB'
    else:
        ssd_size = ' GB'

    # if screen == 13:
    #    screen_size = '13.3"'
    # elif screen == 14:
    #    screen_size = '14.2"'
    # elif screen == 15:
    #    screen_size = '15.4"'
    # elif screen == 16:
    #    screen_size = '16.2"'

    if 'mac' in model.lower():
        isMac = True
        cpu = 'Apple M1'
        brand = 'Apple'

        if screen == 14 and (64 > ram > 16):
            processor = 'M1 Max'
        elif screen == 14 and ram == 64:
            processor = 'M1 Pro'
        elif screen == 16 and 32 > ram:
            processor = 'M1 Max'
        elif screen == 16 and ram >= 32:
            processor = 'M1 Pro'
        else:
            processor = 'M1 M1'

    # query = brand + ' ' + model + ' ' + cpu + ' ' + processor + ' ' + str(ram) + ' GB ' + str(ssd) + ssd_size + screen_size
    searchPhrase = model + ' ' + str(screen) + ' ' + str(ram) + ' GB ' + str(ssd) + ssd_size

    computer_to_find = eksamen_class.Computer(model, screen, ram, ssd, price_range, url, brand, cpu, processor)

    return (searchPhrase, computer_to_find, price_range, isMac)

def foniks_interaction(searchPhrase):
    #print(searchPhrase)
    url = 'https://www.fcomputer.dk/search?q='
    search_tokens = searchPhrase.split(' ')
    for token in search_tokens:
        url = url + str(token) + '%20'

    #print(url)

    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override",
                           "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")

    # headless is needed here because we do not have a GUI version of firefox
    options = Options()
    options.headless = True
    # driver = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')
    browser = webdriver.Firefox(options=options)

    # browser = webdriver.Firefox()
    browser.get(url)
    browser.implicitly_wait(3)
    # button = browser.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection"]')
    # button.click()

    # Search field
    # search_field = browser.find_element_by_xpath('//*[@id="search-query"]')
    # print(search_field)

    # sleep(3)

    # search_field.send_keys(searchPhrase)

    # sleep(3)
    # browser.implicitly_wait(3)

    # search_field.submit()

    sleep(5)

    return browser.page_source


def foniks_scrape(searchPhrase):
    url = 'https://www.fcomputer.dk/search?q='
    search_tokens = searchPhrase.split(' ')
    for token in search_tokens:
        url = url + str(token) + '%20'

    result = requests.get(url)

    page_source = result.text

    return page_source


def find_elements_foniks(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    # print(soup)
    elements = soup.select(
        'div[class="query-product-wrapper phone-1-50 phone-2-50 phone-3-50 tablet-1-25 tablet-2-25 desktop-0-25 desktop-1-20 desktop-2-20 desktop-3-20 desktop-4-20"]')
    # event_cells = soup.select(selector)
    # return event_cells
    return elements


def extract_link_foniks(page_tag):
    soup = bs4.BeautifulSoup(page_tag, 'html.parser')
    link_data = soup.select('a')
    link_url = link_data[0]['href']
    link = 'https://www.fcomputer.dk' + '/' + link_url
    return link


def extract_title_foniks(page_tag):
    soup = bs4.BeautifulSoup(page_tag, 'html.parser')
    title_data = soup.select('span[class="title"]')
    title = title_data[0].getText()
    return title


def extract_price_foniks(page_tag):
    soup = bs4.BeautifulSoup(page_tag, 'html.parser')
    price_data = soup.select('div[class="product-price"]')
    price_text = price_data[0].getText()
    price_no_space = re.sub(r"[\n\t\s]*", "", price_text)
    price_clean = price_no_space.strip("-DKK")
    price_string = ''
    for letter in price_clean:
        if letter.isdigit():
            price_string = price_string + letter
        elif letter == '.':
            continue
        elif letter == ',':
            price_string = price_string + '.'
    price = float(price_string)
    return price


def merge_scrape_results(scrape_result_1=[], scrape_result_2=[]):
    scrape_result = []

    if len(scrape_result_1) > 0:
        for result in scrape_result_1:
            scrape_result.append(result)

    if len(scrape_result_2) > 0:
        for result in scrape_result_2:
            scrape_result.append(result)

    return sorted(scrape_result, key=lambda x: x['price'])


def extract_data_from_element_foniks(page_tag):
    link = extract_link_foniks(page_tag)
    title = extract_title_foniks(page_tag)
    price = extract_price_foniks(page_tag)
    computer_to_add_to_csv = eksamen_csv.create_csv_data(link, title, price)
    return ({"Link": link, "title": title, "price": price}, computer_to_add_to_csv)


def extract_information_from_all_tags_foniks(all_tag_elements):
    all_search_dict_result = []
    all_computer_to_add_to_csv = []

    for element in all_tag_elements:
        search_dict_result, computer_to_add_to_csv = extract_data_from_element_foniks(str(element))
        all_search_dict_result.append(search_dict_result)
        all_computer_to_add_to_csv.append(computer_to_add_to_csv)

    return all_search_dict_result, all_computer_to_add_to_csv


def sorted_all_search_dict_result_by_price(all_search_dict_result):
    return sorted(all_search_dict_result, key=lambda x: x['price'])


def get_low_mid_high_search_dict_result(sorted_all_search_dict_result_by_price):
    return [sorted_all_search_dict_result_by_price[0], sorted_all_search_dict_result_by_price[int(len(sorted_all_search_dict_result_by_price) / 2) + 1], sorted_all_search_dict_result_by_price[len(sorted_all_search_dict_result_by_price) - 1]]


#def sorted_all_computer_to_add_to_csv_by_price_foniks(all_computer_to_add_to_csv):
#    return sorted(all_computer_to_add_to_csv, key=operator.attrgetter('price'))

def computersalg_scrape(search_phrase):
    url = 'https://www.computersalg.dk/l/0/s?sq='
    search_tokens = search_phrase.split(' ')
    for token in search_tokens:
        url = url + str(token) + '+'

    result = requests.get(url)

    page_source = result.text

    return page_source

def find_elements_computersalg(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    return soup.select('li[class="tool-list-product productlist-item"]')

def extract_link_computersalg(page_tag):
    soup = bs4.BeautifulSoup(page_tag, 'html.parser')
    link_data = soup.select('a')
    link_url = link_data[0]['href']
    link = 'https://www.computersalg.dk' + '/' + link_url
    return link

def extract_title_computersalg(page_tag):
    soup = bs4.BeautifulSoup(page_tag, 'html.parser')
    #response-target > ul > li:nth-child(1) > div > div.productContent > div.productText > h3 > a
    title_data = soup.select('a[class="itemclikevent productNameLink"]')
    #print(title_data)
    title = title_data[0].getText()
    return title


def extract_price_computersalg(page_tag):
    soup = bs4.BeautifulSoup(page_tag, 'html.parser')
    price_data = soup.select('div[class="productPrice"] span')
    price_text = price_data[0].text
    price_no_space = re.sub(r"[\n\t\s]*", "", price_text)
    price_clean = price_no_space.strip("-DKK")
    price_string = ''
    for letter in price_clean:
        if letter.isdigit():
            price_string = price_string + letter
        elif letter == '.':
            continue
        elif letter == ',':
            price_string = price_string + '.'
    price = float(price_string)
    return price

def extract_data_from_element_computersalg(page_tag):
    link = extract_link_computersalg(page_tag)
    title = extract_title_computersalg(page_tag)
    price = extract_price_computersalg(page_tag)
    if price < 6000:
        return None, None
    computer_to_add_to_csv = eksamen_csv.create_csv_data_cs(link, title, price)
    #print(computer_to_add_to_csv)
    return ({"Link": link, "title": title, "price": price}, computer_to_add_to_csv)

def extract_information_from_all_tags_computersalg(all_tag_elements):
    all_search_dict_result = []
    all_computer_to_add_to_csv = []

    for element in all_tag_elements:
        search_dict_result, computer_to_add_to_csv = extract_data_from_element_computersalg(str(element))
        if search_dict_result is None or computer_to_add_to_csv is None:
            continue
        all_search_dict_result.append(search_dict_result)
        all_computer_to_add_to_csv.append(computer_to_add_to_csv)

    return all_search_dict_result, all_computer_to_add_to_csv
