from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_job_details(div):
    
    
    try:
        job_key = div.find_element(By.CSS_SELECTOR, 'h2.jobTitle a').get_attribute('id')
        job_key = job_key.replace('job_', '')
    except NoSuchElementException:
        job_key = None
    try:
        job_title = div.find_element(By.CSS_SELECTOR, 'h2.jobTitle').text.strip()
    except NoSuchElementException:
        job_title = None
    try:
        company_name = div.find_element(By.CSS_SELECTOR, 'span.companyName').text.strip()
    except NoSuchElementException:
        company_name = None
    try:
        location = div.find_element(By.CLASS_NAME, 'companyLocation').text.strip()
    except NoSuchElementException:
        location = None
    try:
        salary = div.find_element(By.CLASS_NAME, 'metadata.salary-snippet-container').text.strip()
    except NoSuchElementException:
        salary = None

    try:
        job_description = div.find_element(By.CSS_SELECTOR, 'div.job-snippet ul').text.strip()
    except NoSuchElementException:
        job_description = None
                
            
    
    job_data = {
                "reference": job_key,
                "name": job_title,
                "sections": [
                    {
                        "name": "description",
                        "title": "Description du poste",
                        "description": job_description
                    },
                    {
                        "name": "profile_background",
                        "title": "Profil cherché",
                        "description": None
                    }
                ],
                "skills": [], 
                "tags": [
                    {"name": "salary_expectation", "value": salary}, 
                    {"name": "company", "value": company_name}, 
                    {"name": "location", "value": location}  
                ]
            }
    
    return job_data