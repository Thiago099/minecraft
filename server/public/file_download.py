import time
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  


def download(file, folder):
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-dev-shm-usage')    
    options.add_argument("--disable-gpu")
    options.add_argument('--disable-software-rasterizer')
    options.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")
    options.add_argument("--disable-notifications")

    options.add_experimental_option("prefs", {
        "download.default_directory": folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        'download.behavior': 'allow',
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
        }
    )

    driver = webdriver.Chrome(
        options=options, 
        executable_path = r'D:\python www\_tf\animals\chromedriver.exe'
    )
    driver.execute_cdp_cmd('Page.setDownloadBehavior',  {
        'behavior' : 'allow',
        'downloadPath':folder
    })


    driver.get(file)

    def download_wait(directory, timeout, nfiles=None):
        seconds = 0
        dl_wait = True
        while dl_wait and seconds < timeout:
            time.sleep(1)
            dl_wait = False
            files = os.listdir(directory)
            if nfiles and len(files) != nfiles:
                dl_wait = True

            for fname in files:
                if fname.endswith('.crdownload'):
                    dl_wait = True

            seconds += 1
        return seconds


    download_wait(folder, 100)
    driver.close()