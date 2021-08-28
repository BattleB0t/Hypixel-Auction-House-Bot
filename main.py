##This is the main script.
import scripts.functions

def main():
    #Loading all page data
    
    #page_data = scripts.functions.request_all_pages()
    
    #Saving all page data to a json file
    
    #scripts.functions.save_as_json(page_data, "data.json")


    page_data = scripts.functions.read_from_json("data.json")

    scripts.functions.parse_all_page_data(page_data)

if __name__ == "__main__":
    main()
