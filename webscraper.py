from bs4 import BeautifulSoup
import requests
import re
import ezsheets

""" headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'}

search_term = input("What game do you want to search for? ")
console_type = input("What console would you like the game to be on? (Steam, XBOX, PSN) ")

match console_type.upper():
  case "STEAM":
    url = f"https://www.g2a.com/category/gaming-c1?f%5Bdrm%5D%5B0%5D=1&query={search_term}"
  case "XBOX":
    url = f"https://www.g2a.com/category/gaming-c1?f%5Bdrm%5D%5B0%5D=273&query={search_term}"
  case "PSN":
    url = f"https://www.g2a.com/category/gaming-c1?f%5Bdrm%5D%5B0%5D=8586&query={search_term}"
  case _:
    print("Invalid console type.")

page = requests.get(url, headers=headers).text
doc = BeautifulSoup(page, "html.parser")

div = doc.find(class_="indexes__ContentWrapper-wklrsw-95 epaecL")

if div is None:
  print("No results found for ", search_term.title(), " on ", console_type.upper(), "...", sep="")
else:
  sections = div.findAll(class_="sc-gIvpjk kgKIqe indexes__StyledProductBox-wklrsw-104 bRdNCV productCard")
  print("Results for ", search_term.title(), " on ", console_type.upper(), ":\n", sep="")
  
  for section in sections:
    title = section.find(string=re.compile(search_term, re.IGNORECASE))
    display_title = title.split(' - ')[0]

    price = section.find(class_="sc-iqAclL sc-crzoAE dJFpVb eqnGHx sc-bqGGPW gjCrxq")
    display_price = price.text.replace(" ", "")

    print(display_title, display_price, sep=" => ") """

ss = ezsheets.Spreadsheet('14Ctq_SMhvEwsTJb7FP-sSjgZr5Cwck5MImXL9Lty3js')
