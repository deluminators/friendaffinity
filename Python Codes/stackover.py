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
user=sys.argv[1]
driver.get(user)
bio = driver.find_elements_by_xpath("//div[@class='grid gs16']")
file2 = open(r"stack.txt","w")
file2.write("\nBio:")
for element in bio.text:
        	file2.write('\n')
        	file2.write(element)

try:
 communities = driver.find_elements_by_xpath("//div[@class='grid--cell profile-communities communities']")
 for element in communities.text:
        	file2.write('\n')
        	file2.write(element)

except:
	pass

try:
	top_tags=driver.find_elements_by_xpath("//div[@id='post-tag']")
	print(top_tags.text)
	for element in top_tags.text:
        	file2.write('\n')
        	file2.write(element)
except:
	pass
try:
	comm_post=driver.find_elements_by_xpath("//div[@class='grid--cell communities-posts']")
	for element in comm_post.text:
        	file2.write('\n')
        	file2.write(element)
except:
	pass
ques=user+'?tab=questions'
driver.get(ques)

try:
	questions=driver.find_elements_by_xpath("//a[@class='question-hyperlink']")
	for items in questions:
		print(items.text)
	for element in questions.text:
        	file2.write('\n')
        	file2.write(element)	
except:
	pass

anss=user+'?tab=answers'
driver.get(anss)
try:
	answers=driver.find_elements_by_xpath("//a[@class='answer-hyperlink ']")
	for items in answers:
		print(items.text)
	for element in answers.text:
        	file2.write('\n')
        	file2.write(element)	
except:
	pass


