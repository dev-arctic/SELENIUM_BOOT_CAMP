from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())        
        driver.get("https://www.saucedemo.com/")
        usrName = driver.find_element(By.ID , 'user-name')
        passWd  = driver.find_element(By.ID , 'password')
        lgnBtn = driver.find_element(By.ID , 'login-button')
        sleep(2)
        usrName.send_keys('1')
        passWd.send_keys('1')
        sleep(1)
        lgnBtn.click()
        errorMessage = driver.find_element(By.XPATH , '//*[@id="login_button_container"]/div/form/div[3]/h3')
        reBoll = errorMessage.text == 'Epic sadface: Username and password do not match any user in this service'
        print(f"Hata Mesaji > {errorMessage.text}") # debuglara bak bro onemli arastir oyle neler barindiryr var. icne felan  gorurusun
        print(reBoll)
        sleep(5)
        if reBoll == True:
            driver.close()
        else:
            while True:
                pass
        


testClass = Test_Sauce()
testClass.test_invalid_login()

# https://www.saucedemo.com/ > for testing.