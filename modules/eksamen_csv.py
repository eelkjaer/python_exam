from modules import eksamen_class
import csv
import pandas as pd
import re
import operator


def create_csv_file(filename):
    filename = filename + '.csv'
    file_to_output = open(filename, 'w', newline='')
    csv_writer = csv.writer(file_to_output, delimiter=',')
    csv_writer.writerow(['Brand', 'Model', 'Cpu', 'Processor', 'Ram', 'SSD (TB)', 'Screen', 'Price', 'Date', 'Url'])
    file_to_output.close()


def append_to_csv_file(computer_to_add, filename = 'eksamen', mode = 'a'):
    #print(computer_to_add)
    filename = filename + '.csv'
    file_to_output = open(filename, mode, newline='')
    csv_writer = csv.writer(file_to_output, delimiter=',')
    csv_writer.writerow([computer_to_add.brand, computer_to_add.model, computer_to_add.cpu, computer_to_add.processor,
                         computer_to_add.ram, computer_to_add.ssd, computer_to_add.screen, computer_to_add.price,
                         computer_to_add.date, computer_to_add.url])
    file_to_output.close()


def show_csv_head(filename = 'eksamen'):
    filename = filename + '.csv'
    computer_data = pd.read_csv(filename, decimal=',')
    return computer_data.head()


def return_csv_file_for_head_view(filename = 'eksamen'):
    filename = filename + '.csv'
    computer_data = pd.read_csv(filename, decimal=',')
    return computer_data


def create_csv_data_cs(link, title, price):
    computer_to_add_to_csv = None

    #print(title)

    #if str(title[0:5]).lower() == 'apple':
    if 'apple' in title.lower() and 'refurbished' not in title.lower():
        #print(title)
        if len(title.split(',')) > 2:
            return
        title_tokens = title.split(' - ')
        #print(title_tokens)
        brand_model_tokens = title_tokens[0].split(' ')
        #print(brand_model_tokens)
        brand = 'Apple'
        model = brand_model_tokens[1] + ' ' + brand_model_tokens[2]
        indices = [i for i, s in enumerate(title_tokens) if '"' in s]
        screen_str_indice = title_tokens[indices[0]]
        screen_str_pos = screen_str_indice.split('"')
        screen_str = screen_str_pos[0]
        screen_str = re.sub('[^\d\.]', '', screen_str)
        #print(screen_str)
        screen = int(float(screen_str))
        ram_tokens = title_tokens[3].split(' ')
        ram = int(ram_tokens[0])
        ssd_tokens = title_tokens[4].split(' ')
        ssd = int(ssd_tokens[0])
        cpu = 'Intel Core'

        if 'M1' or 'm1' in str(title_tokens[2]).lower():
            cpu = 'Apple M1'

        processor_tokens = title_tokens[2].split(' ')
        if cpu == 'Intel Core':
            processor = processor_tokens[len(processor_tokens) - 1]
        else:
            processor = 'M1 ' + processor_tokens[len(processor_tokens) - 1]

        computer_to_add_to_csv = eksamen_class.Computer(model, screen, ram, ssd, price, link, brand, cpu, processor)

    return computer_to_add_to_csv


def create_csv_data(link, title, price):
    computer_to_add_to_csv = None

    if str(title[0:5]).lower() == 'apple':
        title_tokens = title.split(' - ')
        brand_model_tokens = title_tokens[0].split(' ')
        brand = brand_model_tokens[0]
        model = brand_model_tokens[1] + ' ' + brand_model_tokens[2]
        screen = int(title_tokens[1][0:2])
        ram_tokens = title_tokens[3].split(' ')
        ram = int(ram_tokens[0])
        ssd_tokens = title_tokens[4].split(' ')
        ssd_value = int(ssd_tokens[0])
        ssd = 0
        if ssd_value < 500:
            ssd = 0.256
        if ssd_value == 500 or ssd_value == 512:
                ssd = 0.512
        if ssd_value == 1:
            ssd = 1
        if ssd_value == 2:
            ssd = 2
        if ssd_value == 4:
            ssd = 4
        if ssd_value == 8:
            ssd = 8
        cpu = 'Intel Core'

        if 'M1' or 'm1' in str(title_tokens[2]).lower():
            cpu = 'Apple M1'

        processor_tokens = title_tokens[2].split(' ')
        if cpu == 'Intel Core':
            processor = processor_tokens[len(processor_tokens) - 1]
        else:
            processor = 'M1 ' + processor_tokens[len(processor_tokens) - 1]

        computer_to_add_to_csv = eksamen_class.Computer(model, screen, ram, ssd, price, link, brand, cpu, processor)

    return computer_to_add_to_csv


def import_computer_data_to_csv_file(all_computer_to_add_to_csv):
    for computer in all_computer_to_add_to_csv:
        if computer is None:
            continue
        append_to_csv_file(computer, 'eksamen')


def read_csv(filename = 'eksamen_computer_to_find'):
    filename = filename + '.csv'

    # Open the file
    data = open(filename, encoding = 'utf-8')

    # csv.reader
    # You can seperate with ",", ";", "\t" etc. Look at the file and find the delimiter
    csv_data = csv.reader(data, delimiter = ',')

    # Reformat it into python list
    csv_data_list = list(csv_data)

    return csv_data_list
