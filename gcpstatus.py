import os
import requests
from bs4 import BeautifulSoup


URL = "https://status.cloud.google.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("tbody")
services = results.find_all("tr", class_="product-row")

for service in services:
  product_name=service.find("td",class_="product-name")
  product=service.find("a",class_="status-icon")
  product_class=product["class"]
  product_status=" ".join(product_class[1:])
  print(product_name.text,product_status)
