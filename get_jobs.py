from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd 
from bs4 import BeautifulSoup
import time

service = Service(executable_path='./chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#driver = webdriver.Chrome("./chromedriver", options=options)

# Getting today and time to save new files names 
today = time.strftime("%m%d%Y_%H:%M")
output = "Bioinformatics_Remote_December"

# Columns
df = pd.DataFrame(columns=["Title", "Location", "Company", "Salary", "Summary"])

for i in range(0,90,10):
    
	'''
 	Check the link before running, $i must start with 0 and increases by 10
	Every multiple of 10 is a page, (e.g 0 = page 1, 10 = page 2 ...)
 	'''
	
 	#Bioinformatics - Remote
 	#driver.get('https://www.indeed.com/jobs?q=Bioinformatics&l=remote&start={}&vjk=d2b226b7af08c0da'.format(i))
    
    # Bioinformatics, remote november
	#driver.get('https://www.indeed.com/jobs?q=Bioinformatics&l=remote&start={}&pp=gQAPAAAAAAAAAAAAAAACGIfb6gASAQEBCC00UWI2Nj68A0UMyPfCAAA&vjk=adbce905d0ea898e'.format(i))
    # Bioinformatics, remote december
	driver.get('https://www.indeed.com/jobs?q=bioinformatics&l=Remote&sc=0kf%3Aattr%28DSQF7%29%3B&start={}&vjk=f4a3f4c434b0c649'.format(i))
	jobs = []
    
	driver.implicitly_wait(100)
	
 	# Each result appears in the class "<div class="job_seen_beacon"
	for job in driver.find_elements(By.CLASS_NAME,'job_seen_beacon'):
		soup = BeautifulSoup(job.get_attribute('innerHTML'),'html.parser')
		
		#title
		try:
			title = soup.find(class_="jobTitle").text.replace("\n","").strip()
		except:
			title = 'None'

		#location
		try:
			location = soup.find(class_="css-t4u72d eu4oa1w0").span.text.strip()
		except:
			location = 'None'
   
		#company
		try:
			company = soup.find(class_="css-1x7z1ps eu4oa1w0").text.strip()
		except:
			company = 'None'

		#salary
		try:
			salary_element = soup.find("div", {"data-testid": "attribute_snippet_testid"})
			salary = salary_element.text.strip()
		except:
			salary = 'None'		

		#summary 
		try:
			summary = soup.find(class_="job-snippet").find("li").text.replace("\n","").strip()
		except:
			summary = 'None'

  		#### cookie button ####
  
		#sum_div = job.find_elements_by_class_name("title")[0]

		#try:
			#cookie_button.click()
		#except:
			#cookie_button = driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']")
			#cookie_button.click()
			#sum_div.click()
		
		#try:
			#close_button.click()
			#sum_div.click()
		#except:
			#close_button = driver.find_elements_by_class_name('popover-x-button-close')[0]
			#close_button.click()
			#sum_div.click()	
   
		#### cookie button ####
		
		df = df.append({"Title":title, "Location":location, "Company":company, "Salary":salary, "Summary": summary}, ignore_index=True)

		print("Got these many results:", df.shape)

df.to_csv("./data/" + output + ".csv", index=False)