from bs4 import BeautifulSoup
import re
import requests
import csv
#url = input("Enter a website to extract the URL's from: ")

r  = requests.get("http://www.thoughtco.com/capitals-of-every-independent-country-1434452")

data = r.text

soup = BeautifulSoup(data,"html.parser")
a=soup.find_all('ol')
country_list = []
capital_list = []

for f in a:
    for ele in f:
        ele = str(ele)
        country = re.search(r"<li>(.*?)-", ele)
        capital = re.search(r"-(.*)</li>", ele)
        country_list.append(country.group(1))
        capital_list.append(capital.group(1))
        print(country.group(1), capital.group(1))
with open('data.csv','w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow([str("Countries"),str("Capitals")])
    for point in range(len(country_list)):
        csvwriter.writerow([country_list[point],capital_list[point]])







