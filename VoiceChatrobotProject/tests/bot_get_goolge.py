import requests
from bs4 import BeautifulSoup
from hanziconv import HanziConv

def bot_get_google(question):
    url = f"https://www.google.com.tw/search?q={question}+維基百科"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/70.0.3538.102 Safari/537.35"
    }    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, "lxml")
        wiki_url = bs.find("cite")
        kwd = wiki_url.text.split("/")[-1]
        kwd = kwd.split(" › ")[-1]
        kwd_trad = HanziConv.toTraditional(kwd)
        return kwd_trad
    else:
        print("fail!")

if __name__ == "__main__":
    keyword = bot_get_google("愛因斯坦")
    print(keyword)







