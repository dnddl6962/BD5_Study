from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

 

"""def get_page_count(keyword):
  
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)

  base_url="https://indeed.com/jobs?q="
  browser.get(f"{base_url}{keyword}")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", class_="css-jbuxu0 ecydgvn0")
  if pagination == None:
    return 1
  pages = pagination.find_all("div", class_="css-tvvxwd ecydgvn1")
  count = len(pages)
  if count >= 5:
    return 5
  else:
    return count"""



def extract_indeed_jobs(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)
  """pages = get_page_count(keyword)
  print("Found", pages, "page")"""
  results = []
  #for page in range(pages):  
  base_url="https://indeed.com/jobs?q="
  final_url = f"{base_url}{keyword}"
  browser.get(final_url)
    
  soup = BeautifulSoup(browser.page_source, "html.parser")
  job_list = soup.find("ul", class_="jobsearch-ResultsList")
  jobs = job_list.find_all("li", recursive=False)
    
  for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
      anchor = job.select_one("h2 a") #h2 밑에 a를 찾는다
      company = job.find("span", class_="companyName")
      location = job.find("div", class_="companyLocation")
      title = anchor['aria-label']
      link = anchor['href']
      job_data = {
        'link':f"https://www.indeed.com{link}",
        'company':company.string.replace(',', ' '),
        'location':location.string,
        'position':title.replace(',', ' ')
      }
      results.append(job_data)
  return results      


