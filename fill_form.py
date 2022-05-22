import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdcljO4zsRB9VgLh5wc2n2agkkW4VYygAHu-XqU4aSugpszwA/viewform?fbzx=-7653465405702150284'
LOGIN_URL = '//*[@id="SMMuxb"]/a[1]'


class FillForm:
    def __init__(self):
        self.s = Service(executable_path="C:/Development/chromedriver.exe")
        self.browser = webdriver.Chrome(service=self.s)
        self.wait = WebDriverWait(driver=self.browser, timeout=30)
        self.browser.get(FORM_URL)

    def fill_form(self, addr, price, link):
        self.adress = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')))
        self.adress.send_keys(addr)
        time.sleep(2)
        self.price = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        self.price.send_keys(price)
        time.sleep(2)
        self.link = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')))
        self.link.send_keys(link)
        time.sleep(2)
        self.send = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
        self.send.click()
        time.sleep(2)
        self.resend = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
        self.resend.click()

