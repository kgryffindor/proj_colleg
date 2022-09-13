
from bs4 import BeautifulSoup as bs
import os
import re# import module
import codecs
from time import sleep, time
from turtle import update
from bs4 import BeautifulSoup
import requests
import webbrowser
# to open/create a new html file in the write mode
f = open('main.html', 'w')
url1 ="https://cyware.com/cyber-security-news-articles"
page = requests.get(url1)


soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('section',class_="cy-content-section")
for list in  lists:
    title = list.find('h1',class_="cy-card__title m-0 cursor-pointer pb-3").text
    info= title.strip()
    print(info)
#https://youtu.be/Hi3WkiVzld0

base = os.path.dirname(os.path.abspath(__file__))
  
# Open the HTML in which you want to make changes
html = open(os.path.join(base, 'main.html'))
  
# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')
  
# Give location where text is 
# stored which you wish to alter
old_text = soup.find("p", {"id": "para"})
a = (old_text)
print(a)
# Replace the already stored text with 
# the new text which you wish to assign
new_text = old_text.find(text=re.compile(a
)).replace_with('GHANSHYAM MAHARAJ NI JAI')
  
# Alter HTML file to see the changes done
with open("main.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.linuxtoday.com/news/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
getvL = (soup.h3).text

print(getvL)



# Making a GET request
r = requests.get('https://www.wired.com/tag/programming/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
getvaL = (soup.h3).text

print(getvaL)

html_content = f"""
<html><head>
  
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
    <title>Tech News</title>
</head>
<body class="w-full h-screen bg-no-repeat bg-cover "style="background-image:linear-gradient(rgba(4,9,30,0.7),rgba(4,9,30,0.7)),url('grr.jpg')"></body>
  <header class="text-gray-600 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        
        <span class="ml-3 text-xl">Tech news</span>
      </a>
     <nav class="md:ml- flex flex-wrap items-center text-green-200 justify-center">
     
      <a href="home.html" class="mr-5 hover:text-gray-100 link link-underline link-underline-blue text-blue">Home</a>
      <a href="contact.html" class="mr-5 hover:text-gray-100 link link-underline link-underline-blue text-blue">Contact Us</a>
      <a href="signup.html" class="mr-5 hover:text-gray-100 link link-underline link-underline-blue text-blue">Sign Up</a>


         


<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-wrap -m-4">
      <div class="p-4 md:w-1/3">
        <div class="h-full border-2 border-gray-200 border-opacity-60 rounded-lg overflow-hidden">
          <img class="lg:h-48 md:h-36 w-full object-cover object-center" src="C:\\Users\\steve\\OneDrive\\Desktop\\tech\\cy.jpg" alt="blog">
          <div class="p-6">
            
            <h1 class="title-font text-lg font-medium text-gray-200 mb-3">Cyber Security</h1>
            <p class="leading-relaxed text-gray-200  mb-3">{info},khudgabar</p>
            <div class="flex items-center flex-wrap ">
            <a href="https://cyware.com/cyber-security-news-articles" class="mr-5 hover:text-gray-100 link link-underline link-underline-blue text-blue">Learn more</a>


              
                <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path d="M12 5l7 7-7 7"></path>
                </svg>
              </a>
              
              <span class="text-gray-400 inline-flex items-center leading-none text-sm">
                
              </span>
            </div>
          </div>
        </div>
      </div>
      <div class="p-4 md:w-1/3">
        <div class="h-full border-2 border-gray-200 border-opacity-60 rounded-lg overflow-hidden">
          <img class="lg:h-48 md:h-36 w-full object-cover object-center" src="C:\\Users\\steve\\OneDrive\\Desktop\\tech\\yc.jpg" alt="blog">
          <div class="p-6">
            
            <h1 class="title-font text-lg font-medium text-gray-200 mb-3">Linux</h1>
            <p class="leading-relaxed text-gray-200 mb-3">{getvL}</p>
            <div class="flex items-center flex-wrap">
              <a href="https://www.linuxtoday.com/news/" class="mr-5 hover:text-gray -100 link link-underline link-underline-blue text-blue">Learn more</a>
             
                <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path d="M12 5l7 7-7 7"></path>
                </svg>
              </a>
             
              <span class="text-gray-400 inline-flex items-center leading-none text-sm">
              
              </span>
            </div>
          </div>
        </div>
      </div>
      <div class="p-4 md:w-1/3">
        <div class="h-full border-2 border-gray-200 border-opacity-60 rounded-lg overflow-hidden">
          <img class="lg:h-48 md:h-36 w-full object-cover object-center" src="C:\\Users\\steve\\OneDrive\\Desktop\\tech\\ab.jpg" alt="blog">
          <div class="p-6">
            
            <h1 class="title-font text-lg font-medium text-gray-200 mb-3">Software and programming</h1>
            <p class="leading-relaxed text-gray-200 mb-3">{getvaL}</p>
            <div class="flex items-center flex-wrap ">
              <a href="https://www.wired.com/tag/programming/" class="mr-5 hover:text-gray -100 link link-underline link-underline-blue text-blue">Learn more</a>
             
                <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path d="M12 5l7 7-7 7"></path>
                </svg>
              </a>
              
              <span class="text-gray-400 inline-flex items-center leading-none text-sm"></span>
                
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</body>
</html>
"""
f.write(html_content)

f.close()

file = codecs.open("main.html", 'r', "utf-8")
print(file.read())





