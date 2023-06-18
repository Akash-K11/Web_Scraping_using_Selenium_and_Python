from bs4 import BeautifulSoup
import requests
import time
import json


def find_jobs_quantbox():
    html_text = requests.get('https://www.quantboxresearch.com/jobs').text
    final_data = list()
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='job-item')

    for index, job in enumerate(jobs):
        job_name = job.find('h3', class_='job-title').text.strip()
        location = job.find('div', class_='job-sub-title').find('small').text.strip()
        job_link = job.h3.a['href']
        final_data.append({
            "Job Title": job_name.strip(),
            "Location": location.strip(),
            "Job ID": "https://www.quantboxresearch.com"+job_link.strip()
        })

    json_data = json.dumps({"company": "quantbox", "data": final_data})
    print(json_data)


if __name__ == '__main__':
    while True:
        find_jobs_quantbox()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
