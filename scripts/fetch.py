from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pathlib import Path

MAX_SAME_HEIGHT_COUNT = 2

def initalize_driver(link):
    '''
    Initalizes web driver to link (Workday login page)
    '''
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    return driver


def click_workday(driver):
    '''
    Clicks the "Log into Workday" button and switches to the new window,
    done to prevent stale request
    '''
    btn = driver.find_element(By.LINK_TEXT, "Log into Workday")
    btn.click()
    driver.switch_to.window(driver.window_handles[-1])
    return driver


def scroll_bottom(driver, pause=1.0):
    '''
    Scrolls to the bottom of the page to load all dynamic content.
    Returns when can't scroll further. If misinterpreting end of page
    due to slow loading, increase pause time.
    '''
    same_count = 0
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # scroll to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        time.sleep(pause)

        # check if new content loaded
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            same_count += 1
        else:
            same_count = 0

        # stop after bottom reached multiple times
        if same_count > MAX_SAME_HEIGHT_COUNT:
            break

        last_height = new_height

    return driver


def saveTo(driver, filename):
    '''
    Saves the current page source to the given filename.
    '''
    # Create parent directories if they don't exist
    # (Probably need to change in the future)
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    html = driver.page_source
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote to ", filepath.absolute())


def main():
    '''
    Main function for the Workday data fetching process.
    See indivudual function docstrings for details.
    '''
    driver = None

    try:
        # Initalize driver
        driver = initalize_driver("https://workday.students.ubc.ca/")

        # Clicks login automaticaly, might take a second
        driver = click_workday(driver)

        # Wait for user to log in and navigate to course sections.
        # REMEMBER TO CLICK EXPAND ALL!!!

        # Input anything to continue with process
        input("Waiting")

        # Scroll
        driver = scroll_bottom(driver, pause=1.0)

        # Save the HTML
        saveTo(driver, "../data/raw/workday_full_page.html")

        print("Successful")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close browser
        if driver:
            driver.quit()
            print("Browser closed")


if __name__ == "__main__":
    main()
