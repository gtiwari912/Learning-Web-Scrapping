import requests   #if not installed, installed it by "pip install requests"
from bs4 import BeautifulSoup #if not installed, installed it by "pip install bs4"
import lxml # if not installed, installed it by "pip install lxml"
import re

# we are going to scrape the search result page of "Best dsa resource"
# Lets inspect the page and try to find the pattern which characterises every video
# we observed that every video is in div class as characterized by div class = "style-scope ytd-video-renderer"


#getting the whole html page as a text
html = requests.get("https://www.youtube.com/results?search_query=best+dsa+courses")

soup = BeautifulSoup(html.text, "lxml")  
#lxml is a tree parser builder, bcoz youtube is a complex website thats why we are using lxml parser, it builds tree like structure

#seeing the html text, by writing all the html text in data.txt file
# with open("data.txt", "w", encoding="utf-8") as output:
#     output.write(soup.prettify())



# we will try to convert the information in form of JSON so that we can access information easily
#since data is stored in scripts, and there is lot of data... so for now we are just getting first 33 videos data
script_data = soup.find_all("script")[33]  

#trying to extract the important part of data, we observed that important part starts from text "var ytInitialData = "
html_text = re.search("var ytInitialData = (.+)[,;]{1}",script_data.text).group(1)
with open("data.txt", "w", encoding="utf-8") as output:
    output.write(html_text)


