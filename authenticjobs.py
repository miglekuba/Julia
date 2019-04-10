import requests
import json


job_type = input("Do you want a 'Full-time' or 'Part-time' job? ")
job_category = input("Which area of tech do you want to work in? ")


url = 'https://authenticjobs.com/api/?api_key=06f00d616c49796aea5dcc0f1e89b4fa&method=aj.jobs.search&keywords=Startup,Apps,{}&perpage=1&format=json'.format(job_type, job_category)


response = requests.get(url)
listings = response.json()

print(listings['listings'])
