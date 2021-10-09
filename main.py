from bs4 import BeautifulSoup
import requests
import csv

#url = 'http://www.diablo1.ru/diablo2game/runes.php'

#req = requests.get(url)

#src = req.text

#with open("index.html", "w", encoding='utf-8') as file:
#    file.write(src)

with open("index.html", encoding = "utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

table = soup.find(style ="border-collapse: collapse; width: 90%; text-align:center;").find("tbody").find_all("tr")

for i in table:
    table1 = i.find_all("td")

    title = table1[1].text
    svois_weapon = table1[2].text
    svois_armor = table1[3].text
    lvl = table1[4].text
    with open(f"data.csv", "a", encoding="utf-8") as file:
       writer = csv.writer(file,delimiter=";", lineterminator='\n')
       writer.writerow(
       [
            title,
            svois_weapon,
            svois_armor,
            lvl
        ]
       )