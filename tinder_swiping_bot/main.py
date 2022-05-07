import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

s = Service('C:/selenium_drivers/chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get("https://tinder.com/tr")
main_page = driver.current_window_handle
driver.implicitly_wait(3)

### Accept Cookies
btn_accept_cookies = driver.find_element(By.CSS_SELECTOR, "[data-testid=privacyPreferencesAccept]")
btn_accept_cookies.click()
time.sleep(3)


btn_sign_in = driver.find_element(By.CSS_SELECTOR, "[data-testid=appLoginBtn]")
btn_sign_in.click()
time.sleep(3)

### Sign in with facebook
btn_facebook_login = driver.find_element(By.XPATH, "//*[@id='c-528371988']/div/div/div[1]/div/div/div[3]/span/div[2]/button")
btn_facebook_login.click()


### Switch to facebook window
main_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)



### Facebook Login Form
email_input_bar = driver.find_element(By.ID, "email")
email_input_bar.send_keys("bilgealpkinali@gmail.com")

password_input_bar = driver.find_element(By.ID, "pass")
password_input_bar.send_keys("Bil220245.")

btn_login = driver.find_element(By.NAME, "login")
btn_login.click()


### Switch to tinder window
driver.switch_to.window(main_window)
print(driver.title)

### Accept Cookies
try:
    btn_accept_cookies = driver.find_element(By.CSS_SELECTOR, "[data-testid=privacyPreferencesAccept]")
    btn_accept_cookies.click()
    time.sleep(3)
except:
    print("No cookies")

### Accept location sharing
time.sleep(5)
btn_location_allow = driver.find_element(By.XPATH, "//*[@id='c-528371988']/div/div/div/div/div[3]/button[1]")
btn_location_allow.click()

### Accept notifications
time.sleep(5)
btn_allow_notifications = driver.find_element(By.XPATH, "//*[@id='c-528371988']/div/div/div/div/div[3]/button[1]")
btn_allow_notifications.click()


### Dismiss Gold Message
btn_dismiss_premium = driver.find_element(By.XPATH, "//*[@id='c-528371988']/div/div/div/div[3]/button[2]")
btn_dismiss_premium.click()


for _ in range(5):
    time.sleep(3)
    try:
        btn_like = driver.find_element(By.XPATH, "//*[@id='c1200009088']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
    except:
        continue
### ElementClickInterceptedException
### When you get a match like button will be hidden




