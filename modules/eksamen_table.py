# coding=utf-8
from IPython.core.display import display, HTML


def convert_result_object(result_object):
    string = ''

    title = result_object['title'][:]
    price = str(result_object['price'])[:-2] + ' kr.'
    link = result_object['Link']

    string = f'<tr><td>{title}</td><td>{price}</td><td><a href="{link}">Gå til hjemmesiden</a></td></tr>'

    # print (string)

    return string


def create_result_table(sorted_result_list, function):
    table_data = '<table><tr><th>Title</th><th>Price</th><th>URL</th></tr>'

    map_data = map(function, sorted_result_list)
    string_from_map_data = ''.join(map_data)

    table_data = table_data + string_from_map_data + '</table>'

    return table_data


def show_result_table(result):
    table_data = create_result_table(result, convert_result_object)
    #print(table_data)
    display(HTML(table_data))