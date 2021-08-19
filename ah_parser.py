class parse:
    def __init__(self, ah_data_obj):
        self.ah_data_obj = ah_data_obj
        self.ah_page_quantity = ah_data_obj.number_of_pages
        self.sorted_by_type = False
        
        self.item_set = {}

    #This may take some time-
    def sort_into_type(self):
        for page in range(self.ah_page_quantity):
            current_page_data = self.ah_data_obj.data[f"page{page}"]

            if current_page_data["success"] == True:
                
                for item in current_page_data["auctions"]:

                    #Creates a list of this type of item in the set of data.
                    if item["item_name"] not in self.item_set:

                        self.item_set[item["item_name"]] = [item]

                    #Appends to a previously created list.
                    else:
                        self.item_set[item["item_name"]].append(item)

            else: #If this is called it means that the page you want to parse wasnt installed successsfully.
                continue

            self.sorted_by_type = True

    def search_by_name(self, item_name): ##The item_name needs to be **PRECISE** like to the word.
        if self.sorted_by_type == True:
            try:
                return self.item_set[item_name]
            except:
                return "item not found"
        else:
            print("You have to sort by type before running this function.")
