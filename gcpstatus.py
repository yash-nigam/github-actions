import os
import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://status.cloud.google.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("tbody")
services = results.find_all("tr", class_="product-row")

s=[]
for service in services:
  service_name=service.find("td",class_="product-name").text
  service_status=service.find("a",class_="status-icon")["class"][1]
  s.append([service_name,service_status,''])

#print(s)
pd.DataFrame(s).to_excel("service_status.xlsx",header=["service_name","status","last_refresh_date"],index=False)
