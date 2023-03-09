# This file scrapes reddit to find top 10 reddit post and put together
# their titles and url in a csv file.

from bs4 import BeautifulSoup
import requests
import csv 

scrape_page = requests.get("https://www.reddit.com/top/")
soup = BeautifulSoup(scrape_page.text, "html.parser")

write_file = open("top_reddit.csv", "w")
writer = csv.writer(write_file)

writer.writerow(["TITLE", "URL"])
posts = soup.find_all("h3", attrs = {"class": "_eYtD2XCVieq6emjKBH3m"},limit=10)
links = soup.find_all("a", attrs = {"class": "SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE", "data-click-id":"body"}, limit = 10)

for post,link in zip(posts,links):
    writer.writerow([post.text, "https://www.reddit.com/" + link['href']])

write_file.close()

