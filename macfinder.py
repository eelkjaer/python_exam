from modules import eksamen_scrape
from modules import eksamen_table
from modules import eksamen_plot
from modules import eksamen_csv
from modules import eksamen_cluster
from modules import eksamen_class
from modules import eksamen_normalize
from modules import eksamen_linear_regression
from modules import eksamen_machine_learning

def scrape_computersalg(searchPhrase, isMac):
    # Scrape Computersalg.dk
    page_source = eksamen_scrape.computersalg_scrape(searchPhrase)
    
    # Get all tag elements
    all_tag_elements = eksamen_scrape.find_elements_computersalg(page_source)
    
    # Extract data of search and csv file
    all_search_dict_result, all_computer_to_add_to_csv = eksamen_scrape.extract_information_from_all_tags_computersalg(all_tag_elements)
    
    # Sort search dict
    sorted_all_search_dict_result_by_price = eksamen_scrape.sorted_all_search_dict_result_by_price(all_search_dict_result)

    if len(all_search_dict_result) > 3:
        # Get low, mid and high result 
        result = eksamen_scrape.get_low_mid_high_search_dict_result(sorted_all_search_dict_result_by_price)
        
    else:
        result = all_search_dict_result
    
    if isMac:
        # append result to csv file
        eksamen_csv.import_computer_data_to_csv_file(all_computer_to_add_to_csv)
    
    return result

def scrape_foniks(searchPhrase, isMac):
    # Scrape Føniks
    page_source = eksamen_scrape.foniks_scrape(searchPhrase)
    
    # Get all tag elements
    all_tag_elements = eksamen_scrape.find_elements_foniks(page_source)
    
    # Extract data of search and csv file
    all_search_dict_result, all_computer_to_add_to_csv = eksamen_scrape.extract_information_from_all_tags_foniks(all_tag_elements)
    
    # Sort search dict
    sorted_all_search_dict_result_by_price = eksamen_scrape.sorted_all_search_dict_result_by_price(all_search_dict_result)

    if len(all_search_dict_result) > 3:
        # Get low, mid and high result 
        result = eksamen_scrape.get_low_mid_high_search_dict_result(sorted_all_search_dict_result_by_price)
        
    else:
        result = all_search_dict_result
    
    if isMac:
        # append result to csv file
        eksamen_csv.import_computer_data_to_csv_file(all_computer_to_add_to_csv)
    
    return result

def start_scrape():
    
    # User input
    searchPhrase, computer_to_find, price_range, isMac = eksamen_scrape.search_input()
    
    print(searchPhrase)
    
    scrape_result_1 = scrape_foniks(searchPhrase, isMac)
    
    scrape_result_2 = scrape_computersalg(searchPhrase, isMac)
        
    result = eksamen_scrape.merge_scrape_results(scrape_result_1, scrape_result_2)
    
    #eksamen_table.show_result_table(result)
    
    #eksamen_plot.plot_result(result)

    eksamen_machine_learning.execute_machine_learning('eksamen', 'eksamen_computer_to_find', 2000, 'SVM')
    
    if isMac:
        # Save computer_to_find
        eksamen_csv.create_csv_file('eksamen_computer_to_find')

        eksamen_csv.append_to_csv_file(computer_to_find, 'eksamen_computer_to_find', 'w')
    



if __name__ == "__main__":
    start_scrape()
