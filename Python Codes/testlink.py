from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys
user=sys.argv[1]
# defining new variable passing two parameters
#writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
#writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('C:/Users/Computerist/Downloads/chromedriver')
window_before = driver.window_handles[0]
# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

# locate email form by_class_name
username = driver.find_element_by_xpath("//input[@name='session_key']")

# send_keys() to simulate key strokes
username.send_keys("amitm.agarwal@gmail.com")

# sleep for 0.5 seconds

time.sleep(5)
# locate password form by_class_name
password = driver.find_element_by_xpath("//input[@name='session_password']")
# send_keys() to simulate key strokes
password.send_keys('hello kitty')
time.sleep(5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//button[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()
time.sleep(5)

driver.get(user)
time.sleep(8)
page=driver.find_element_by_tag_name("html")

time.sleep(8)
name = driver.find_element_by_xpath("//li[@class='inline t-24 t-black t-normal break-words']")
file2 = open(r"linkedin.txt","w")
file2.write("\nName: "+name.text)
try:
	workexp=driver.find_element_by_xpath("//li[@data-control-name='position_see_more']")
	file2.write("\nWork Experience "+workexp.text)
except:
	pass
try:
	education=driver.find_element_by_xpath("//li[@data-control-name='education_see_more']")
	file2.write("\nEducation: "+education.text)
except:
	pass
try:
	bio=driver.find_element_by_xpath("//h2[@class='mt1 t-18 t-black t-normal']")
	file2.write("\nBio: "+bio.text)
except:
 pass	
try:
	address=driver.find_element_by_xpath("//li[@class='t-16 t-black t-normal inline-block']")
	file2.write("\nAddress: "+address.text)
except:
	pass
try:
	connections=driver.find_element_by_xpath("//span[@class='t-16 t-black t-normal']")
	file2.write("\nConnections: "+connections.text)
except:
	pass
try:
	temp=driver.find_element_by_xpath("//span[@class='lt-line-clamp__line']")
	driver.execute_script("arguments[0].scrollIntoView();",temp)
	degree=driver.find_elements_by_xpath("//div[@class='pv-entity__degree-info']")
	file2.write("\nDegree:")
	for element in degree.text:
        	file2.write('\n')
        	file2.write(element)
except:
 pass	
try:
	experience=driver.find_elements_by_xpath("//li[@class='pv-profile-section__sortable-card-item pv-profile-section pv-position-entity ember-view']")
	file2.write("\nExperience:")
	for element in experience.text:
        	file2.write('\n')
        	file2.write(element)
except:
	pass
try:
	more_exp=driver.find_elements_by_xpath('//button[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar"]')
	for item in more_exp: 
		item.click()
		more_button = driver.find_element_by_xpath('//button[@class="pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link"]')
'''for item in more_button:
	item.click()'''
try:
	more_skills=driver.find_elements_by_xpath("//div[@id='skill-categories-expanded']")
	file2.write("\nMore Skills:")
	for element in more_skills.text:
        	file2.write('\n')
        	file2.write(element)
except:
 pass
try:         	
	activity=driver.find_elements_by_xpath("//div[@class='pv-profile-section pv-recent-activity-section-v2 artdeco-container-card ember-view']")
    file2.write("\nActivity:")
    for element in activity.text:
        	file2.write('\n')
        	file2.write(element)
except:
 pass 

try:        	
	recommendation=driver.find_elements_by_xpath("//section[@class='pv-profile-section pv-recommendations-section artdeco-container-card ember-view']")
	file2.write("\nRecommendations:")
	for element in recommendation.text:
        	file2.write('\n')
        	file2.write(element)
except:
	pass
try:
	accomplishments=driver.find_elements_by_xpath("//section[@class='pv-profile-section pv-accomplishments-section artdeco-container-card ember-view']")    
	file2.write("\nAccomplishments:")
    for element in accomplishments.text:
    	file2.write('\n')
    	file2.write(element)
except:
	pass

try:
	interests=driver.find_elements_by_xpath("//section[@class='pv-profile-section pv-interests-section artdeco-container-card ember-view']")
    file2.write("\nInterests:")
    for element in interests.text:
        	file2.write('\n')
        	file2.write(element)
except:
 pass
try:         	
	about=driver.find_element_by_xpath("//div[@id='oc-about-section']")
	file2.write("\nMore Skills:"+about.text)
except:
	pass
        

#print(skills.text)
try:
	temp=driver.find_element_by_xpath("//h3[@class='pv-entity__school-name t-16 t-black t-bold']")
	driver.execute_script("arguments[0].scrollIntoView();",temp)
	time.sleep(4)
	skills=driver.find_elements_by_xpath("//a[@data-control-name='skills_endorsement_full_list']")
    file2.write("\nSkills:")
    for element in skills.text:
        	file2.write('\n')
        	file2.write(element)
except:
	pass
   
for item in degree: 
    text = item.text 
    print(text) 
for item in experience: 
    text = item.text 
    print(text)
  

for item in skills: 
    text = item.text 
    print(text) 


    



#print(skills.text)
#skills=driver.find_elements_by_xpath("//a[@class='pv-skill-entity__highlight-link t-14 t-black t-normal ember-view']")
#print(skills.text)
'''for record in skills:
	print(record.find_elements_by_xpath('.//p').text)


<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,18)/shared-entity-company/" id="ember406" class="pv-skill-entity__highlight-link t-14 t-black t-normal ember-view">      Endorsed by <span class="custom-highlight t-bold">2 of Rohit’s colleagues at Georgetown University</span>
</a>'''
'''<li id="1144037549" class="pv-profile-section__sortable-card-item pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/12896024/" id="ember138" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img class="lazy-image pv-entity__logo-img pv-entity__logo-img EntityPhoto-square-5 loaded" alt="Non-Obvious Company" src="https://media.licdn.com/dms/image/C560BAQEcxOxpC0MQiA/company-logo_400_400/0?e=1571875200&amp;v=beta&amp;t=C_Uyd5p4apMwWbhssLF-SvltPPksLVT0OX65yp5mj1M">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section ">
  <h3 class="t-16 t-black t-bold">Founder &amp; Chief Trend Curator</h3>

  <h4 class="t-16 t-black t-normal">
    <span class="visually-hidden">Company Name</span>
      <span class="pv-entity__secondary-title">Non-Obvious Company</span>
  </h4>

    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>2015 – Present</span>
    </h4>
      <h4 class="t-14 t-black t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">4 yrs</span>
      </h4>
  </div>

  <h4 class="pv-entity__location t-14 t-black--light t-normal block">
    <span class="visually-hidden">Location</span>
    <span>Washington D.C. Metro Area</span>
  </h4>

</div>

</a>
<!---->    </div>

<!---->  </div>
</li>'''
'''<div id="ember235" class="pv-profile-section pv-recent-activity-section-v2 artdeco-container-card ember-view"><header class="pv-profile-section__card-header">
  <h2 class="pv-profile-section__card-heading pv-recent-activity-section-v2__headline">
      Articles &amp; activity
  </h2>
</header>

<h3 id="ember237" class="pv-recent-activity-section__follower-count t-14 t-black--light t-normal ember-view">
<span class="align-self-center pv-recent-activity-section__follower-count ">
  7,500 followers
</span>
<!----></h3>

<div class="pv-recent-activity-section-v2__summary t-14 t-black--light t-normal">
  <div class="pv-recent-activity-section-v2__columns pv-recent-activity-section-v2__columns--condensed">
      <section class="pv-recent-activity-section-v2__column pv-recent-activity-section-v2__column--post">
        <div id="ember238" class="pv-recent-activity-article-v2 Elevation-0dp pv-recent-activity-article-v2--condensed ember-view"><a data-control-name="recent_activity_article_see_more" rel="noreferrer noopener" target="_blank" href="https://www.linkedin.com/pulse/gen-z-rebelling-against-adulthood-heres-what-means-rohit-bhargava" id="ember239" class="pv-recent-activity-article-v2__content block ember-view">    <div class="pv-recent-activity-article-v2__header">
      <div class="pv-recent-activity-article-v2__image">
        <img class="lazy-image pv-recent-activity-article-v2__image-content EntityPhoto-square-6 loaded" alt="" src="https://media.licdn.com/dms/image/C4E12AQGIIB5zPdlg0w/article-cover_image-shrink_180_320/0?e=1569456000&amp;v=beta&amp;t=BkKLpgqaDDSD1IEXSjpoFzZXryDjgVZD3IJ_rrMVwvQ">

        <li-icon aria-hidden="true" type="image-icon" class="pv-recent-activity-article-v2__image-ghost" size="medium"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M21,4H3A1,1,0,0,0,2,5V19a1,1,0,0,0,1,1H21a1,1,0,0,0,1-1V5A1,1,0,0,0,21,4ZM20,6V16.65l-3.7-3.53a0.44,0.44,0,0,0-.6,0L13.79,15,7.87,9.13a0.44,0.44,0,0,0-.62,0L4,12.4V6H20ZM4,18V13.64l3.57-3.59,5.91,5.82a0.44,0.44,0,0,0,.61,0L16,14l4,3.82V18H4Zm12-6a2,2,0,1,0-2-2A2,2,0,0,0,16,12Zm0-3.25A1.25,1.25,0,1,1,14.75,10,1.25,1.25,0,0,1,16,8.75Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
      </div>
      <div class="pv-recent-activity-article-v2__title">
        <h3 class="t-16 t-black t-bold">
            <div id="ember241" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Gen Z Is Rebelling Against Adulthood. Here's What That Means ...

<!----></div>

        </h3>
        <div class="pv-recent-activity-article-v2__author">
          <div class="pv-recent-activity-article-v2__author-image inline-block">
            <div id="ember242" class="ivm-image-view-model ember-view">  <div id="ember243" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->      <img class="lazy-image ivm-view-attr__img--centered ivm-view-attr__entity-img--profile EntityPhoto-circle-1 loaded" alt="Rohit’s profile photo" src="https://media.licdn.com/dms/image/C4E03AQHAlqgWIx5z2w/profile-displayphoto-shrink_800_800/0?e=1569456000&amp;v=beta&amp;t=EzWG1ehfC6FamRrrenx2Sbb5WOym4zJvZmQ3vUNZ8KU">
</div>
</div>
          </div>
          <div class="pv-recent-activity-article-v2__details inline-block">
            <h4 class="pv-recent-activity-article-v2__details-name t-12 t-black t-bold break-words">
              Rohit Bhargava
            </h4>
            <div class="pv-recent-activity-article-v2__details-subscript t-12 t-black--light t-normal">
              Published on LinkedIn
            </div>
          </div>
        </div>
      </div>
    </div>
      <div class="pv-recent-activity-article-v2__preview t-14 t-black t-normal">
        <div class="pv-recent-activity-article-v2__preview-text" data-overflow-text="…see more">
            <div id="ember245" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 4">  What if the next generation of adults isn't all that interested in growing up? I spent last weekend at the 38th Annual&nbsp;First Year Experience Conference&nbsp;in Las Vegas where I was speaking and engaging in conversations with learning directors at schools from all over the world who are helping shape the next generation of workers and citizens ... and trying to motivate and inspire them to be successful in the world. It is a topic I often think about. Last year I wrote a career advice book called&nbsp;Always Eat Left Handed as a way to try and share the sort of irreverent advice I always tried to offer to my students when I was teaching. As multiple researchers are finding, this upcoming generation are actively rebelling against adulthood and see the world very differently than their Millennial predecessors. As the world gets more dire, politics gets angrier and the climate apocalypse brings&nbsp;snow to Hawaii, young people are increasingly looking for an escape from the traditional responsibilities of adulthood. This was the conclusion of several new pieces of research released recently, including a&nbsp;new study from the Pew Research Center&nbsp;on how young adulthood today compares with previous generations. One of the results of this shift is that for the first time ever,&nbsp;women over 30 are having more babies than younger women. Another is that crazy experiences like the "Weaving Project" in London are encouraging people to revisit their childhood by&nbsp;climbing magical rope structures&nbsp;or&nbsp;jumping into massive bean bags. According to JWT Intelligence’s SONAR™ research,&nbsp;consumers are rebelling against traditional ‘adulthood’ and embracing a more carefree mentality: 52% of Americans aged 20-29 and 47% of those aged 30-45 believe that people never truly become adults. So what does all of this mean and what will it take to reach this new generation and earn their trust?&nbsp; It is no longer enough to focus on function and benefits alone. The best products and services that win with this new audience will also promote whimsy and delight along with the "softer side" of an experience that demonstrate it is worth having. A long time ago, the consumer question used to be: "where's the beef?" Today the better question to ask might be ... "where's the fun?"

<!----></div>

        </div>
      </div>
</a>
<div class="pv-recent-activity-article-v2__footer">
      <div class="pv-recent-activity-article-v2__social-counts t-14 t-black--light t-normal">
          <span class="pv-recent-activity-article-v2__social-counts-item pv-recent-activity-article-v2__social-counts-item--likes">
            30 Likes
          </span>

          <span class="pv-recent-activity-article-v2__social-counts-item pv-recent-activity-article-v2__social-counts-item--comments">
            5 Comments
          </span>
      </div>
  <div class="pv-recent-activity-article-v2__social-actions">
<div id="ember246" class="feed-shared-social-actions feed-shared-social-action-bar social-detail-base-social-actions feed-shared-social-action-bar--minimal-padding ember-view">      <span id="ember247" class="reactions-react-button reactions-react-button--flat feed-shared-social-action-bar__action-btn ember-view"><!---->
<button aria-label="Like" aria-pressed="false" id="ember248" class="react-button__trigger artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view"><!---->
<span class="artdeco-button__text">
          <li-icon aria-hidden="true" type="like-icon" class="artdeco-button__icon"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M17.51,11L15.36,8a14.81,14.81,0,0,1-2.25-5.29L12.74,1H10.5A2.5,2.5,0,0,0,8,3.5V4.08a9,9,0,0,0,.32,2.39L9,9H4.66A2.61,2.61,0,0,0,2,11.4a2.48,2.48,0,0,0,.39,1.43,2.48,2.48,0,0,0,.69,3.39,2.46,2.46,0,0,0,1.45,2.92,2.47,2.47,0,0,0,0,.36A2.5,2.5,0,0,0,7,22h4.52a8,8,0,0,0,1.94-.24l3-.76H21V11H17.51ZM19,19H16.88l-3.41.82A6,6,0,0,1,12,20H7a0.9,0.9,0,0,1-.9-0.89s0-.07,0-0.14l0.15-1-1-.4a0.9,0.9,0,0,1-.55-0.83,0.93,0.93,0,0,1,0-.22L5,15.57,4.27,15a0.9,0.9,0,0,1-.39-0.74A0.88,0.88,0,0,1,4,13.82l0.46-.72L4,12.38a0.88,0.88,0,0,1-.14-0.51,1,1,0,0,1,1-.87H11.5L10.2,6.3a9,9,0,0,1-.33-2.37V3.38a0.5,0.5,0,0,1,.5-0.5h0.95a17.82,17.82,0,0,0,2.52,6.22L16.6,13H19v6Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

    <span class="artdeco-button__text react-button__text react-button__text--">
        Like
    </span>

</span></button>
<!----></span>
      <span id="ember249" class="comment ember-view"><button data-control-name="comment" aria-label="Comment" id="ember250" class="artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view">  <li-icon aria-hidden="true" type="speech-bubble-icon" class="artdeco-button__icon"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M18,10H6V9H18v1Zm4-5V22l-5-4H3a1,1,0,0,1-1-1V5A1,1,0,0,1,3,4H21A1,1,0,0,1,22,5ZM20,6H4V16H17.7L20,17.84V6Zm-4,6H8v1h8V12Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<span class="artdeco-button__text">
    Comment
</span></button>
</span>
<div id="ember251" class="reader-social-bar-v2__external-share social-share ember-view"><artdeco-dropdown id="ember252" class="ember-view"><artdeco-dropdown-trigger aria-expanded="false" role="button" placement="top" id="ember253" class="social-share__dropdown-trigger artdeco-button artdeco-button--4 artdeco-button--tertiary artdeco-button--muted ember-view" tabindex="0">    <li-icon aria-hidden="true" type="share-linkedin-icon" class="artdeco-button__icon" size="medium"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M24,12h0a1.18,1.18,0,0,0-.36-0.84L14,2V8H11A10,10,0,0,0,1,18v4H2.87A6.11,6.11,0,0,1,9,16h5v6l9.63-9.14A1.18,1.18,0,0,0,24,12s0,0,0,0h0Zm-8,5.54V14H9a8.15,8.15,0,0,0-6,2.84A8,8,0,0,1,11,10h5V6.48L21.81,12Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
    <span class="artdeco-button__text">Share</span>

<!----></artdeco-dropdown-trigger>
<artdeco-dropdown-content arrow-dir="left" justification="left" placement="top" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember254" class="artdeco-dropdown-with-arrow ember-view"><artdeco-dropdown-header id="ember255" class="social-share__header-text ember-view">      Share on LinkedIn

</artdeco-dropdown-header>
<artdeco-dropdown-item data-control-name="social_share_post" role="button" data-dropdown="" id="ember256" class="social-share__item social-share__item--share-box-btn display-flex ember-view" tabindex="0">      <li-icon aria-hidden="true" type="pencil-icon" class="mr2"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M21.71,5L19,2.29a1,1,0,0,0-1.41,0L4,15.85,2,22l6.15-2L21.71,6.45A1,1,0,0,0,22,5.71,1,1,0,0,0,21.71,5ZM6.87,18.64l-1.5-1.5L15.92,6.57l1.5,1.5ZM18.09,7.41l-1.5-1.5,1.67-1.67,1.5,1.5Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
      Share in a post

</artdeco-dropdown-item>
<artdeco-dropdown-item data-dropdown="" id="ember257" class="display-flex ember-view" tabindex="0"><div data-control-name="social_message" id="ember258" class="ember-view">    <button class="message-anywhere-button social-share__item social-share__item--msg-btn" aria-label="Send group message to " data-ember-action="" data-ember-action-259="259">
                <li-icon aria-hidden="true" type="messages-icon" class="mr2 flex-shrink-zero"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M21,8H8A1,1,0,0,0,7,9V19a1,1,0,0,0,1,1H18l4,3V9A1,1,0,0,0,21,8ZM20,19.11L18.52,18H9V10H20v9.11ZM12,15h5v1H12V15ZM4,13H5v2H3a1,1,0,0,1-1-1V4A1,1,0,0,1,3,3H16a1,1,0,0,1,1,1V6H15V5H4v8Zm14,0H11V12h7v1Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
        Send in a message

    </button>

<div id="ember295" class="ember-view"><!----></div></div>
</artdeco-dropdown-item>
<artdeco-dropdown-header id="ember260" class="social-share__header-text ember-view">      Other options

</artdeco-dropdown-header>

<artdeco-dropdown-item data-control-name="social_copy_link" role="button" data-dropdown="" id="ember261" class="social-share__item social-share__item--copy-link display-flex ember-view" tabindex="0">      <li-icon aria-hidden="true" type="link-icon" class="mr2"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M17.29,3a3.7,3.7,0,0,0-2.62,1.09L12.09,6.67A3.7,3.7,0,0,0,11,9.29a3.65,3.65,0,0,0,.52,1.86l-0.37.37a3.66,3.66,0,0,0-4.48.56L4.09,14.67a3.71,3.71,0,1,0,5.24,5.24l2.59-2.59A3.7,3.7,0,0,0,13,14.71a3.65,3.65,0,0,0-.52-1.86l0.37-.37a3.66,3.66,0,0,0,4.48-.57l2.59-2.59A3.71,3.71,0,0,0,17.29,3ZM11.13,14.71a1.82,1.82,0,0,1-.54,1.3L8,18.59A1.83,1.83,0,0,1,5.41,16L8,13.41a1.79,1.79,0,0,1,1.74-.48L8.28,14.4A0.94,0.94,0,0,0,9.6,15.73l1.46-1.46A1.82,1.82,0,0,1,11.13,14.71ZM18.59,8L16,10.59a1.79,1.79,0,0,1-1.74.48L15.73,9.6A0.94,0.94,0,0,0,14.4,8.27L12.94,9.74A1.79,1.79,0,0,1,13.41,8L16,5.41A1.83,1.83,0,0,1,18.59,8Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
      Copy link

</artdeco-dropdown-item>
<artdeco-dropdown-item data-control-name="share_fb" aria-label="Share to Facebook" role="button" data-dropdown="" id="ember262" class="social-share__item social-share__item--external display-flex ember-view" tabindex="0">        <li-icon aria-hidden="true" type="facebook-icon" class="mr2"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="social-icon" focusable="false"><g style="fill: currentColor" class="solid-icon">
        <rect x="-0.003" style="fill:none;" width="24" height="24"></rect>
        <path style="" d="M20,2h-16c-1.1,0-2,0.9-2,2v16c0,1.1,0.9,2,2,2h16c1.1,0,2-0.9,2-2V4C22,2.9,21.1,2,20,2zM19.2,10l-0.6,3h-2.6v6h-3v-6h-2v-3h2V8.5C13,6.4,13.6,5,16.6,5h2.4v3h-2.3c-0.5,0-0.7,0.2-0.7,0.7V10H19.2z"></path>
      </g></svg></li-icon>
        Facebook

</artdeco-dropdown-item><artdeco-dropdown-item data-control-name="share_twitter" aria-label="Share to Twitter" role="button" data-dropdown="" id="ember263" class="social-share__item social-share__item--external display-flex ember-view" tabindex="0">        <li-icon aria-hidden="true" type="twitter-icon" class="mr2"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="social-icon" focusable="false"><g style="fill: currentColor" class="solid-icon">
        <rect x="-0.003" style="fill:none;" width="24" height="24"></rect>
        <path style="" d="M21,7.7c0,0.2,0,0.4,0,0.6C21,14.4,16.5,21,8.3,21c-2.5,0-5.4-0.5-7.3-1.6c2.7,0,5.1-0.7,7-2c-2-0.2-3.7-1.3-4.3-3c0.7,0.1,1.9-0.1,2.3-0.3c-2-0.6-3.1-2.1-3.4-4.1c0.4,0.2,1.2,0.2,1.7,0.1c-1-0.8-1.4-2.2-1.4-3.8c0-0.8,0.2-1.7,0.6-2.3c1.9,2.8,5.2,4.9,8.7,5.1c-0.1-0.5-0.3-1.2-0.3-1.8C12,4.8,13.7,3,16.3,3c1.9,0,2.8,0.7,3.6,1.7c0.9-0.3,1.7-0.8,2.5-1.3c-0.2,1.1-0.8,2.1-1.8,2.7c0.9-0,1.8-0.3,2.6-0.7C22.7,6.2,22,7,21,7.7z"></path>
      </g></svg></li-icon>
        Twitter

</artdeco-dropdown-item>

</artdeco-dropdown-content></artdeco-dropdown>
<div id="ember264" class="ember-view"><div id="ember265" class="ember-view"><!----></div></div>
</div>
</div>  </div>
</div>
</div>

<a data-control-name="recent_activity_posts_all" href="/in/rohitbhargava/detail/recent-activity/posts/" id="ember266" class="pv-recent-activity-section__see-more-inline pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link inline-block mt4 ember-view">            See all articles
</a>      </section>

      <div class="pv-recent-activity-section-v2__column pv-recent-activity-section-v2__column--activity">
        <ul class="pv-recent-activity-section-v2__column-activity list-style-none">
            <li id="ember268" class="pv-recent-activity-item-v2 pv-recent-activity-item-v2--condensed ember-view"><a data-control-name="view_activity_details" href="https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A6553280971788087296?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6553234662435680256%2C6553280949960929280%29" id="ember269" class="pv-recent-activity-item-v2__detail app-aware-link ember-view">    <div class="pv-recent-activity-item-v2__entity-logo ">
      <div id="ember270" class="ivm-image-view-model ember-view">  <div id="ember271" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->      <img class="lazy-image ivm-view-attr__img--centered EntityPhoto-square-4 pv-recent-activity-item-v2__image EntityPhoto-square-4 loaded" alt="No alt text provided for this image" src="https://media.licdn.com/dms/image/C4E22AQHCgO_K62Ddyw/feedshare-shrink_8192/0?e=1566432000&amp;v=beta&amp;t=AEKWjr4-_IUmZp03QJpXVqefaxG1-R9Z95ows484Hkk">
</div>
</div>
<!---->    </div>
    <div class="pv-recent-activity-item-v2__summary-info">
        <h3 class="pv-recent-activity-item-v2__title t-16 t-black t-bold break-words">
            <div id="ember273" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Great idea!

<!----></div>

        </h3>
        <p class="pv-recent-activity-item-v2__message t-14 t-black t-normal">
            <div id="ember275" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Rohit commented

<!----></div>

        </p>
<!---->    </div>
</a></li>
            <li id="ember277" class="pv-recent-activity-item-v2 pv-recent-activity-item-v2--condensed ember-view"><a data-control-name="view_activity_details" href="https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A6548233175452172288?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6547559670947602432%2C6548233148080152576%29" id="ember278" class="pv-recent-activity-item-v2__detail app-aware-link ember-view">    <div class="pv-recent-activity-item-v2__entity-logo ">
      <div id="ember279" class="ivm-image-view-model ember-view">  <div id="ember280" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->      <img class="lazy-image ivm-view-attr__img--centered EntityPhoto-circle-4 pv-recent-activity-item-v2__image EntityPhoto-square-4 loaded" alt="View Corie Spialek’s profile" src="https://media.licdn.com/dms/image/C4E03AQHyWxrnmlAJGg/profile-displayphoto-shrink_800_800/0?e=1569456000&amp;v=beta&amp;t=B9yRgS5Jtk5MbEpuKe_mPOL6G3h-CXy1k4tOBijMKgU">
</div>
</div>
<!---->    </div>
    <div class="pv-recent-activity-item-v2__summary-info">
        <h3 class="pv-recent-activity-item-v2__title t-16 t-black t-bold break-words">
            <div id="ember282" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Thanks for reading!

<!----></div>

        </h3>
        <p class="pv-recent-activity-item-v2__message t-14 t-black t-normal">
            <div id="ember284" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Rohit commented

<!----></div>

        </p>
<!---->    </div>
</a></li>
            <li id="ember286" class="pv-recent-activity-item-v2 pv-recent-activity-item-v2--condensed ember-view"><a data-control-name="view_activity_details" href="https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A6547123489264975872?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6545675085372542977%2C6547123459103739904%29" id="ember287" class="pv-recent-activity-item-v2__detail app-aware-link ember-view">    <div class="pv-recent-activity-item-v2__entity-logo ">
      <div id="ember288" class="ivm-image-view-model ember-view">  <div id="ember289" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->      <img class="lazy-image ivm-view-attr__img--centered EntityPhoto-circle-4 pv-recent-activity-item-v2__image EntityPhoto-square-4 loaded" alt="View Jori Hume’s profile" src="https://media.licdn.com/dms/image/C4E03AQGBTmOc8HySvQ/profile-displayphoto-shrink_800_800/0?e=1569456000&amp;v=beta&amp;t=Vo-STAxEhlQ7kbKFFHj9lMrIHwliQXRAvAR8-3aqpyg">
</div>
</div>
<!---->    </div>
    <div class="pv-recent-activity-item-v2__summary-info">
        <h3 class="pv-recent-activity-item-v2__title t-16 t-black t-bold break-words">
            <div id="ember291" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Thanks so much Jori!

<!----></div>

        </h3>
        <p class="pv-recent-activity-item-v2__message t-14 t-black t-normal">
            <div id="ember293" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Rohit commented

<!----></div>

        </p>
<!---->    </div>
</a></li>
        </ul>

<a data-control-name="recent_activity_details_all" href="/in/rohitbhargava/detail/recent-activity/" id="ember294" class="pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link inline-block mt4 ember-view">            See all activity
</a>      </div>
  </div>
</div>

<!----></div>'''
'''<button class="pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link" aria-expanded="false">Show 2 more experiences
<li-icon aria-hidden="true" type="chevron-down-icon" class="pv-profile-section__toggle-detail-icon" size="small"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M8,9l5.93-4L15,6.54l-6.15,4.2a1.5,1.5,0,0,1-1.69,0L1,6.54,2.07,5Z" class="small-icon" style="fill-opacity: 1"></path></svg></li-icon></button>'''
'''<div id="skill-categories-expanded" role="region" tabindex="-1" class="pv-skill-categories-section__expanded">
<div id="ember1082" class="pv-skill-category-list pv-profile-section__section-info mb6 ember-view"><h3 class="pb2 t-16 t-black--light t-normal pv-skill-categories-section__secondary-skill-heading">
  Industry Knowledge<!----></h3>
<ol class="pv-skill-category-list__skills_list list-style-none">
                <li id="ember1084" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,15)/" id="ember1086" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Digital Marketing
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,15)/" id="ember1087" class="ember-view">          <span class="visually-hidden">See 117 endorsements for Digital Marketing</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">99+</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1089" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,7)/" id="ember1091" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Blogging
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,7)/" id="ember1092" class="ember-view">          <span class="visually-hidden">See 105 endorsements for Blogging</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">99+</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1094" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,55)/" id="ember1096" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Online Advertising
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,55)/" id="ember1097" class="ember-view">          <span class="visually-hidden">See 96 endorsements for Online Advertising</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">96</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1099" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,5)/" id="ember1101" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Integrated Marketing
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,5)/" id="ember1102" class="ember-view">          <span class="visually-hidden">See 94 endorsements for Integrated Marketing</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">94</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1104" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,53)/" id="ember1106" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Strategy
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,53)/" id="ember1107" class="ember-view">          <span class="visually-hidden">See 88 endorsements for Strategy</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">88</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1109" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,9)/" id="ember1111" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Marketing
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,9)/" id="ember1112" class="ember-view">          <span class="visually-hidden">See 74 endorsements for Marketing</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">74</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1114" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,58)/" id="ember1116" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Marketing Strategy
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,58)/" id="ember1117" class="ember-view">          <span class="visually-hidden">See 72 endorsements for Marketing Strategy</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">72</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1119" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,16)/" id="ember1121" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Digital Strategy
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,16)/" id="ember1122" class="ember-view">          <span class="visually-hidden">See 58 endorsements for Digital Strategy</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">58</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1124" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,54)/" id="ember1126" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            E-commerce
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,54)/" id="ember1127" class="ember-view">          <span class="visually-hidden">See 37 endorsements for E-commerce</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">37</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1129" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,44)/" id="ember1131" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Public Relations
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,44)/" id="ember1132" class="ember-view">          <span class="visually-hidden">See 36 endorsements for Public Relations</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">36</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1134" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,56)/" id="ember1136" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Publishing
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,56)/" id="ember1137" class="ember-view">          <span class="visually-hidden">See 26 endorsements for Publishing</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">26</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1139" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,40)/" id="ember1141" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Press Releases
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,40)/" id="ember1142" class="ember-view">          <span class="visually-hidden">See 25 endorsements for Press Releases</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">25</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1144" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,57)/" id="ember1146" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            CRM
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,57)/" id="ember1147" class="ember-view">          <span class="visually-hidden">See 21 endorsements for CRM</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">21</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1149" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,39)/" id="ember1151" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Digital Media
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,39)/" id="ember1152" class="ember-view">          <span class="visually-hidden">See 19 endorsements for Digital Media</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">19</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1154" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,6)/" id="ember1156" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Interactive Marketing
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,6)/" id="ember1157" class="ember-view">          <span class="visually-hidden">See 18 endorsements for Interactive Marketing</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">18</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1159" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,41)/" id="ember1161" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Marketing Communications
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,41)/" id="ember1162" class="ember-view">          <span class="visually-hidden">See 15 endorsements for Marketing Communications</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">15</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1164" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,51)/" id="ember1166" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Online Marketing
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,51)/" id="ember1167" class="ember-view">          <span class="visually-hidden">See 15 endorsements for Online Marketing</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">15</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1169" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,45)/" id="ember1171" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Brand Development
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,45)/" id="ember1172" class="ember-view">          <span class="visually-hidden">See 12 endorsements for Brand Development</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">12</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1174" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,12)/" id="ember1176" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Consulting
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,12)/" id="ember1177" class="ember-view">          <span class="visually-hidden">See 8 endorsements for Consulting</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">8</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1179" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,46)/" id="ember1181" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            SEM
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,46)/" id="ember1182" class="ember-view">          <span class="visually-hidden">See 7 endorsements for SEM</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">7</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1184" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,48)/" id="ember1186" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Email Marketing
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,48)/" id="ember1187" class="ember-view">          <span class="visually-hidden">See 7 endorsements for Email Marketing</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">7</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1189" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,13)/" id="ember1191" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Production Managment
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,13)/" id="ember1192" class="ember-view">          <span class="visually-hidden">See 5 endorsements for Production Managment</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">5</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1194" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,42)/" id="ember1196" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Creative Strategy
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,42)/" id="ember1197" class="ember-view">          <span class="visually-hidden">See 5 endorsements for Creative Strategy</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">5</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1199" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,43)/" id="ember1201" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Copywriting
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,43)/" id="ember1202" class="ember-view">          <span class="visually-hidden">See 5 endorsements for Copywriting</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">5</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1204" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,49)/" id="ember1206" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            New Media
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,49)/" id="ember1207" class="ember-view">          <span class="visually-hidden">See 5 endorsements for New Media</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">5</span>
</a>
<!---->
  </div>

</div>

<!----></li>

</ol>
</div><div id="ember1209" class="pv-skill-category-list pv-profile-section__section-info mb6 ember-view"><h3 class="pb2 t-16 t-black--light t-normal pv-skill-categories-section__secondary-skill-heading">
  Tools &amp; Technologies<!----></h3>
<ol class="pv-skill-category-list__skills_list list-style-none">
                <li id="ember1211" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,50)/" id="ember1213" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Google Analytics
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,50)/" id="ember1214" class="ember-view">          <span class="visually-hidden">See 5 endorsements for Google Analytics</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">5</span>
</a>
<!---->
  </div>

</div>

<!----></li>

</ol>
</div><div id="ember1216" class="pv-skill-category-list pv-profile-section__section-info mb6 ember-view"><h3 class="pb2 t-16 t-black--light t-normal pv-skill-categories-section__secondary-skill-heading">
  Interpersonal Skills<!----></h3>
<ol class="pv-skill-category-list__skills_list list-style-none">
                <li id="ember1218" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,30)/" id="ember1220" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Public Speaking
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,30)/" id="ember1221" class="ember-view">          <span class="visually-hidden">See 28 endorsements for Public Speaking</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">28</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1223" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,52)/" id="ember1225" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Leadership
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,52)/" id="ember1226" class="ember-view">          <span class="visually-hidden">See 27 endorsements for Leadership</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">27</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1228" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,11)/" id="ember1230" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Team Leadership
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,11)/" id="ember1231" class="ember-view">          <span class="visually-hidden">See 9 endorsements for Team Leadership</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">9</span>
</a>
<!---->
  </div>

</div>

<!----></li>

</ol>
</div><div id="ember1233" class="pv-skill-category-list pv-profile-section__section-info mb6 ember-view"><h3 class="pb2 t-16 t-black--light t-normal pv-skill-categories-section__secondary-skill-heading">
  Other Skills<artdeco-hoverable-trigger tabindex="-1" id="ember1234" class="ember-view">      <button aria-describedby="artdeco-hoverable-skill-category-other-tooltip">
        <li-icon type="question-pebble-icon" size="small" role="img" aria-label="What is Other category?"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M7,10h2v2H7V10zM15,8c0,3.9-3.1,7-7,7s-7-3.1-7-7c0-3.9,3.1-7,7-7S15,4.1,15,8zM13.2,8c0-2.9-2.3-5.2-5.2-5.2S2.8,5.1,2.8,8c0,2.9,2.3,5.2,5.2,5.2S13.2,10.9,13.2,8zM8.5,4h-1C6.1,4,5,5.1,5,6.5V7h1.9V5.9h2.3v1.3H8c-0.6,0-1,0.4-1,1V9h1.5C9.9,9,11,7.9,11,6.5C11,5.1,9.9,4,8.5,4z" class="small-icon" style="fill-opacity: 1"></path></svg></li-icon>
      </button>
</artdeco-hoverable-trigger>
<div id="skill-category-other-tooltip" style="display: none;" class="ember-view"><div id="ember1236" class="ember-view"></div></div></h3>
<ol class="pv-skill-category-list__skills_list list-style-none">
                <li id="ember1238" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,10)/" id="ember1240" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Web Strategy
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,10)/" id="ember1241" class="ember-view">          <span class="visually-hidden">See 5 endorsements for Web Strategy</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">5</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1243" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,8)/" id="ember1245" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Creative Direction
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,8)/" id="ember1246" class="ember-view">          <span class="visually-hidden">See 17 endorsements for Creative Direction</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">17</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1248" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,47)/" id="ember1250" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Social Networking
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,47)/" id="ember1251" class="ember-view">          <span class="visually-hidden">See 12 endorsements for Social Networking</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">12</span>
</a>
<!---->
  </div>

</div>

<!----></li>

                <li id="ember1253" class="pv-skill-category-entity pv-skill-category-entity--secondary pt4 pv-skill-endorsedSkill-entity relative ember-view">

<div class="pv-skill-category-entity__skill-wrapper" tabindex="-1">

<!---->
  <div class="display-flex align-items-center flex-grow-1 full-width">

    <p class="pv-skill-category-entity__name tooltip-container" tabindex="-1">
<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,14)/" id="ember1255" class="display-block full-width ember-view">          <span class="pv-skill-category-entity__name-text t-16 t-black t-bold">
            Personality
          </span>
</a>
<!---->    </p>

<a data-control-name="skills_endorsement_full_list" href="/in/rohitbhargava/detail/skills/(ACoAAAAyhwkBIXjoy1omwHQolCL8RM7CDN_LWFQ,14)/" id="ember1256" class="ember-view">          <span class="visually-hidden">See 6 endorsements for Personality</span>
          <span class="pv-skill-category-entity__endorsement-count t-14 t-black--light t-normal" aria-hidden="true">6</span>
</a>
<!---->
  </div>

</div>

<!----></li>

</ol>
</div>    </div>








'''
'''
<button class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar" aria-controls="skill-categories-expanded" aria-expanded="false" data-control-name="skill_details" data-ember-action="" data-ember-action-885="885">
                    <span aria-hidden="true">
                    Show more
                  </span>
                  <span class="visually-hidden">
                    Show all of Rohit’s skills
                  </span>
                  <li-icon aria-hidden="true" type="chevron-down-icon" class="pv-skills-section__chevron-icon" size="small"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M8,9l5.93-4L15,6.54l-6.15,4.2a1.5,1.5,0,0,1-1.69,0L1,6.54,2.07,5Z" class="small-icon" style="fill-opacity: 1"></path></svg></li-icon>

</button>

<section id="ember886" class="pv-profile-section pv-recommendations-section artdeco-container-card ember-view"><div class="recommendations-inlining">
<!----><!---->
  <header class="pv-profile-section__card-header">
    <h2 class="pv-profile-section__card-heading">Recommendations</h2>
  </header>

<artdeco-tabs size="40dp" id="ember887" class="mt1 ember-view"><artdeco-tablist aria-multiselectable="false" id="ember888" class="native-scroll no-wrap ember-view" role="tablist"><artdeco-tab tabindex="0" aria-selected="true" aria-expanded="true" id="ember889" class="active ember-view" role="tab" selected="selected" aria-controls="ember891">        Received (10)
</artdeco-tab><artdeco-tab tabindex="-1" aria-selected="false" aria-expanded="false" id="ember890" class="ember-view" role="tab" aria-controls="ember903">        Given (5)
</artdeco-tab>
</artdeco-tablist>
<artdeco-tabpanel aria-hidden="false" id="ember891" class="active ember-view" role="tabpanel" aria-labelledby="ember889"><!---->
<div id="ember892" class="ember-view">          <div id="ember893" class="ember-view"><ul id="recommendation-list" class="section-info" tabindex="-1">
    <li id="ember894" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/admissionnetwork/" id="ember895" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl ghost-person loaded" alt="Rebecca Eckstein, MA, CEC" height="56" width="56" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Rebecca Eckstein, MA, CEC</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Executive Leadership Coach | Educational Consultant | Seminar Facilitator and Speaker | Enrollment Success</p>
        <p class="t-12 t-black--light t-normal">
          December 30, 2017, Rebecca and Rohit were students together
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember897" class="ember-view">    <span class="lt-line-clamp__line">Rohit is the best when it comes to idea creation. He is innovative</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      where others are ordinary!<!----></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember898" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/paulvogelzang/" id="ember899" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl loaded" alt="Paul Vogelzang" height="56" width="56" src="https://media.licdn.com/dms/image/C4D03AQEYZGQ3V22pZA/profile-displayphoto-shrink_100_100/0?e=1569456000&amp;v=beta&amp;t=rcHyU6q_UEFQyi4dAF4WlLbup7ALktu3ZBJGursI6-8">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Paul Vogelzang</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Chief Digital Officer ► Host of Award Winning, The Not Old - Better Show, Freelance Producer/Director/Voice Over</p>
        <p class="t-12 t-black--light t-normal">
          March 24, 2016, Paul worked with Rohit but at different companies
        </p>
    </div>
</a></div
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember901" class="ember-view">    <span class="lt-line-clamp__line">While I'd remained "connected" to Rohit over the years, after first</span>
      <span class="lt-line-clamp__line">meeting him at Ogilvy 7-8 years ago, we ran into each other</span>
      <span class="lt-line-clamp__line">yesterday at an event.  Not only was it great to see him, but his</span>
      <span class="lt-line-clamp__line">gracious, generous and "High EQ" style was as if we'd been close</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      professional friends.  That's important. Prior to our con<span class="lt-line-clamp__ellipsis">...
            <a href="#" class="lt-line-clamp__more">See more</a>
        </span></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember1296" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/allandick/" id="ember1297" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl ghost-person loaded" alt="Allan Dick" height="56" width="56" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Allan Dick</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Co-Founder at CommerceNext</p>
        <p class="t-12 t-black--light t-normal">
          October 9, 2015, Allan worked with Rohit in different groups
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember1299" class="ember-view">    <span class="lt-line-clamp__line">I worked with Rohit when he spoke as the keynote speaker at the</span>
      <span class="lt-line-clamp__line">2015 Shop.org Digital Summit Boot Camp. His high level of</span>
      <span class="lt-line-clamp__line">professionalism (example: willingness to work with the conference</span>
      <span class="lt-line-clamp__line">to tailor his presentation to the audience) and the quality of</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      content made him one of the best speakers I have work<span class="lt-line-clamp__ellipsis">...
            <a href="#" class="lt-line-clamp__more">See more</a>
        </span></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember1301" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/patrickokeefe/" id="ember1302" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl loaded" alt="Patrick O&amp;#39;Keefe" height="56" width="56" src="https://media.licdn.com/dms/image/C4D03AQGykTvMUnchFA/profile-displayphoto-shrink_100_100/0?e=1569456000&amp;v=beta&amp;t=Wh_9kbQ4CQEqIO0kLOvdpc7l0e9JeLZJOcXjPvmgNI4">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Patrick O'Keefe</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Director of Community, The Community Company</p>
        <p class="t-12 t-black--light t-normal">
          May 29, 2014, Patrick worked with Rohit but at different companies
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember1304" class="ember-view">    <span class="lt-line-clamp__line">Rohit is really impressive. Smart, deeply experienced, a great</span>
      <span class="lt-line-clamp__line">communicator. He's entertaining and insightful as a speaker. He's</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      also very kind and approachable. I hold him in high regard.<!----></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember1306" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/brandonschaefer/" id="ember1307" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl ghost-person loaded" alt="Brandon Schaefer" height="56" width="56" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Brandon Schaefer</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Simple Business Help</p>
        <p class="t-12 t-black--light t-normal">
          September 11, 2013, Brandon worked with Rohit but at different companies
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember1309" class="ember-view">    <span class="lt-line-clamp__line">I'm recommending Rohit for his work in bringing more humanity</span>
      <span class="lt-line-clamp__line">back to business. Rohit is an amazing author and I highly</span>
      <span class="lt-line-clamp__line">recommend you pick up his book "LIKEONOMICS" to learn how</span>
      <span class="lt-line-clamp__line">you can become more successful in your own life. There are few</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      people that will benefit you as much as Rohit will.<!----></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember1311" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/asktinu/" id="ember1312" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl loaded" alt="Tinu Abayomi-Paul" height="56" width="56" src="https://media.licdn.com/dms/image/C4D03AQET3nBXxMSUrA/profile-displayphoto-shrink_100_100/0?e=1569456000&amp;v=beta&amp;t=823L-rxFrOICFYEaThx56y4yu2fCOAXtjrfZHwlYVcA">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Tinu Abayomi-Paul</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Writing about digital marketing and other topics since 1998.</p>
        <p class="t-12 t-black--light t-normal">
          June 22, 2013, Tinu worked with Rohit in different groups
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember1314" class="ember-view">    <span class="lt-line-clamp__line">This is a recommendation for Rohit as a speaker. I am fresh from</span>
      <span class="lt-line-clamp__line">seeing him speak at Vocus' #Demand13. His talk on Likability was</span>
      <span class="lt-line-clamp__line">personable, informative, illuminating, and had practical tips and</span>
      <span class="lt-line-clamp__line">actions we could take in our real professional lives. It was a</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      Keynote caliber presentation, and always is, despite wh<span class="lt-line-clamp__ellipsis">...
            <a href="#" class="lt-line-clamp__more">See more</a>
        </span></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember1316" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/paolonagari/" id="ember1317" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl loaded" alt="Paolo Nagari" height="56" width="56" src="https://media.licdn.com/dms/image/C5103AQGztuKn-JGJHQ/profile-displayphoto-shrink_100_100/0?e=1569456000&amp;v=beta&amp;t=TlsWoM6H8bL2Y8OQR7ljZmkbydPU27l0QqivTC95zBU">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Paolo Nagari</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Intercultural Group Founder | Intercultural Intelligence® Expert | Keynote Speaker | Expat Coach</p>
        <p class="t-12 t-black--light t-normal">
          December 23, 2009, Paolo worked with Rohit but at different companies
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember1319" class="ember-view">    <span class="lt-line-clamp__line">I experienced Rohit’s perspicacious global vision on marketing at</span>
      <span class="lt-line-clamp__line">Ogilvy PR in London, where he invited me to give a guest lecture</span>
      <span class="lt-line-clamp__line">on Intercultural Intelligence for Georgetown University. I was</span>
      <span class="lt-line-clamp__line">deeply impressed by his scintillating clarity of thought on the social</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      media era and by his innate ability to translate the pers<span class="lt-line-clamp__ellipsis">...
            <a href="#" class="lt-line-clamp__more">See more</a>
        </span></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember1450" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/krishnade/" id="ember1451" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl loaded" alt="Krishna De" height="56" width="56" src="https://media.licdn.com/dms/image/C5103AQHNOX-f7dkrEw/profile-displayphoto-shrink_100_100/0?e=1569456000&amp;v=beta&amp;t=FodrpHO3qh1kg0pJKL9TCOml2v_bw5fhivYEX4dlvOo">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Krishna De</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Strategic Communications, Content Marketing, Talent and Organisation Development Strategist, Educator and Speaker</p>
        <p class="t-12 t-black--light t-normal">
          August 5, 2008, Krishna worked with Rohit but at different companies
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember1453" class="ember-view">    <span class="lt-line-clamp__line">In today's world of business and in an increasingly competitive</span>
      <span class="lt-line-clamp__line">global market place, how do you stand out from the crowd? That's</span>
      <span class="lt-line-clamp__line">exactly what you can learn from Rohit through his speaking, writing</span>
      <span class="lt-line-clamp__line">and consulting. Listen to Rohit's wise words then apply what he</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      teaches and you will ensure that your brand need never<span class="lt-line-clamp__ellipsis">...
            <a href="#" class="lt-line-clamp__more">See more</a>
        </span></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember1455" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/kenekaplan/" id="ember1456" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl loaded" alt="Ken Kaplan" height="56" width="56" src="https://media.licdn.com/dms/image/C5103AQFnmPEaA-DIXg/profile-displayphoto-shrink_100_100/0?e=1569456000&amp;v=beta&amp;t=CBoA9n5o44UEjwhMFOn3O48hT9RVecD9oTlevvYS82k">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Ken Kaplan</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Editorial Director at Nutanix</p>
        <p class="t-12 t-black--light t-normal">
          December 11, 2007, Ken worked with Rohit but at different companies
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember1458" class="ember-view">    <span class="lt-line-clamp__line">Rohit is a sage of social media -- a well-connected influencer who</span>
      <span class="lt-line-clamp__line">knows by doing and quickly understanding needs and real</span>
      <span class="lt-line-clamp__line">potential.  He's a skilled listener and a wellspring of creative ideas</span>
      <span class="lt-line-clamp__line">that are often novel yet practical.  Rohit has helped me and my</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      company try new things, break new ground and build n<span class="lt-line-clamp__ellipsis">...
            <a href="#" class="lt-line-clamp__more">See more</a>
        </span></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember1460" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/julieyork/" id="ember1461" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl loaded" alt="Julie York" height="56" width="56" src="https://media.licdn.com/dms/image/C5103AQGIazTpIbxxaQ/profile-displayphoto-shrink_100_100/0?e=1569456000&amp;v=beta&amp;t=FEihx3rJFAM5GqhXwy5jEOFWnVm7aLT2ULc1TU5mhTs">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Julie York</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">A human centred approach to Organisational, People and Technology Transformations.</p>
        <p class="t-12 t-black--light t-normal">
          May 10, 2006, Julie worked with Rohit but at different companies
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember1463" class="ember-view">    <span class="lt-line-clamp__line">I worked closely with Rohit, when he led the development of a</span>
      <span class="lt-line-clamp__line">major e-commerce website for a major client of ours. The website</span>
      <span class="lt-line-clamp__line">was developed by Dimension Data (Com Tech) with Rohhit as the</span>
      <span class="lt-line-clamp__line">key lead.  Rohit was always very professional and had no hesitation</span>
      <span class="lt-line-clamp__line lt-line-clamp__line--last">
      in doing what it took to keep the customer happy - oft<span class="lt-line-clamp__ellipsis">...
            <a href="#" class="lt-line-clamp__more">See more</a>
        </span></span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
</ul>
<!----></div>
</div></artdeco-tabpanel>
<artdeco-tabpanel aria-hidden="true" id="ember903" class="ember-view" role="tabpanel" aria-labelledby="ember890"><!---->
<div id="ember904" class="ember-view">          <div id="ember905" class="ember-view"><ul id="recommendation-list" class="section-info" tabindex="-1">
    <li id="ember906" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/hopefrank/" id="ember907" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl" alt="Hope Frank" height="56" width="56">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Hope Frank</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Futurist, Chief Marketing Officer, CXO of the Year 2017, 2018, Digital Expert, BOD Member, Evanta CMO Chairwoman SF/LA</p>
        <p class="t-12 t-black--light t-normal">
          September 29, 2012, Rohit was a client of Hope’s
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember909" class="ember-view">  <span class="lt-line-clamp__raw-line">Hope is easily one of the smartest people in the marketing industry - commanding the respect of both partners and employees.  While other CMOs may remain buried in data or only engage on a superficial level, her ability to extract brilliant digital insights and provide trusted counsel has always made her a go to partner for me and the Ogilvy team.  They always say every vendor should strive to be a partner instead of a provider ... Hope manages to do this so well it's almost like she is a part of our team despite the "minor" fact that she doesn't actually work for Ogilvy.  Highly recommended.

Rohit Bhargava 
SVP Global Strategy &amp; Planning 
Ogilvy &amp; Mather</span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
    <li id="ember910" class="pv-recommendation-entity ember-view"><div class="pv-recommendation-entity__header">
<a data-control-name="recommendation_details_profile" href="/in/serenateslerlomonaco/" id="ember911" class="pv-recommendation-entity__member ember-view">    <img class="lazy-image EntityPhoto-circle-4 fl" alt="Serena Tesler-LoMonaco" height="56" width="56">


    <div class="pv-recommendation-entity__detail">
      <h3 class="t-16 t-black t-bold">Serena Tesler-LoMonaco</h3>
      <p class="pv-recommendation-entity__headline t-14 t-black t-normal pb1">Senior Communications Professional</p>
        <p class="t-12 t-black--light t-normal">
          March 19, 2012, Rohit was senior to Serena but didn’t manage directly
        </p>
    </div>
</a></div>
<div class="pv-recommendation-entity__highlights">
  <blockquote class="pv-recommendation-entity__text relative">
      <div id="ember913" class="ember-view">  <span class="lt-line-clamp__raw-line">All the best communications professionals I know have a combination of passion and motivation -- and Serena has both.  When it comes to developing the right strategy for a client or doing the real work of achieving results, I highly recommend having Serena on your team!</span>

<!----><span class="lt-line-clamp__ellipsis lt-line-clamp__ellipsis--dummy">... <a class="lt-line-clamp__more" href="#">See more</a></span></div>

  </blockquote>
</div>
</li>
</ul>
  <div class="artdeco-container-card-action-bar">
    <div id="ember914" class="pv-profile-section__actions-inline ember-view"><button class="pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link" aria-controls="recommendation-list" aria-expanded="false">Show more
<li-icon aria-hidden="true" type="chevron-down-icon" class="pv-profile-section__toggle-detail-icon" size="small"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M8,9l5.93-4L15,6.54l-6.15,4.2a1.5,1.5,0,0,1-1.69,0L1,6.54,2.07,5Z" class="small-icon" style="fill-opacity: 1"></path></svg></li-icon></button>

<!----></div>
    <span class="visually-hidden">Show more</span>
  </div>
</div>
</div></artdeco-tabpanel></artdeco-tabs></div>
</section>

<section id="ember1072" class="pv-profile-section pv-accomplishments-section artdeco-container-card ember-view"><header class="card-header clearfix">
  <h2 class="card-heading t-20 t-black t-normal fl">Accomplishments</h2>

<!----></header>

<div id="ember1074" class="ember-view">    <section id="ember1075" class="accordion-panel pv-profile-section pv-accomplishments-block honors ember-view">
<h3 class="pv-accomplishments-block__count t-32 t-black t-normal pr3">
  <span class="visually-hidden">Rohit has 9 honors</span>
  <span>9</span>
</h3>

<div class="pv-accomplishments-block__content break-words">
  <h3 class="pv-accomplishments-block__title">Honors &amp; Awards</h3>

  <button aria-label="Expand honors &amp; awards section" aria-expanded="false" aria-controls="honors-expandable-content" id="ember1076" class="pv-accomplishments-block__expand artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--tertiary ember-view">  <li-icon aria-hidden="true" type="chevron-down-icon" class="artdeco-button__icon" size="small"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M8,9l5.93-4L15,6.54l-6.15,4.2a1.5,1.5,0,0,1-1.69,0L1,6.54,2.07,5Z" class="small-icon" style="fill-opacity: 1"></path></svg></li-icon>

<span class="artdeco-button__text">
    
</span></button>

  <div role="region" id="honors-expandable-content" tabindex="-1" class="pv-accomplishments-block__list-container">
      <ul class="pv-accomplishments-block__summary-list t-14 ">
          <li class="pv-accomplishments-block__summary-list-item">The AMA-Berry Marketing Book Prize Finalist: Non-Obvious 2018</li>
          <li class="pv-accomplishments-block__summary-list-item">The Eric Hoffer Book Award (Business Book Of The Year) - Non-Obvious 2018</li>
          <li class="pv-accomplishments-block__summary-list-item">INDIE Gold Medal: Best Business Book - Non-Obvious 2018</li>
          <li class="pv-accomplishments-block__summary-list-item">Top 100 Thought Leaders In Trustworthy Business Behaviour</li>
          <li class="pv-accomplishments-block__summary-list-item">Top 40 Strategists In Digital Marketing</li>
          <li class="pv-accomplishments-block__summary-list-item">Best Sales/Marketing Book of the Year Award - Shortlist</li>
          <li class="pv-accomplishments-block__summary-list-item">25 Digital Marketing Executives To Watch</li>
          <li class="pv-accomplishments-block__summary-list-item">Most Influential South Asian In Media &amp; Marketing</li>
          <li class="pv-accomplishments-block__summary-list-item">Gold Atticus Award</li>
      </ul>
  </div>
</div>
</section>
</div><div id="ember1078" class="ember-view">    <section id="ember1079" class="accordion-panel pv-profile-section pv-accomplishments-block publications ember-view">
<h3 class="pv-accomplishments-block__count t-32 t-black t-normal pr3">
  <span class="visually-hidden">Rohit has 3 publications</span>
  <span>3</span>
</h3>

<div class="pv-accomplishments-block__content break-words">
  <h3 class="pv-accomplishments-block__title">Publications</h3>

  <button aria-label="Expand publications section" aria-expanded="false" aria-controls="publications-expandable-content" id="ember1080" class="pv-accomplishments-block__expand artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--tertiary ember-view">  <li-icon aria-hidden="true" type="chevron-down-icon" class="artdeco-button__icon" size="small"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M8,9l5.93-4L15,6.54l-6.15,4.2a1.5,1.5,0,0,1-1.69,0L1,6.54,2.07,5Z" class="small-icon" style="fill-opacity: 1"></path></svg></li-icon>

<span class="artdeco-button__text">
    
</span></button>

  <div role="region" id="publications-expandable-content" tabindex="-1" class="pv-accomplishments-block__list-container">
      <ul class="pv-accomplishments-block__summary-list t-14 ">
          <li class="pv-accomplishments-block__summary-list-item">Non-Obvious 2018 Edition: How To Predict Trends And Win The Future (Non-Obvious Series)</li>
          <li class="pv-accomplishments-block__summary-list-item">Non-Obvious - How To Think Different, Curate Ideas &amp; Predict The Future</li>
          <li class="pv-accomplishments-block__summary-list-item">Likeonomics: The Unexpected Truth Behind Earning Trust, Influencing Behavior, and Inspiring Action</li>
      </ul>
  </div>
</div>
</section>
</div></section>

<section id="ember1257" class="pv-profile-section pv-interests-section artdeco-container-card ember-view"><h2 class="card-heading t-20 t-black t-normal">Interests</h2>

<ul class="pv-profile-section__section-info section-info display-flex justify-flex-start overflow-hidden">
    <li id="ember1259" class="pv-interest-entity pv-profile-section__card-item ember-view"><a href="/groups/2489713/" id="ember1261" class="pv-interest-entity-link ember-view">    <div id="ember1262" class="pv-interest-entity__logo company-logo ember-view"><img class="lazy-image pv-entity__logo-img EntityPhoto-square-4 loaded" alt="Independent Book Publishers Association-IBPA" src="https://media.licdn.com/dms/image/C4E07AQHjv98_q-dVLA/group-logo_image-shrink_92x92/0?e=1563818400&amp;v=beta&amp;t=NkM1dusluHpzq9R7SNeIobAFKv51VpnOr6jwC_cfCqg">
</div>
    <div id="ember1263" class="pv-entity__summary-info ember-view"><h3 class="pv-entity__summary-title t-16 t-black t-bold">
  <span class="pv-entity__summary-title-text">Independent Book Publishers Association-IBPA</span><!----></h3>
<p class="pv-entity__occupation t-14 t-black--light t-normal"></p>
<p class="pv-entity__follower-count t-14 t-black--light t-normal">5,035 members</p>
</div>
</a>
</li>
    <li id="ember1265" class="pv-interest-entity pv-profile-section__card-item ember-view"><a href="/groups/3719/" id="ember1267" class="pv-interest-entity-link ember-view">    <div id="ember1268" class="pv-interest-entity__logo company-logo ember-view"><img class="lazy-image pv-entity__logo-img EntityPhoto-square-4 loaded" alt="Emory University's Goizueta Business School" src="https://media.licdn.com/dms/image/C4E07AQGiBP7r6vZP3w/group-logo_image-shrink_92x92/0?e=1563818400&amp;v=beta&amp;t=10bybeF3GAn0359slMIPmrRvTuSgjkY6Q9KqmUEHcoo">
</div>
    <div id="ember1269" class="pv-entity__summary-info ember-view"><h3 class="pv-entity__summary-title t-16 t-black t-bold">
  <span class="pv-entity__summary-title-text">Emory University's Goizueta Business School</span><!----></h3>
<p class="pv-entity__occupation t-14 t-black--light t-normal"></p>
<p class="pv-entity__follower-count t-14 t-black--light t-normal">10,241 members</p>
</div>
</a>
</li>
    <li id="ember1271" class="pv-interest-entity pv-profile-section__card-item ember-view"><a data-control-name="interests_company_clicked" href="/company/3889/" id="ember1273" class="pv-interest-entity-link ember-view">    <div id="ember1274" class="pv-interest-entity__logo company-logo ember-view"><img class="lazy-image pv-entity__logo-img EntityPhoto-square-4 loaded" alt="Emory University" src="https://media.licdn.com/dms/image/C560BAQHU63E5TDuvZw/company-logo_400_400/0?e=1571875200&amp;v=beta&amp;t=HCzHwYkfOaKK7GM-RbebHCEJitCyPrh7jYcsSfsu1Lw">
</div>
    <div id="ember1275" class="pv-entity__summary-info ember-view"><h3 class="pv-entity__summary-title t-16 t-black t-bold">
  <span class="pv-entity__summary-title-text">Emory University</span><!----></h3>
<p class="pv-entity__occupation t-14 t-black--light t-normal"></p>
<p class="pv-entity__follower-count t-14 t-black--light t-normal">126,393 followers</p>
</div>
</a>
</li>
    <li id="ember1277" class="pv-interest-entity pv-profile-section__card-item ember-view"><a href="/groups/2183410/" id="ember1279" class="pv-interest-entity-link ember-view">    <div id="ember1280" class="pv-interest-entity__logo company-logo ember-view"><img class="lazy-image pv-entity__logo-img EntityPhoto-square-4 loaded" alt="CES" src="https://media.licdn.com/dms/image/C4E07AQGp1ytT6SxXNQ/group-logo_image-shrink_92x92/0?e=1563818400&amp;v=beta&amp;t=KZ7GnyEpmp8Clj0ykGMeuTTe4tDpJM7fFq8pgrPowqA">
</div>
    <div id="ember1281" class="pv-entity__summary-info ember-view"><h3 class="pv-entity__summary-title t-16 t-black t-bold">
  <span class="pv-entity__summary-title-text">CES</span><!----></h3>
<p class="pv-entity__occupation t-14 t-black--light t-normal"></p>
<p class="pv-entity__follower-count t-14 t-black--light t-normal">23,127 members</p>
</div>
</a>
</li>
    <li id="ember1283" class="pv-interest-entity pv-profile-section__card-item ember-view"><a data-control-name="interests_profile_clicked" href="/in/johnfwelch/" id="ember1285" class="pv-interest-entity-link ember-view">    <div id="ember1286" class="pv-interest-entity__logo people-logo ember-view"><img class="lazy-image pv-entity__logo-img EntityPhoto-circle-4 loaded" alt="Jack Welch" src="https://media.licdn.com/dms/image/C4D03AQEnLkMsVAS1OQ/profile-displayphoto-shrink_800_800/0?e=1569456000&amp;v=beta&amp;t=LJ6lWh0jxK_SAKoCZ0KsZVzslI2_TL224rE0ERNdItc">
</div>
    <div id="ember1287" class="pv-entity__summary-info ember-view"><h3 class="pv-entity__summary-title t-16 t-black t-bold">
  <span class="pv-entity__summary-title-text">Jack Welch</span><li-icon type="linkedin-influencer-color-icon" class="pv-interest-entity__influencer-icon" size="small" role="img" aria-label="Jack Welch is a LinkedIn Influencer"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><g class="small-icon" style="fill-opacity: 1">
        <path d="M15,1.25v11.5A1.25,1.25,0,0,1,13.75,14H4L1,16V1.25A1.25,1.25,0,0,1,2.25,0h11.5A1.25,1.25,0,0,1,15,1.25Z" style="fill: #0073b1;fill-rule: evenodd"></path>
        <path d="M4,1.68A1.36,1.36,0,0,0,2.69,3,1.36,1.36,0,0,0,4,4.31,1.36,1.36,0,0,0,5.31,3,1.36,1.36,0,0,0,4,1.68Z" style="fill: #fff"></path>
        <rect x="3" y="5" width="2" height="7" style="fill: #fff"></rect>
        <path d="M10.25,4.88a3,3,0,0,0-2.31,1H7.88V5H6v7H8V9c0-1.17.48-2,1.62-2C10.53,7,11,7.66,11,9v3h2V7.88C13,6,12.21,4.88,10.25,4.88Z" style="fill: #fff"></path>
      </g></svg></li-icon></h3>
<p class="pv-entity__occupation t-14 t-black--light t-normal">Executive Chairman, The Jack Welch Management Institute</p>
<p class="pv-entity__follower-count t-14 t-black--light t-normal">7,203,532 followers</p>
</div>
</a>
</li>
    <li id="ember1289" class="pv-interest-entity pv-profile-section__card-item ember-view"><a data-control-name="interests_company_clicked" href="/company/43579/" id="ember1291" class="pv-interest-entity-link ember-view">    <div id="ember1292" class="pv-interest-entity__logo company-logo ember-view"><img class="lazy-image pv-entity__logo-img EntityPhoto-square-4 loaded" alt="iStock" src="https://media.licdn.com/dms/image/C4E0BAQF5mQJ6sfliFA/company-logo_400_400/0?e=1571875200&amp;v=beta&amp;t=U13UEM0lFwiMgemuN6CHIXsyA1KfUWvtwD1D4hwodg0">
</div>
    <div id="ember1293" class="pv-entity__summary-info ember-view"><h3 class="pv-entity__summary-title t-16 t-black t-bold">
  <span class="pv-entity__summary-title-text">iStock</span><!----></h3>
<p class="pv-entity__occupation t-14 t-black--light t-normal"></p>
<p class="pv-entity__follower-count t-14 t-black--light t-normal">11,036 followers</p>
</div>
</a>
</li>
</ul>

<a data-control-name="view_interest_details" href="/in/rohitbhargava/detail/interests/" id="ember1294" class="pv-profile-section__card-action-bar artdeco-container-card-action-bar ember-view">    <span class="pv-profile-section__section-info" aria-hidden="true">See all</span>
    <span class="visually-hidden">See all following</span>
</a></section>

<a href="#" class="lt-line-clamp__more">see more</a>

<button class="pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link" aria-controls="recommendation-list" aria-expanded="false">Show more
<li-icon aria-hidden="true" type="chevron-down-icon" class="pv-profile-section__toggle-detail-icon" size="small"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M8,9l5.93-4L15,6.54l-6.15,4.2a1.5,1.5,0,0,1-1.69,0L1,6.54,2.07,5Z" class="small-icon" style="fill-opacity: 1"></path></svg></li-icon></button>'''
