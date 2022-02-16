import math
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HOST = True if len(sys.argv) == 2 and sys.argv[1] == 'True' else False
print(HOST)
options = Options()
options.add_argument(r'user-data-dir=C:\Users\Mitul\AppData\Local\Google\Chrome\Selenium')
options.add_argument('use-fake-ui-for-media-stream')
options.add_argument('—disable-notifications')
PATH = r'C:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=PATH, options=options)
driver.get(r'https://meet.google.com/ycf-esrz-rtx')

driver.implicitly_wait(10)

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)

mute_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div')
video_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div')

time.sleep(1)

mute_button.click()
video_button.click()
time.sleep(0.5)
# join_button = driver.find_element_by_xpath(
#     '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
# join_button.click()

join_button = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((
    By.XPATH,
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')))
join_button.click()

captions = driver.find_element_by_xpath(
    '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[3]/div/span/button/span[2]')
captions.click()

num_students = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[2]/div/div')))
str_num = num_students.text
total_num_students = int(str_num)
print(total_num_students)
# print(str_num)
# print(num_students)
loop_variable = True
while loop_variable:
    try:
        caption_tray = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[7]/div[1]/div[1]')
        captions = driver.find_element_by_xpath(
            '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[7]/div[1]/div[1]/div/div[2]/div')
        # //*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[7]/div[1]/div[1]/div/div[2]/div
        if captions.is_displayed():
            captions_text = captions.text.lower()
            print(captions_text)
    except:
        loop_variable = True

    updated_student_number = int(num_students.text)
    print(updated_student_number)
    if updated_student_number > total_num_students:
        total_num_students = updated_student_number
    elif updated_student_number < total_num_students:
        if updated_student_number <= math.floor(0.2 * total_num_students):
            leave_call = driver.find_element_by_xpath(
                '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button')
            leave_call.click()
            if HOST:
                just_end_call = driver.find_element_by_xpath(
                    '//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/button[1]/span')
                just_end_call.click()
