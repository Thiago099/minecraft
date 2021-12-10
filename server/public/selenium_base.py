from selenium import webdriver
OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument("--headless")
OPTIONS.add_argument("--start-maximized")
OPTIONS.add_argument("--no-sandbox")
OPTIONS.add_argument("--disable-extensions")
OPTIONS.add_argument('--disable-dev-shm-usage')    
OPTIONS.add_argument("--disable-gpu")
OPTIONS.add_argument('--disable-software-rasterizer')
OPTIONS.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")
OPTIONS.add_argument("--disable-notifications")


def chrome():
    return webdriver.Chrome(options = OPTIONS, executable_path = 'D:\\python www\\_tf\\animals\\chromedriver.exe')