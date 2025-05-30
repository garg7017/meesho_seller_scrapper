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
