from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #Webdriver for Google Chrome
from selenium.webdriver.common.by import By             #For going to an element on page same as soup
from selenium.webdriver.common.keys import Keys         #For using keys like enter, shift etc.
from selenium.webdriver.support.ui import WebDriverWait #This helps to wait on the webpage for like loading the full webpage in given seconds
from selenium.webdriver.support import expected_conditions as EC    #This tells if we get the element or not after waiting and if not the program quits
import time

# These 2 lines are for running Chrome browser in real time 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


# These 3 lines are running chrome in background only

# options = webdriver.ChromeOptions()
# options.add_argument('headless')  # To run Chrome in headless mode
# driver = webdriver.Chrome(options=options)



driver.get('https://google.com/')  #It opens the website on chrome

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))    #This waits for 5 seconds or until this class tag is found
)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")     #This find the tag with class name give, here i.e. search box
input_element.clear()                                           #Clears if anything is written there
input_element.send_keys("python" + Keys.ENTER)  #This typed in the box and pressed enter key


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "python"))    #This time its searching for partial link i.e. if a link exists partially similiar like this
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "python")      #This will find the link if the page gets load fully
link.click()                                                            #The found link will be clicked

cc=driver.find_element(By.CLASS_NAME, 'slide-copy')
print(cc)

time.sleep(10)                            #Due to this the website was open for 10 seconds
driver.quit()                             #This closed the crome after sleep time



# These are for scrolling the page
current_scroll_position = driver.execute_script("return window.scrollY") #This will provide the pixel on which it is
scroll_amount = 500  #Pixels to scroll
for _ in range(18):  #This will happen 18 times
    new_scroll_position = current_scroll_position + scroll_amount
    driver.execute_script(f"window.scrollTo(0, {new_scroll_position})")    #This will scroll to new pixel position
    current_scroll_position = driver.execute_script("return window.scrollY")   #This will again see the picel on which it is