import sqlite3

import requests
from bs4 import BeautifulSoup

def get_price(code):
    url = "https://finance.naver.com/item/main.naver?code="+code
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    today = soup.find('div', {'class':'today'})
    price = today.find('em').find('span', {'class': 'blind'}).text
    price = price.replace(',', '')
    return price
if __name__=='__main__':
    # kospi의 전체 종목의 현재 가격을 출력하시오
    print(get_price('005930'))
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM stock WHERE market='KOSPI'")
    rows = cur.fetchall() # 전체 한개 fetchall(), 몇몇 fetchmany(3)
    conn.close()
    for row in rows:
        print(get_price(row[0]), row[1])