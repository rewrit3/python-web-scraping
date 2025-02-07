from bs4 import BeautifulSoup
from urllib.request import urlopen

# url = "http://olympus.realpython.org/profiles/dionysus"
url = "https://rewrite.com.br/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
print(soup.find_all("h1"))