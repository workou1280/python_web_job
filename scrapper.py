import requests
from bs4 import BeautifulSoup

def get_last_page(url):
   result = requests.get(url)
   soup = BeautifulSoup(result.text,"html.parser")
   s_pagination = soup.find("div", {"class":"s-pagination"}).find_all("a")
   last_page = s_pagination[-2].get_text().strip()
   return int(last_page)

def extract_job(html):
  title = html.find("h2",class_="mb4").find("a", class_="s-link")["title"]
  company = html.find("h3",class_="fc-black-700").find("span").get_text().strip()
  location = html.find("h3",class_="fc-black-700").find("span", class_="fc-black-500").get_text().strip()
  id = html["data-jobid"]
  return {
          "title": title,
          "company": company,
          "location": location,
          "link": f"https://stackoverflow.com/jobs/{id}" 
         }
  
def extract_jobs(last_page,url):
  jobs = []
  for page in range(last_page):
      print(f"Scrapping so page {page + 1}")
      result = requests.get(f"{url}&pg={page + 1}")
      soup = BeautifulSoup(result.text, "html.parser")
      divs = soup.find_all("div", {"class": "-job"})
      for div in divs:
          job = extract_job(div)
          jobs.append(job)
  return(jobs)

def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page,url)
  return jobs