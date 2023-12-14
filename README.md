Automated web scraping using Selenium and BeautifulSoup to extract job listings from [Indeed](https://www.indeed.com/). 

### Features
- Iterates through specified job URL pages and saves results in a CSV file
- Generates histograms depicting company, location, and keyword frequencies from job summaries

### Instalation
```bash
git clone https://github.com/felipevzps/indeed_jobs.git

cd indeed_jobs

# Create indeed_jobs environment with conda
conda env create -f environment.yml
```

### Usage
```
usage: get_jobs.py [-h] --url 'URL' --end PAGES --out OUTPUT_NAME

Automated web scraping using Selenium and BeautifulSoup to extract job listings from Indeed.

options:
  -h, --help         show this help message and exit
  --url 'URL'          URL pattern for web scraping with a {} placeholder
  --end PAGES        Last page for iteration
  --out OUTPUT_NAME  Output name <save on data/>
```

### Example
Just replace the page number with {} (`start={}`). 

```
./get_jobs.py --url 'https://www.indeed.com/jobs?q=bioinformatics&l=Remote&sc=0kf%3Aattr%28DSQF7%29%3B&start={}&vjk=f4a3f4c434b0c649' --end 20 --out Bioinformatics_Remote_2pages
```

> **Note:** Make sure to download the appropriate ChromeDriver version that matches your Google Chrome installation. For the correct version, visit the [ChromeDriver downloads page](https://chromedriver.chromium.org/downloads).
> ```bash
> google-chrome --version
> Google Chrome 119.0.6045.199
> 
> ./chromedriver --version
> ChromeDriver 119.0.6045.105 
> ```

### Data Visualization
```
usage: data_visualization.py [-h] --i data/OUTPUT_NAME

A script to generate histograms from Indeed job listings.

options:
  -h, --help            show this help message and exit
  --i data/OUTPUT_NAME  Output name <saved on data/>
```

### Example
```
./data_visualization.py --i bioinformatics_US.csv
```

#### Companies
![JobCompanies_BioinformaticsUS](https://github.com/felipevzps/indeed_jobs/blob/main/plot/JobCompanies_BioinformaticsUS.png)

#### Locations
![JobLocation_BioinformaticsUS](https://github.com/felipevzps/indeed_jobs/blob/main/plot/JobLocation_BioinformaticsUS.png)

#### Keyword Frequency
![KeywordFrequency_BioinformaticsUS](https://github.com/felipevzps/indeed_jobs/blob/main/plot/KeywordFrequency_BioinformaticsUS.png)
