from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:

    PATH = '/home/done/Documents/geckodriver'

    driver = webdriver.Firefox()
    driver.get('https://www13.9anime.to/watch/rezero-kara-hajimeru-isekai-seikatsu-2nd-season-part-2-dub.kqj6/ep-1')
    driver.implicitly_wait(20)

    # Worked:
    download_link = str(driver.find_element_by_xpath("/html/body/div[1]/div[2]/aside[1]/div[1]/div[1]/div/iframe").get_attribute("src"))

    print(download_link)
    if 'embed' in download_link:
        driver.get(download_link.replace('embed-', ''))

    print("next part")
    print(driver.title)
    driver.find_element_by_xpath("//*[@id=\"todl\"]").click()
    driver.find_element_by_xpath("//*[@id=\"downloadbtn\"]").click()

except Exception as e:
    print('error')
    print(e)
finally:
    driver.quit()


