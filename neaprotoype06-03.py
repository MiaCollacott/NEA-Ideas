
import requests
from bs4 import BeautifulSoup
import re
import sqlite3
import random


#database stuff
conn = sqlite3.connect('access.db')
conn.execute("""CREATE TABLE PROPERTIES 
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            ACCESS_DETAILS TEXT NOT NULL,
            URL TEXT NOT NULL)""")


URL = input("Enter an English Heritage URL: ")
url_for_table = URL
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
title = soup.find('title')


#was find_all but that also returned details about roof access
for strong_tag in soup.find('strong',string=re.compile(r'Access')):
    p_tag = strong_tag.find_parent('p')
    # Remove HTML tags and print the text content on a single line
    text_content = p_tag.get_text(separator="", strip=True)
    title = title.get_text(separator="",strip=True)
    print(text_content)
    numid = random.randint(0, 100)
    conn.execute("INSERT INTO PROPERTIES (ID, NAME, ACCESS_DETAILS, URL) VALUES (?, ?, ?, ?)",
                   (numid, title, text_content,url_for_table ))
    conn.commit()

