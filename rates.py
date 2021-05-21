from bs4 import BeautifulSoup
import requests

def fetch_bitcoin():
    url = "https://www.coingecko.com/en/coins/bitcoin"
    headers = {'User-Agent' : 'Mozilla/5.0'}
    bitcoin_file = requests.get(url)

    # Создаём soup-объект
    soup = BeautifulSoup(bitcoin_file.text, "html.parser")

    bitcoin_li = []

    # Извлекаем необходимые данные из тегов
    for table in soup.find_all("table", attrs={"class" : "table b-b"}):
        for td in table.find_all("td"):
            bitcoin_li.append(td.text)
    
    # print(bitcoin_li)

    del bitcoin_li[2:]

    # Убираем ненужные символы из элементов списка
    bitcoin_li = map(lambda s : s.strip(), bitcoin_li)
    # print(*bitcoin_li)
    return bitcoin_li
