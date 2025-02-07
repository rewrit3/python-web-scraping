from urllib.request import urlopen
from bs4 import BeautifulSoup

def write_to_text(filename, content):
  try:
    with open(filename, 'w', encoding='utf-8') as file:
      file.write(content)
  except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

url = 'https://rewrite.com.br/'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

write_to_text('scrape2.txt', soup.select('h1')[0].text.strip())

print(soup.select('h1')[0].text.strip())