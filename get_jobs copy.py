from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver")

# Getting today and time to save new files names 
today = time.strftime("%m%d%Y_%H:%M")
output = 'EstagioDesigner_BR'

# Having problems to get job_desc
df = pd.DataFrame(columns=["Title","Location","Company","Salary","Rating", "Summary","Description"])

for i in range(0,200,10):
	# Check the link, it must start with 0 and go from 10 to 10
	# Every multiple of 10 is a page, e.g 0 = page 1, 10 = page 2 ...
	#Tibia
	#driver.get('https://www.tibia.com/charactertrade/?subtopic=pastcharactertrades&filter_profession=5&filter_levelrangefrom=0&filter_levelrangeto=0&filter_world=&filter_worldpvptype=9&filter_worldbattleyestate=1&filter_skillid=1&filter_skillrangefrom=90&filter_skillrangeto=0&order_column=101&order_direction=1&currentpage={}'.format(i))
	
	#Bioinformatics - Remote
	#driver.get('https://www.indeed.com/jobs?q=Bioinformatics&l=remote&start={}&vjk=d2b226b7af08c0da'.format(i))
	
	#Bioinformatics - United States
	#driver.get('https://www.indeed.com/jobs?q=Bioinformatics&l=United+States&start={}'.format(i))
	
	#Bioinformatics - United States - $70k+ - Biology - Entry Level
	#driver.get('https://www.indeed.com/jobs?q=Bioinformatics+%2470%2C000&l=United+States&explvl=entry_level&taxo1=HH9s9Yq9Tw28vEHiAAur0A&start={}'.format(i))
	
	#dudu estágio designer
	driver.get('https://br.indeed.com/jobs?q=est%C3%A1gio+designer&l=Brasil&start={}'.format(i))

	jobs = []
	driver.implicitly_wait(1000)
	# The each result appears in the class "<div class="jobsearch-SerpJobCard unifiedRow row result clickcard..."
	# Im getting the attributes from the class wich have "result" in it
	for job in driver.find_elements_by_class_name('TableContentContainer'):# and driver.find_elements_by_id('vjs-container'):
		soup = BeautifulSoup(job.get_attribute('innerHTML'),'html.parser')
		try:
			name = soup.find(class_="AuctionCharacterName").text.replace("\n","").strip()
		except:
			title = 'None'

		print(name)	
		#df = df.append({'Title':title,'Location':location,"Company":company,"Salary":salary,
		#				"Rating":rating, "Summary":summary, "Description": job_desc
        #                },ignore_index=True)

		#print("Got these many results:",df.shape)


df.to_csv("./data/" + output + ".csv",index=False)	
