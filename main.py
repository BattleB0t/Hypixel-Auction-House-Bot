#There is no controling code for this program yet as it is still being developed.
#Currently the code present is being used by me for testing.

def main():
    #This is only here to allow me to surf through the pages of data (because there is so much and for testing) so ignore it lol
    page_data = scripts.functions.request_all_pages()
    while True:
        try:
            print(page_data[input("Enter The Page You Would Like To View: ")])
        except:
            print("ERROR")

if __name__ == "__main__":
    main()
