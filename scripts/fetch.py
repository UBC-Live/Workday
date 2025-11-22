from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''

This script uses Selenium to interact with your browser, 
loading the entire workday page and then saving the raw html. 

Instructions on using this script:

1. Run the program and a browser window should open. Dont interact with it yet and let it click onto
"log into workday". After a new tab opens and the login page is shown, you may log in.

2. Navigate to academics, then view course sections of the desired semester to scrape. 

3. Here you should click "Expand all" on the right. THIS IS IMPORTANT!!!

4. Click enter on the terminal. The script should then run, scrolling to the bottom repeatedly 
and loading all courses. After it has loaded everything, it will save the full html. 

'''

driver = webdriver.Chrome()
driver.get("https://workday.students.ubc.ca/")

btn = driver.find_element(By.LINK_TEXT, "Log into Workday")
btn.click()

driver.switch_to.window(driver.window_handles[-1])
input("Waiting for log in")

pause = 1.0  # if API calls are slow might need to increase this value
same_count = 0
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrolsl to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)

    # check if new content loaded
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        same_count += 1
    else:
        same_count = 0

    # stop after bottom reached multiple times
    if same_count > 2:
        break

    last_height = new_height

# Saves html
html = driver.page_source
with open("workday_full_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Finished")
