This software is designed using Beautiful Soup 4 (BS4) and Python and is intended for use by consumers to track the price of a given product over a period of time on Amazon, Ebay, Newegg, and Walmart (with more coming in the future). This is achieved by using BS4 to scrape the data from a website after being passed a URL.

It's implementation is in the form of a Chrome extension. When you click on the extension, the URL is passed to the software and is added to the list of products to be checked every day. Upon being run, it will check how long it has been since it last checked prices. If it has been 24 hours or more, it will poll the sites to check their prices, updating the CSV file.

Authorship by Aidan Farber in May of 2020