import os
from pygame import mixer
from gtts import gTTS

mixer.init()
if not os.path.isfile("tmp.mp3"):
    tts = gTTS(text="我是豬豬惠晴", lang="zh-tw")
    tts.save("tmp.mp3")
    print("已生成不重要的語音檔.mp3")

def bot_speak(text, lang):
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


if __name__ == "__main__":
    bot_speak("我是豬豬惠晴, 快打我", "zh-tw")