from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "C:\development\chromedriver.exe"
IG_PASS = "kaur_codes01"
SIMILAR_ACCOUNT = "gaylemcdowell"
USERNAME = "amrinderkaur_1"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        time.sleep(2)

        username.send_keys(USERNAME)
        password.send_keys(IG_PASS)
        time.sleep(2)

        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(10)

        search = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(5)

        first_val = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div")
        first_val.click()

    def follow(self):
        time.sleep(5)
        button = self.driver.find_element_by_css_selector("#react-root section main div header section div.Igw0E.IwRSH.eGOV_._4EzTm div div div span span.vBF20._1OSdk button")
        button.click()

        # find followers of gayle and follow them
        time.sleep(5)
        follower_count = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        self.driver.execute_script("arguments[0].click();", follower_count)

        time.sleep(3)
        # address of the popup
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        # scrolling the popup
        # for i in range(10):
        #     # In this case we're executing some Javascript, that's what the execute_script() method does.
        #     # The method can accept the script as well as a HTML element.
        #     # The modal in this case, becomes the arguments[0] in the script.
        #     # Then we're using Javascript to say: "scroll the top of the modal (popup)
        #     # element by the height of the modal (popup)"
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(5)

        all_buttons = self.driver.find_elements_by_css_selector("li button")
        # for i in range(10):
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
            # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            # time.sleep(8)

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
