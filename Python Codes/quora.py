from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
chrome_options = Options()
chrome_options.add_argument("--disable-user-media-security=true")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Computerist/Downloads/chromedriver',options=chrome_options)
window_before = driver.window_handles[0]
url=sys.argv[1]
driver.get(url)

name = driver.find_element_by_xpath("//span[@class='user']")
print(name.text)
file2 = open(r"quora.txt","w")
file2.write("Name: "+name.text)
try:
	credentials=driver.find_elements_by_xpath("//span[@class='UserCredential']")
	print(credentials.text)
	file2.write("\nCredentials:")
	for element in credentials.text:
        	file2.write('\n')
        	file2.write(element)

except:
	pass

try:
	bio=driver.find_elements_by_xpath("//div[@class='ProfileDescriptionPreviewSection']")
	print(bio.text)
	file2.write("\nBio :")
	for element in bio.text:
        	file2.write('\n')
        	file2.write(element)

except:
	pass
try:
	about=driver.find_elements_by_xpath("//div[@class='AboutSection']")
	print(about.text)
	file2.write("\nAbout :")
	for element in about.text:
        	file2.write('\n')
        	file2.write(element)
except:
	pass
try:
	knows_about=driver.find_elements_by_xpath("//div[@class='EditableList ProfileExperienceList']")
	print(knows_about.text)
	file2.write("\nKnows About:")
	for element in knows_about.text:
        	file2.write('\n')
        	file2.write(element)

except:
	pass


SCROLL_PAUSE_TIME = 2

while True:
    # Scroll down to bottom
    last_height = driver.execute_script("return document.body.scrollHeight")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

try:
	questions=driver.find_elements_by_xpath("//span[@class='ui_qtext_rendered_qtext']")
	for items in questions:
		print(items.text)
	file2.write("\nQuestions:")
	for element in questions.text:
        	file2.write('\n')
        	file2.write(element)	
except:
	pass

try:
	morbtn=driver.find_elements_by_link_text("//a[@class='ui_qtext_more_link']")
	for items in morbtn:
		items.click()
except:
 pass

try:
 answer=driver.find_elements_by_xpath("//class[@class='Answer']")
 for items in answer:
 	print(items.text)
 file2.write("\nAnswers:")
	for element in answer.text:
        	file2.write('\n')
        	file2.write(element)
except: 		
	pass
