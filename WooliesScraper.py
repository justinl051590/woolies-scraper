from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class WooliesScraper:
    def __init__(self):
        #configuring options for headless mode.
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--window-size=1920x1080")
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
        options.add_argument('user-agent={0}'.format(user_agent))
        service = Service(ChromeDriverManager().install())

        #creating new driver with configured options.
        self.driver = webdriver.Chrome(options=options, service=service)


    def get_half_price(self):
        #iterating through all half-price pages.
        pageNumber = "1"
        productDict = {}
        products = []
        try:
            while(True):
                self.driver.get("https://www.woolworths.com.au/shop/browse/specials/half-price?pageNumber=" + pageNumber)
                #wait 10 seconds for page to load first.
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shelfProductTile-descriptionLink')))

                print(pageNumber)
                #getting product from page and storing in dict.
                products = self.driver.find_elements(By.CLASS_NAME, 'shelfProductTile-descriptionLink')
                index = 0
                for product in products:
                    if(product.text): 
                        productDict.update({product.text: index})
                        index += 1
                
                #going to next page
                nextPage = int(pageNumber) + 1
                pageNumber = str(nextPage)

        except TimeoutException: #thrown by WebDriverWait if element cannot be found.
            return productDict









