from bs4 import BeautifulSoup   #importing Soup module
import re       #importing regex
import requests #importing requests library
import csv      #importing csv library
#url = input("Enter a website to extract the URL's from: ")  #optional code to input website name

r  = requests.get("http://www.thoughtco.com/capitals-of-every-independent-country-1434452")  

data = r.text #converting the raw info of the website link to text

soup = BeautifulSoup(data,"html.parser")
a=soup.find_all('ol')  #finding all of the ordered list links
country_list = []  #list to have country names
capital_list = []   #list to have capital names

for f in a:  #iterating for <ol> link
    for ele in f:   #iterating for the <li> link
        ele = str(ele) #converting data to string
        country = re.search(r"<li>(.*?)-", ele)   #extracting country name for eg: "Afghanistan: from <li> Afghanistan - kabul </li>" 
        capital = re.search(r"-(.*)</li>", ele)    #extracting country name for eg: "Kabul: from <li> Afghanistan - kabul </li>"
        country_list.append(country.group(1))   #appending the respective data to the lists
        capital_list.append(capital.group(1))
        print(country.group(1), capital.group(1))
with open('data.csv','w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow([str("Countries"),str("Capitals")])
    for point in range(len(country_list)):
        csvwriter.writerow([country_list[point],capital_list[point]]) #writing all the list data to the csv file where Country and Capitals are the columns







