##This is the main script.
import scripts.functions

import time

def main():
    #Loading all page data
    
    #EVERYTHING PAST THIS POINT IS JUST TEST/EXAMPLE CODE:
    if scripts.functions.file_search("data.json") == False:
        print("Requesting Pages")
        page_data = scripts.functions.request_all_pages()
        print("Requested Pages")
        time.sleep(4)
        scripts.functions.save_as_json(page_data, "data.json")
        print("Saving Data To Json")

    else:
        page_data = scripts.functions.read_from_json("data.json")

    
    scripts.functions.parse_all_page_data(page_data)

    scripts.functions.save_as_json(scripts.functions.data_set, "formatted_data.json")

    item_data_formatted = scripts.functions.format_flip_data()


    margin_avarage = 0

    for item in item_data_formatted:
        margin_avarage += item_data_formatted[item]["margins"]
    
    margin_avarage = margin_avarage/len(item_data_formatted)

    for item in item_data_formatted:
        print(f"\033[1;37;40m{item}\033[0;37;40m")

        if item_data_formatted[item]['margins'] > margin_avarage:
            print(f"\033[1;34;40mMargins: {item_data_formatted[item]['margins']}\n")

        else:
            print(f"\033[1;31;40mMargins: {item_data_formatted[item]['margins']}\n")


if __name__ == "__main__":
    main()
