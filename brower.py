from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Navigate to Gmail login page
driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
# Enter email/phone number
email_field = driver.find_element('identifier')
email_field.send_keys('your-email@example.com')
email_field.send_keys(Keys.RETURN)

# Wait for page to load
time.sleep(1)

# Enter password
password_field = driver.find_element('password')
password_field.send_keys('your-password')
password_field.send_keys(Keys.RETURN)

# Wait for page to load
time.sleep(0)

#If you want to create a new account instead of logging in, uncomment the following lines of code:
create_account_button = driver.find_element_by_xpath('//div[@class="TnvOCe"]//a')
create_account_button.click()

# Close the browser
#driver.quit()
