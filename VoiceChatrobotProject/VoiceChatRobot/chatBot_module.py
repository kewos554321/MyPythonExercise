import os
import re
import sys
import speech_recognition as sr
import requests
from pygame import mixer
from gtts import gTTS
from bs4 import BeautifulSoup
from hanziconv import HanziConv

def bot_listen():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        audioData = recog.listen(source)
    try:
        text = recog.recognize_google(audioData, language="zh-tw")
        return text
    except:
        return("unknow")

def bot_speak(text, lang):
    mixer.init()
    print(os.getcwd())
    if not os.path.isfile("tmp.mp3"):
        tts = gTTS(text="我是豬豬惠晴", lang="zh-tw")
        tts.save("tmp.mp3")
        print("已生成不重要的語音檔.mp3")

    try:
        mixer.music.load("tmp.mp3")
        tts = gTTS(text=text, lang=lang)
        tts.save("speak.mp3")
        mixer.music.load("speak.mp3")
        mixer.music.play()
        while(mixer.music.get_busy()):
            continue
    except:
        print("fail!")

def bot_speak_re(sentence):
    s1 = re.sub(r"\[.*?\]", "", sentence)
    s1 = re.sub(r"\（.*?\）", "", s1)
    en_list = re.findall(r"[a-zA-z]+", s1)
    s2 = re.sub(r"[a-zA-z]+", "@English@", s1)
    print(s2)
    all_list = s2.split("@")
    print(all_list)
    index = 0
    for text in all_list:
        if text != "English":
            bot_speak(text, "zh-tw")
        else:
            print(en_list)
            bot_speak(en_list[index], "en")
            index += 1

def bot_get_wiki(keyword):
    response = requests.get("https://zh.wikipedia.org/zh-tw/" + keyword)

    bs = BeautifulSoup(response.text, "lxml")
    
    p_list = bs.find_all("p")
    for p in p_list:
        print(p)
        if keyword in p.text[0:10]:
            return p.text

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
    sentence = "阿爾伯特·愛因斯坦（德語：Albert Einstein），for test."
    bot_speak_re(sentence)