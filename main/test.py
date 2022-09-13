# Python program to modify HTML
# with the help of Beautiful Soup
  
# Import the libraries 
from bs4 import BeautifulSoup as bs
import os
import re
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup as bs
import webbrowser
import os
import re
########################################################################################################
url1 ="https://cyware.com/cyber-security-news-articles"
page = requests.get(url1)


soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('section',class_="cy-content-section")
for list in  lists:
    title = list.find('h1',class_="cy-card__title m-0 cursor-pointer pb-3").text
    info= title.strip()
    print(info)


r = requests.get('https://www.linuxtoday.com/news/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
getvL = (soup.h3).text

print(getvL)


r = requests.get('https://www.wired.com/tag/programming/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
getvaL = (soup.h3).text

print(getvaL)
###############################################################################################################

# Remove the last segment of the path
base = os.path.dirname(os.path.abspath(__file__))
  
# Open the HTML in which you want to make changes
html = open(os.path.join(base, "C:\\Users\\steve\\OneDrive\\Desktop\\tech\\main\\main.html"))
  
# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')
  
# Give location where text is 
# stored which you wish to alter
old_text = soup.find("p", {"id": "para"})
a = (old_text).text
print(a)

new_text = old_text.find(text=re.compile(a)).replace_with(info)
print('change applied')
##########################################################################################################3
old_text = soup.find("p", {"id": "gval"})
a = (old_text).text
print(a)

new_text = old_text.find(text=re.compile(a)).replace_with(getvL)
print('change applied')
############################################################################################################3
old_text = soup.find("p", {"id": "gtval"})
a = (old_text).text
print(a)

new_text = old_text.find(text=re.compile(a)).replace_with(getvaL)
print('change applied')












# Alter HTML file to see the changes done
with open("C:\\Users\\steve\\OneDrive\\Desktop\\tech\\main\\main.html", "wb") as f_output:
    f_output.write(soup.prettify("UTF-8"))
    #webbrowser.open('main.html')