Automated web scraping using Selenium and BeautifulSoup to extract job listings from Indeed. 

### Features
- Iterates through specified job URL and saves results in a CSV file.
- Generates histograms depicting company, location, and keyword frequencies from job summaries.

### Usage

```
usage: get_jobs.py [-h] --url URL --end PAGES --out OUTPUT_NAME

Automated web scraping using Selenium and BeautifulSoup to extract job listings from Indeed.

options:
  -h, --help         show this help message and exit
  --url URL          URL pattern for web scraping with a {} placeholder
  --end PAGES        Last page for iteration
  --out OUTPUT_NAME  Output name <save on data/>
```

### Examples 

Just replace the page number with {} (`start={}`). 

```
./get_jobs.py --url 'https://www.indeed.com/jobs?q=bioinformatics&l=Remote&sc=0kf%3Aattr%28DSQF7%29%3B&start={}&vjk=f4a3f4c434b0c649' --end 20 --out Bioinformatics_Remote_2pages
```

#### Companies

![JobCompanies_BioinformaticsUS](https://github.com/felipevzps/indeed_jobs/blob/main/plot/JobCompanies_BioinformaticsUS.png)

#### Locations

![JobLocation_BioinformaticsUS](https://github.com/felipevzps/indeed_jobs/blob/main/plot/JobLocation_BioinformaticsUS.png)

#### Keyword Frequency
![KeywordFrequency_BioinformaticsUS](https://github.com/felipevzps/indeed_jobs/blob/main/plot/KeywordFrequency_BioinformaticsUS.png)
