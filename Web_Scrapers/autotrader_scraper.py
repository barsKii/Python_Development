#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas
import requests
from bs4 import BeautifulSoup

base_url = "https://www.autotrader.co.nz/used-cars-for-sale/mazda-bongo"
r = requests.get(base_url)
c = r.content
soup = BeautifulSoup(c, "html.parser")
page_num = int(soup.find("li", {"class":"no-border"}).text.split(' ', 3)[2]) + 1
l = []
for page in range(1, page_num):
    print(base_url + "?page=" + str(page))
    r = requests.get(base_url + "?page=" + str(page))
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div",{"class":"list-item"})

    for item in all:
        #Setup Code
        d = {}
        title = item.find("a").text
        features = item.find("ul", {"class":"features"})
        features = features.find_all("li")

        #Code adding pairs to dictionary
        d["Make"] = title.split(' ', 2)[1]
        d["Model"] = title.split(' ', 2)[2]
        d["Year"] = title.split(' ', 1)[0]
        d["Price"] = item.find("p", {"class":"price"}).text.replace(" ","")
        d["KMs"] = features[0].text
        d["Colour"] = features[1].text.split(' ', 1)[0]
        d["CC"] = features[2].text.split(' ', 1)[0]
        try:
            d["Transmition"] = features[2].text.split(' ', 1)[1]
        except:
            d["Transmition"] = "None"
        try:
            d["Fuel"] = features[3].text  
        except:
            d["Fuel"] = "None"
        d["Dealer"] = item.find("p", {"class":"dealer"}).text.split(' ', 1)[0].replace(",","")
        d["Location"] = item.find("p", {"class":"dealer"}).text.split(' ', 1)[-1].replace(",","").replace("Seller ","").title()

        l.append(d)

df = pandas.DataFrame(l)

df.to_csv("AT_BONGO.csv")





