from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 100
PROMISED_UP = 10
TWITTER_EMAIL = "bilgehanpython£gmail.com"
TWITTER_PASSWORD = "Bi220245."

s = Service('C:/selenium_drivers/chromedriver.exe')
driver = webdriver.Chrome(service=s)
main_window = driver.current_window_handle

class InternetSpeedTwitterBot:
    def __init__(self):
        global s
        self.driver = webdriver.Chrome(service=s)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        btn_go = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        btn_go.click()
        time.sleep(40)
        download_speed = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.down = download_speed
        upload_speed = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        self.up = upload_speed
        print(self.down, self.up)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        btn_log_in = self.driver.find_element(By.CSS_SELECTOR, "[data-testid=loginButton]")
        btn_log_in.click()
        time.sleep(3)
        email_input_bar = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input_bar.send_keys("bilgehanpython@gmail.com")
        btn_next = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        btn_next.click()
        time.sleep(3)
        password_input_bar = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input_bar.send_keys("Bi220245.")
        btn_log = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div")
        btn_log.click()


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()