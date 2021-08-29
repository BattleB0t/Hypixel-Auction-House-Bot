##This is the main script.
import scripts.functions

from pprint import pprint

def main():
    #Loading all page data
    
    #page_data = scripts.functions.request_all_pages()
    
    #scripts.functions.save_as_json(page_data, "data.json")


    page_data = scripts.functions.read_from_json("data.json")

    scripts.functions.parse_all_page_data(page_data)

    scripts.functions.save_as_json(scripts.functions.data_set, "formatted_data.json")

    

    for page in scripts.functions.data_set:
        scripts.functions.get_two_lowest_values(page)
        
        

if __name__ == "__main__":
    main()
