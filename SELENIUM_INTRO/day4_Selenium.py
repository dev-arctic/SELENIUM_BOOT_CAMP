from selenium import webdriver # isimlendirmelere dikkat et
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
# What is Selenium
# bir browser'da yaptigimiz islmeler var bu manuel islemleri serileristiriyor biizm icin kendisi yapiyor yani, bir cok dilde kullanila bilir bi yapi.
# webdrive tanitma bir  yol daha  
# drive = webdriver.Chrome(dizin adi)
driver = webdriver.Chrome()
driver.maximize_window() # genelde driver tanaimdan sonra veririz, tam ekran aciyor iste. 
driver.get("https://www.Google.com") # verdigim url ye gidecegimi soyluyorum.
# sleep(10)
# Html Locators > yani sayfanin uzeornde ki belli attr lere ulsasmka icin bir yapi
input = driver.find_element(By.NAME,'q') # html locators iste  
# input.click()
# input.send_keys() vs. vs. gibi func. lar var.
sleep(2)
input.send_keys("https://kodlama.io")
serachBtn = driver.find_element(By.NAME,"btnK")
print(serachBtn)
sleep(2)
serachBtn.click() # bu ilgili islemi click ediyr uste
print(f"Input > {input}") # ilgili kosullar saglaniyor icine yazdiigmim paraetreyi bu inputa yazioyr.

firstResult = driver.find_element(By.XPATH , '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a')
firstResult.click()

listOfCourses = driver.find_elements(By.CLASS_NAME,'course-listing')
print(f"Kodlama.io sitesinde su anda {len(listOfCourses)} adet kurs var")
while True:
    pass


# xpath
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a