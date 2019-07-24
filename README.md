# Jobin
### Advanced Company Profiling using Machine Learning
______________________________________________________________________________

Jobin uses a candidate’s publicly accessible personal and professional data to give insights about whether he/she will be suitable to work in a company. It actually compares a person’s personality and professionality with the already existing employees of a company which may suggest the candidate whether it is good for him/her to work for the company.


It essentially provides the company and the user, a company index to know about the work culture, structure, skill sets,and mindsets for
the company.

##### So, use Jobin to know about the company you have been dreaming to work to!

Jobin uses the basis of the Problem Statement of Friend Affinity Finder to suggest a user whether its suitable for him/her to work for a particular company based on a comparison with the work culture, skill sets, mindsets of the already working employees.
Jobin essentially uses the IBM Watson’s Personality Insights Service to gather personal and professional information about a candidate and already employed people from the publicly accessible data available. 
Jobin classifies a user on suitability using Decision Trees which are trained by the data of already employed people.


## Steps to use:
1. Clone the repository or download it into your system.
2. Extract all the files present in compressed format and move into the directory of Friend_Affinity_Finder\Friend_Affinity_Finder\Friend_Affinity
3. Run the python script manage.py in your terminal as "*python manage.py runserver*"
4. The Web App launches where it will be asked to either company info or a users.
5. For companies entering their info, they need to go to the company registration page, where they will input the details about their copany and then they need to provide details about the social media handles of their employees as asked. After submitting all these data, the company index will be displayed which is a standardised score based on their employee data.
6. When a company succesfully registers itself into the application, then only its data can be used by any aspiring candidate.
7. For a candidate's search, they need to go to the user's page from the home page, and then provide the details about them and name of the company they are looking upon, after providing all details, the user's personality, professionality, suitability status and suitability index is shown which suggests whether he/she is suitable for the job.


### Packages need to be installed before running the application
##### Run the following commands in your terminal with administrator access
- *pip install selenium*
- *pip install python-bs4*
- *pip install sqllite*
- *pip install tweepy*
- *pip install ibm-watson*
- *pip install google-api-python-client*
- *pip install db-sqllite3*
- *pip install gspread*
- *pip install numpy*
- *pip install scipy*
- *pip install matplotlib*
- *pip install scikit-learn*
- *pip install pandas*

**For using the selenium framework, you should have Google Chrome Web Browser installed in your system, furthermore download the following (ChromeDriver) in your application's directiory to run it successfully::**
(For Chrome)http://chromedriver.chromium.org/downloads


For viewing the documentation, go to idea.docx
For viewing the project presentation go to jobin presentation.pdf
For viewing the undertaking document go to undertaking.docx
For viewing the Python Codes used go to Python Codes
For viewing the Web Applcation's codes used go to Friend_Affinity_FinderV2.0


//This project was made by Team The BitLords in participating in IBM Hack Challenge 2019, with the Problem Statement of Friend Affinity Finder
