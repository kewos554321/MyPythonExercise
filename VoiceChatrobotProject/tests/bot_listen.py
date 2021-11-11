import speech_recognition as sr
import sys
def bot_listen():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        audioData = recog.listen(source)
    try:
        text = recog.recognize_google(audioData, language="zh-tw")
        return text
    except:
        return("unknow")

if __name__ == "__main__":
    question = bot_listen()
    print(question)
