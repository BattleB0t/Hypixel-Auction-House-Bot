class parse:
    def __init__(self, ah_data_obj):
        self.ah_data_obj = ah_data_obj
        self.ah_page_quantity = ah_data_obj.number_of_pages

        self.item_set = {}

    #This may take some time-
    def parse(self):
        for page in range(self.ah_page_quantity):
            current_page_data = self.ah_data_obj.data[f"page{page}"]

            if current_page_data["success"] == True:
                
                for item in current_page_data["auctions"]:

                    pass

            else: #If this is called it means that the page you want to parse wasnt installed successsfully.
                continue
