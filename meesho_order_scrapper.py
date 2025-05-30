from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
import glob

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import time
from selenium.webdriver.chrome.options import Options

download_dir = os.path.abspath("downloads")

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed

driver.set_window_size(1280, 800) 

# Open Meesho Supplier Login Page
driver.get("https://supplier.meesho.com/panel/v3/new/root/login")
time.sleep(3)  # Wait for page to load

# Find username/password fields and login button (Modify based on actual elements)
email_input = driver.find_element(By.NAME, "emailOrPhone")  # Replace 'username' with actual field name
password_input = driver.find_element(By.NAME, "password")  # Replace 'password' with actual field name
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/form/button[2]")  # Adjust as needed

# Enter credentials
email_input.send_keys("username")  # Replace with actual email
password_input.send_keys("password")  # Replace with actual password

# email_input.send_keys("garg7017@gmail.com")  # Replace with actual email
# password_input.send_keys("Admin@123")  # Replace with actual password

login_button.click()

time.sleep(5)  # Wait for login to complete

# Delete the popup div with class 'MuiDialog-container'
try:
    popup = driver.find_element(By.CLASS_NAME, "MuiDialog-container")
    driver.execute_script("arguments[0].remove();", popup)
    print("Popup removed successfully!")
except:
    print("No popup found, continuing.")

driver.execute_script("document.body.style.overflow = 'auto';")
print("Removed overflow: hidden from body.")

# time.sleep(1000)
# Find and click "Orders" in the sidebar
catalog_uploads_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/nav/div/div/div/div[2]/div[2]/div/ul/div[2]/div[1]/li")
catalog_uploads_button.click()
time.sleep(5)  # Wait for page transition

# Wait until the "Download Orders Data" element is clickable and click it
download_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//p[text()='Download Orders Data']"))
)
download_btn.click()

# Wait and click on "Select Date Range"
date_range_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//p[text()='Select Date Range']"))
)
date_range_btn.click()

# OPTIONAL: Handle date selection if a calendar UI appears
# Step 3: Click on start date using the given XPath (1st of the month)
start_date_xpath = "/html/body/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div[5]/div/button"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, start_date_xpath))
).click()

# Step 4: Click on end date using the given XPath
end_date_xpath = "/html/body/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[5]/div[6]/div/button"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, end_date_xpath))
).click()

# Confirm selection if there's a button like "Apply"
apply_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[3]/button/span[1]"))
)
apply_btn.click()

# Add delay to wait for the download or next steps
time.sleep(5)

driver.refresh()


# Wait until the "Download Orders Data" element is clickable and click it
download_btn2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//p[text()='Download Orders Data']"))
)
download_btn2.click()

time.sleep(2)
# Step 2: Locate the first "Download" text AFTER "EXPORTED FILES"
report_download_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, "//*[@id='mainWrapper']/div/div[1]/section/div[2]/div[2]/div/div/div[3]/div/div[3]/div[1]/div[2]/span"
    ))
)
report_download_button.click()
time.sleep(8)

driver.quit()






















































#    ++++++++++++++++++++++++ Catalog Inventory Scraper for Meesho Supplier Panel   ++++++++++++++++++++++++ 

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import json
# import csv
# import os

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Set up WebDriver
# driver = webdriver.Chrome()

# driver.set_window_size(1280, 800) 

# # Open Meesho Supplier Login Page
# driver.get("https://supplier.meesho.com/panel/v3/new/root/login")
# time.sleep(3)  # Wait for page to load

# # Find username/password fields and login button (Modify based on actual elements)
# email_input = driver.find_element(By.NAME, "emailOrPhone")  # Replace 'username' with actual field name
# password_input = driver.find_element(By.NAME, "password")  # Replace 'password' with actual field name
# login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/form/button[2]")  # Adjust as needed

# # Enter credentials
# email_input.send_keys("modisalesagencies@gmail.com")  # Replace with actual email
# password_input.send_keys("dPC5tc@4SszaJef")  # Replace with actual password

# login_button.click()

# time.sleep(5)  # Wait for login to complete

# # Delete the popup div with class 'MuiDialog-container'
# try:
#     popup = driver.find_element(By.CLASS_NAME, "MuiDialog-container")
#     driver.execute_script("arguments[0].remove();", popup)
#     print("Popup removed successfully!")
# except:
#     print("No popup found, continuing.")

# driver.execute_script("document.body.style.overflow = 'auto';")
# print("Removed overflow: hidden from body.")


# # Find and click "Catalog Uploads" in the sidebar
# catalog_uploads_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/nav/div/div/div/div[2]/div[2]/div/ul/div[2]/div[5]/li/div")
# catalog_uploads_button.click()
# time.sleep(5)  # Wait for page transition


# # Scroll the page a bit to load content if necessary (adjust as needed)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)

# extracted_data = []
# page_number = 1
# while True:
#     print(f"Processing page {page_number}...")
    
#     catalogs = []
#     # Find all elements that have the text "Catalog ID:"
#     catalog_id_labels = driver.find_elements(By.XPATH, "//*[contains(text(),'Catalog ID:')]")

#     for label in catalog_id_labels:
#         try:
#             # The "Catalog ID:" text is in one <p>, the actual ID is likely in the next sibling <p>
#             catalog_id = label.find_element(By.XPATH, 'following-sibling::p').text
            
#             # To find the category, go up to the common container and find the "Category:" <p> label and its sibling text
#             container = label.find_element(By.XPATH, '../../..')  # adjust levels based on HTML structure
            
#             category_label = container.find_element(By.XPATH, ".//p[contains(text(),'Category:')]")
#             category = category_label.find_element(By.XPATH, 'following-sibling::p').text
            
#             # Find the title (h5) in the same container
#             title = container.find_element(By.TAG_NAME, 'h5').text
            
#             # Find image URL inside the container
#             image = container.find_element(By.TAG_NAME, 'img').get_attribute('src')
            
#             catalogs.append({
#                 'Catalog ID': catalog_id,
#                 'Category': category,
#                 'Title': title,
#                 'Image URL': image
#             })
#         except Exception as e:
#             print(f"Error extracting catalog: {e}")

#     # Remove the last item if it has the unwanted image URL
#     unwanted_url = "https://static.meeshosupply.com/supplier-new/rocket_blueAction.svg"
#     if catalogs and catalogs[-1]['Image URL'] == unwanted_url:
#         print("Removing last catalog with placeholder image.")
#         catalogs.pop()

#     catalog_copy = catalogs.copy()  # Create a copy for later use
#     time.sleep(3)

#     # List to store data for each catalog
#     catalogs_data = []
    

#     # Number of catalogs you want to process (adjust as needed)
#     num_catalogs = 10

#     # for i in range(1, num_catalogs + 1):
#     j = 1
#     for c2 in catalog_copy:
#         try:
#             print(f"\nProcessing catalog {j}...")

#             # Construct XPath dynamically
#             xpath = f'//*[@id="mainWrapper"]/div/div[6]/div[1]/div/div[2]/div[{j}]/div/div/div[2]/div[1]/p[1]'

#             # Find catalog title element
#             catalog_elem = driver.find_element(By.XPATH, xpath)
            
#             # Click catalog
#             driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", catalog_elem)
#             time.sleep(2)
            

#             # === Try a strong JS-based click using MouseEvent ===
#             click_script = """
#                 const elem = document.evaluate(arguments[0], document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
#                 if (elem) {
#                     const event = new MouseEvent('click', {
#                         view: window,
#                         bubbles: true,
#                         cancelable: true
#                     });
#                     elem.dispatchEvent(event);
#                 } else {
#                     console.log("Element not found via XPath.");
#                 }
#             """
#             driver.execute_script(click_script, xpath)
#             time.sleep(2)

#             product_blocks = driver.find_elements(By.XPATH, "//div[contains(@class, 'MuiBox-root') and contains(@class, 'css-ot1oja')]")
            
#             # extracted_data = []

#             for block in product_blocks:
#                 try:
#                     title = block.find_element(By.XPATH, ".//p[1]").text.strip()

#                     style_id_label = block.find_element(By.XPATH, ".//p[contains(text(), 'Style ID:')]")
#                     style_id = style_id_label.find_element(By.XPATH, "following-sibling::p").text.strip()

#                     sku_label = block.find_element(By.XPATH, ".//p[contains(text(), 'SKU:')]")
#                     sku = sku_label.find_element(By.XPATH, "following-sibling::p").text.strip()

#                     price_label = block.find_element(By.XPATH, ".//p[contains(text(), 'Meesho Price: ₹')]")
#                     price = price_label.find_element(By.XPATH, "following-sibling::p").text.strip()

#                     # Step 1: Find the "Current Stock" label element
#                     stock_label = driver.find_element(By.XPATH, "//*[contains(text(), 'Current Stock')]")
#                     # Step 2: Find the nearest input element after "Current Stock"
#                     stock_input = stock_label.find_element(By.XPATH, ".//following::input[1]")
#                     # Step 3: Extract the value
#                     stock_value = stock_input.get_attribute("value").strip()

#                     extracted_data.append({
#                         "S.no": j,
#                         "Catalog ID": c2['Catalog ID'],
#                         "Category": c2['Category'],
#                         "Catalog Title": c2['Title'],
#                         "Catalog Image URL": c2['Image URL'],
#                         "Product Title": title,
#                         "Style ID": style_id,
#                         "SKU": sku,
#                         "Meesho Price": price,
#                         "Stock": stock_value
#                     })

#                 except Exception as e:
#                     print("⚠️ Error parsing a block:", e)
#                     continue

#             j += 1

#         except Exception as e:
#             print("❌ Error processing catalog:", e)
#             time.sleep(3)
        
#         except Exception as e:
#             print(f"Error processing catalog {i}: {e}")
#             driver.back()
#             time.sleep(2)
    
#     # ✅ Try to find and click the "Next Page" button
#     try:
#         next_button = driver.find_element(By.XPATH, '//*[@id="mainWrapper"]/div/div[6]/div[1]/div/div[3]/div/div[7]/button')
        
#         # Check if the button has a "disabled" attribute
#         is_disabled = next_button.get_attribute("disabled")

#         if is_disabled:
#             print("✅ 'Next' button is disabled. Stopping pagination.")
#             break
#         else:
#             driver.execute_script("arguments[0].click();", next_button)
       
#         time.sleep(3)

#         # # Wait until the new page is loaded (simple way: wait for "10 Items / page" to appear again)
#         WebDriverWait(driver, 15).until(EC.presence_of_element_located(
#             (By.XPATH, "//*[contains(text(), '10 Items / page')]")
#         ))

#         page_number += 1
#         time.sleep(3)  # Give time for new catalogs to load

#     except Exception as e:
#         print(f"❌ No next page button found or click failed: {e}")
#         break

# print("\n✅ Final Extracted Data:")
# # print(json.dumps(extracted_data, indent=2, ensure_ascii=False))

# # Define the output CSV file name
# csv_file = "meesho_catalog_data.csv"

# # Check if file already exists (to decide whether to write the header)
# file_exists = os.path.isfile(csv_file)

# # Write extracted data to CSV (append mode)
# with open(csv_file, "a", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)

#     # Write the header only if the file does not already exist
#     if not file_exists:
#         writer.writerow([
#             "S.no", "Catalog ID", "Category", "Catalog Title",
#             "Catalog Image URL", "Product Title", "Style ID", "SKU",
#             "Meesho Price", "Stock"
#         ])

#     # Write rows from extracted_data
#     for item in extracted_data:
#         writer.writerow([
#             item['S.no'],
#             item['Catalog ID'],
#             item['Category'],
#             item['Catalog Title'],
#             item['Catalog Image URL'],
#             item["Product Title"],
#             item["Style ID"],
#             item["SKU"],
#             item["Meesho Price"],
#             item["Stock"]
#         ])
# driver.quit()

#    ++++++++++++++++++++++++ END OF SCRIPT: Catalog Inventory Scraper for Meesho Supplier Panel   ++++++++++++++++++++++++ 