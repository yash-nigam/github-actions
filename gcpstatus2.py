import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date

URL = "https://status.cloud.google.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find('table', class_='main-dashboard-table')
table_body = table.find('tbody')
rows = table_body.findAll('tr', class_='product-row')
services_status_list = []
for row in rows:
    product_name = row.find('td', 'product-name')
    multi_tags = row.select('td:nth-of-type( 9 )')
    service_status = ""
    for x in multi_tags:
        if "status-icon available" in str(x):
            service_status = "available"
        elif "status-icon disruption" in str(x):
            service_status = "disruption"
    services_status_list.append([product_name.find(text=True), service_status, str(date.today())])

print(services_status_list)
pd.DataFrame(services_status_list).to_excel("service_status.xlsx",
                                            header=["service_name",
                                                    "status",
                                                    "last_refresh_date"],
                                            index=False)
