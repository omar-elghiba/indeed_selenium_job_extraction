from selenium import webdriver
from selenium.webdriver.chrome.options import Options




def create_driver(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Remote(
        command_executor='http://srv2.omarelghiba.com:4444/wd/hub', 
        options=chrome_options
    )
    return driver