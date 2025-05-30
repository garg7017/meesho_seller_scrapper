# 📦 Meesho Supplier Data Scraper

This Python script uses Selenium to log in to the [Meesho Supplier Panel](https://supplier.meesho.com), navigate the UI, and scrape **catalog** and **orders data** for a specified date range (e.g., one month). It downloads the order data CSV file automatically and saves it locally for further analysis.

---

## 🚀 Features

- ✅ Automated login to Meesho Supplier Panel
- ✅ Handles post-login popups
- ✅ Navigates to "Orders" section
- ✅ Selects custom date range via calendar UI
- ✅ Downloads "Orders Export" file
- ✅ Automatically saves the file to a local folder
- ✅ Moves latest downloaded file from system Downloads if needed

---

## 🧰 Tech Stack

- Python 3.10+
- [Selenium](https://selenium.dev/)
- Google Chrome + Chromedriver
- OS: macOS / Windows / Linux

---

## 📁 Folder Structure
meesho_scrapper/
├── meesho_order_scrapper.py # Main scraping script
├── downloads/ # Folder where order export files are stored
├── README.md # This file
└── requirements.txt # Python dependencies


## Create and activate a virtual environment
- python3 -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate

## Run the script
- python3 meesho_order_scrapper.py  ## To download the order report for one month 

## 📋 Expected CSV Headers:
"S.no", "Catalog ID", "Category", "Catalog Title",
"Catalog Image URL", "Product Title", "Style ID", "SKU",
"Meesho Price", "Stock"
- python3 meesho_catalog_inventory_scrapper.py  


## change the "css-YOUR_CLASS_NAME" variable with your css class for the products (catalog products). That class will be like for example: MuiBox-root css-otkopb  so you have to replace that variable with css-otkopb

⚠️ Important:
Update the variable css-YOUR_CLASS_NAME in the script with your actual CSS class for catalog product containers.
For example, if the class looks like MuiBox-root css-otkopb, replace it with just css-otkopb.