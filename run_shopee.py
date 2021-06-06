import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from login import login # import function login
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
 
"""

"""
class ShopeeSelenium:
    def __init__(self, url):
        self.driver = webdriver.Firefox() # you can using driver cho Google Chromium
        self.driver.get(url)
 
    def get_site_info(self):
        """
            Show info web page
        """
        print('URL:', self.driver.current_url)
        print('Title:', self.driver.title)
        sleep(1)
        # self.driver.save_screenshot('screen_shot.png')
 
    def clear_pop_ups(self):
        """
            Close pop-ups on home page 
        """
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div").click() # click button x
            print("closed")
        except:
            pass

        try:
            alert = self.driver.switch_to_alert # Cai nay cung eo biet no lam gi copy from internet 
            alert.accept()
        except:
            pass

    def select_deal_1k(self):
        """
            Select 1k deal section:  click vao muc section Khuyen mai cua shopee
        """
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/a[3]").click()
            print("Select 1k section")
        except:
            print("Exception in Select 1k section")
            pass

    def test(self):
        """
            Test
        """

        try:
            keywords = [ "Đăng nhập"]
            conditions = " or ".join(["contains(text(), '%s')" % keyword for keyword in keywords])
            expression = "//*[%s]" % conditions
            print(expression)
            elms = self.driver.find_elements(By.XPATH ,expression)
            print(str(len(elms)))
            if len(elms) > 0:
                elms[0].click()
            
            # Phase Login Google 
            child = self.driver.find_element(By.XPATH ,"//*[contains(text(), 'Google')]") # element contain string Google
            parent = child.find_element(By.XPATH, ("./..")) # Lay thang cha cua thang child do element child khong co caction click
            sleep(2)
            parent.click()

        except Exception as e:
            print(e)
            pass

"""
    App Entry In here 
"""
if __name__ == '__main__':
    # init and open page
    login(username, password) # Dang bi lo do tai khoan dang su dung test co xac thuc qua otp qua tin nhan dien thoai
    sleep(5)
    shopee = ShopeeSelenium('https://shopee.vn/')
    shopee.get_site_info()
    shopee.clear_pop_ups()
    # shopee.select_deal_1k()
    # shopee.test()
    

    # Close driver
    # shopee.driver.close()