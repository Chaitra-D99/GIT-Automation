import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver (use Chrome in this case)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def create_github_account(email, username, password):
    try:
        # Open the GitHub sign-up page
        driver.get("https://github.com/signup")
        time.sleep(3)  # Wait for the page to load

        # Find and fill in the 'Name' field
        email_sel = driver.find_element(By.ID, "email")
        email_sel.send_keys(email)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#email-container > div.d-flex.flex-items-center.flex-column.flex-sm-row > button").click()
        time.sleep(3)


        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#password-container > div.d-flex.flex-items-center.flex-column.flex-sm-row > button").click()
        time.sleep(9)

        user_name = driver.find_element(By.ID, "login")
        user_name.send_keys(username)
        time.sleep(9)

        driver.find_element(By.CSS_SELECTOR, '#username-container > div.d-flex.flex-items-center.flex-column.flex-sm-row > button').click()
        time.sleep(3)


    except Exception as e:
        print(f"Error during account creation: {e}")
    # finally:
    #     driver.quit()

def login(user_name, password):
    try:
        # Open the GitHub sign-up page
        driver.get("https://github.com/login")

        time.sleep(3)  # Wait for the page to load

        # Find and fill in the 'Name' field
        login_field = driver.find_element(By.ID, "login_field")
        login_field.send_keys(user_name)

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        driver.find_element(By.CSS_SELECTOR, "#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button").click()
        time.sleep(3)




    except Exception as e:
        print(f"Error during account creation: {e}")
    finally:
        driver.quit()


# Usage example

email = "my_n@gmail.com"
username = "my-n-gmail-com"
password = "My_n_@123789"

create_github_account(email, username, password)
login(username, password)