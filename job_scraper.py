import requests
from bs4 import BeautifulSoup

# job criteria
desired_job_title = "Cleaning"
desired_location = "Brainerd, MN"

url = https://www.indeed.com/l-brainerd,+mn-jobs.html?vjk=3c1b76a2fc60c7e9

response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('div', class_='job-listing')

    for job in job_listings:
        # Extract the job title and location (this is an example, adjust to the site's HTML structure)
        job_title = job.find('h2', class_='job-title').text.strip()
        job_location = job.find('span', class_='job-location').text.strip()

        # Check if the job matches your criteria
        if desired_job_title.lower() in job_title.lower() and desired_location.lower() in job_location.lower():
            print(f"Job Title: {job_title}")
            print(f"Location: {job_location}")
            print(f"Link: {job.find('a')['href']}")
            print("-" * 40)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")