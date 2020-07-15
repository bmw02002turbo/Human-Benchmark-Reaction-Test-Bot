from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://humanbenchmark.com/tests/reactiontime")

# If you wish to autoclick the start button, uncomment the code below
# box = driver.find_element_by_xpath("/html/body/div/div/div[4]/div[1]")
# box.click()

try:
    while True:
        # Waits until green box is detected, then clicks
        newbox = WebDriverWait(driver, 300, poll_frequency=0.0000000000001).until(
            EC.presence_of_element_located((By.CLASS_NAME, "view-go"))
        )
        newbox.click()

finally:
    driver.quit()
