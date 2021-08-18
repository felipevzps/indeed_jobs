from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver")

# Getting today and time to save new files names 
today = time.strftime("%m%d%Y_%H:%M")
output = "EstagioDesigner_SP"

# Having problems to get job_desc
df = pd.DataFrame(columns=["Title","Location","Company","Salary","Rating", "Summary","Description"])

for i in range(0,110,10):
	# Check the link, it must start with 0 and go from 10 to 10
	# Every multiple of 10 is a page, e.g 0 = page 1, 10 = page 2 ...
	
	#Bioinformatics - Remote
	#driver.get('https://www.indeed.com/jobs?q=Bioinformatics&l=remote&start={}&vjk=d2b226b7af08c0da'.format(i))
	
	#Bioinformatics - United States
	#driver.get('https://www.indeed.com/jobs?q=Bioinformatics&l=United+States&start={}'.format(i))
	
	#Bioinformatics - United States - $70k+ - Biology - Entry Level
	#driver.get('https://www.indeed.com/jobs?q=Bioinformatics+%2470%2C000&l=United+States&explvl=entry_level&taxo1=HH9s9Yq9Tw28vEHiAAur0A&start={}'.format(i))
	
	#EstagioDesigner dudu
	driver.get('https://br.indeed.com/jobs?q=est%C3%A1gio+designer&l=S%C3%A3o+Paulo%2C+SP&start={}'.format(i))
	
	jobs = []
	driver.implicitly_wait(3000)
	# The each result appears in the class "<div class="jobsearch-SerpJobCard unifiedRow row result clickcard..."
	for job in driver.find_elements_by_class_name('result'):
		soup = BeautifulSoup(job.get_attribute('innerHTML'),'html.parser')
		
		try:
			title = soup.find(class_="title").text.replace("\n","").strip()
		except:
			title = 'None'

		try:
			company = soup.find(class_="company").text.replace("\n","").strip()
		except:
			company = 'None'

		try:
			rating = soup.find(class_="ratingsContent").text.replace("\n","").strip()
		except:
			rating = 'None'

		try:
			location = soup.find(class_="location").text
		except:
			location = 'None'

		try:
			salary = soup.find(class_="salary").text.replace("\n","").strip()
		except:
			salary = 'None'			
		
		sum_div = job.find_elements_by_class_name("title")[0]

		try:
			sum_div.click()
		except:
		
			cookie_button = driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']")
			cookie_button.click()
			sum_div.click()
		
		try:
			sum_div.click()
		except:
			close_button = driver.find_elements_by_class_name('popover-x-button-close')[0]
			close_button.click()
			sum_div.click()	

		try:
			job_desc = soup.find(class_="jobsearch-JobComponent-embeddedBody").text.replace("\n","").strip()
		except:
			job_desc = 'None'	

		try:
			summary = soup.find(class_="summary").text.replace("\n","").strip()
		except:
			summary = 'None'
	
		df = df.append({'Title':title,'Location':location,"Company":company,"Salary":salary,
						"Rating":rating, "Summary":summary, "Description": job_desc
                        },ignore_index=True)

		print("Got these many results:",df.shape)

df.to_csv("./data/" + output + ".csv",index=False)	
