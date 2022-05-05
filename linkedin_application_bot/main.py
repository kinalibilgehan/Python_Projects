from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('C:/selenium_drivers/chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/")
driver.implicitly_wait(3)

### Clicking the sign in button
btn_sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
btn_sign_in.click()

### Email and Password Input
email_input = driver.find_element(By.ID, "username")
email_input.send_keys("YOUR EMAIL")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("YOUR PASSWORD")

### Login Account
acc_login = driver.find_element(By.CLASS_NAME, "btn__primary--large")
acc_login.click()

## Search for Jobs
btn_jobs = driver.find_element(By.ID, "ember20")
btn_jobs.click()

search_bar = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
search_bar.send_keys("SEARCH TEXT")
search_bar.click()
search_bar.send_keys(Keys.ENTER)

### Follow Companies
for i in range(8):
    company_names = driver.find_elements(By.CLASS_NAME, "job-card-container__company-name")
    try:
        company_names[i].click()
        btn_follow = driver.find_element(By.CLASS_NAME, "follow")
        btn_follow.click()
        driver.back()
    except:
        continue





# for company in company_names:
#     print(company.text)
#     print("\n")
#     company.click()
#     btn_follow = driver.find_element(By.CLASS_NAME, "follow")
#     btn_follow.click()
#     driver.back()



# job_positions = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list")
# job_positions_sliced = job_positions[0:3]

# for job in job_positions_sliced:
#     company_name = job.find_element(By.CLASS_NAME, "job-card-container__link")
#     company_name.click()
#     # btn_follow = driver.find_element(By.CLASS_NAME, "follow")
#     # btn_follow.click()
#     # driver.back()



