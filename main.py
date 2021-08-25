##This is the main script.
import scripts.functions
import scripts.console_graphics

def main():
    #Loading all page data
    page_data = scripts.functions.request_all_pages()
    
    #Saving all page data to a json file
    scripts.functions.save_as_json(page_data, "data.json")

if __name__ == "__main__":
    main()
