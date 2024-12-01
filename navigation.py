from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_PASSWORD = os.getenv('GITHUB_PASSWORD')
REPO_URL = 'https://github.com/your_username/your_repo'

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open GitHub login page
driver.get('https://github.com/login')

time.sleep(2)

driver.find_element(By.ID, 'login_field').send_keys(GITHUB_USERNAME)
driver.find_element(By.ID, 'password').send_keys(GITHUB_PASSWORD)

# Submit the login form
driver.find_element(By.NAME, 'commit').click()

time.sleep(5)

# Navigate to the repository page
driver.get(REPO_URL)

time.sleep(2)

# Navigate to the "Code" tab
code_tab = driver.find_element(By.XPATH, '//span[text()="Code"]')
code_tab.click()

time.sleep(3)

# Navigate to the "Issues" tab
issues_tab = driver.find_element(By.XPATH, '//span[text()="Issues"]')
issues_tab.click()

time.sleep(3)

# Navigate to the "Pull Requests" tab
pull_requests_tab = driver.find_element(By.XPATH, '//span[text()="Pull requests"]')
pull_requests_tab.click()


time.sleep(3)

# Navigate to the "Actions" tab
actions_tab = driver.find_element(By.XPATH, '//span[text()="Actions"]')
actions_tab.click()


time.sleep(3)

# Close the browser
driver.quit()
