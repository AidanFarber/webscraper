# Function for removing entries
# Function for adding entries
# Function for checking entries
# function for menu

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from time import sleep
import os

def main():
    # File definitions
    settingsFile = "settings.txt"
    productFile = 'products.csv'

    mode = 0
    try:
        with open(settingsFile, "r") as settings:
            # Reading of settings from file
            for line in settings:
                if "mode=" in line:
                    mode = line[6]
    except:
        # create settings file because it doesn't exist
        with open(settingsFile, "x") as settings:
            settings.write("mode=1") # Set the mode to 1; allows menu
            mode = 1
    
    if mode != 0:
        selection(productFile) # Display the menu
    else:
        checkEntries(productFile) # Auto check entries; to display menu again change settings file
    

# Entry Menu
def selection(productFile):
    # Menu to either add an entry, remove an entry, or continue through to check existing entries
    print('Welcome to the price tracker\n')

    selection = 'invalid'
    while selection != '4':
        print("Please select an option from the following:\n"
            "\t1. Update existing entries\n"
            "\t2. Add a new entry\n"
            "\t3. Delete an entry\n"
            "\t4. Exit")
        selection = input()

        if selection == '1':
            checkEntries(productFile)
        elif selection == '2':
            addEntry()
        elif selection == '3':
            removeEntries()
        elif selection == '4':
            pass
        else:
            print(f'Your selection of \'{selection}\' is invalid, please try again')

# Check existing entries
def checkEntries( productFile ):

    sleepTime = 1800000 # time (in milliseconds) before each entry check, 1800000 = 30mins
    with open(productFile, "r") as products:
        for x in products:
            seperated = x.split(',')
            link = seperated[3]
            if 'amazon.com' in link:
                # Open connection, grab HTML
                siteConnection = uReq(link)
                pageHTML = siteConnection.read()
                siteConnection.close()

                # Parse HTML
                parsedData = soup(pageHTML, 'html.parser')

                # if a search result is given, not an individual product
                if 's?k=' in link:
                    print("Search")

                # else it is a single product
                else:
                    print('Individual')
                print('amazon')

            # Ebay
            elif 'ebay.com' in link:
                # Open connection, grab HTML
                siteConnection = uReq(link)
                pageHTML = siteConnection.read()
                siteConnection.close()
                
                # Parse HTML
                parsedData = soup(pageHTML, 'html.parser')

                # if a search result is given, not an individual product
                if 'sch' in link:
                    print("Search")

                # else it is a single product
                else:
                    print("Individual")

                print('ebay')

            # Newegg
            elif 'newegg.com' in link:
                # Open connection, grab HTML
                siteConnection = uReq(link)
                pageHTML = siteConnection.read()
                siteConnection.close()

                # Parse HTML
                parsedData = soup(pageHTML, 'html.parser')

                # if a search result is given, not an individual product
                if 'Category' in link or 'pl?d=':
                    print("Search")

                # else it is a single product
                else:
                    print("Individual")

                print('newegg')

            # Walmart
            elif 'walmart.com' in link:
                # Open connection, grab HTML
                siteConnection = uReq(link)
                pageHTML = siteConnection.read()
                siteConnection.close()

                # Parse HTML
                parsedData = soup(pageHTML, 'html.parser')

                # if a search result is given, not an individual product
                if 'search' in link:
                    pass

                # else it is a single product
                else:
                    pass

                print('walmart')

            else:
                print('Entry not valid')

# Removing an entry
def removeEntries():
    pass

# Adding a site
def addEntry():
    # Ask for user to input a site to read from
    print('Please enter the link to the product to track: ')
    siteURL = input()
    # Decide which site it is from
    # Amazon
    if 'amazon.com' in siteURL:
        print('amazon')

    # Ebay
    elif 'ebay.com' in siteURL:
        print('ebay')

    # Newegg
    elif 'newegg.com' in siteURL:
        print('newegg')

    # Walmart
    elif 'walmart.com' in siteURL:
        print('walmart')

    else:
        print('Invalid entry')

def writeToCSV( item, price, time_stamp, link ):
    outputFile = "products.csv"
    headers = 'Item:, Price:, Time_stamp:, Link:\n'
    with open(outputFile, "a") as out:
        if os.stat(outputFile).st_size == 0: # if the file is empty
            out.write(headers)
        else:
            out.write(f'{item},{price},{time_stamp},{link}') # write line in CSV


if __name__ == "__main__":
    main()
