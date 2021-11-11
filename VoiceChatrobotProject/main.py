import VoiceChatRobot.chatBot_module as m
import sys

question = ""
answer = ""
QA = {
    "你是誰": "我是豬豬惠晴", 
    "unknow": "請再說一次"
}

#question = m.bot_listen()
print(question)
question = "愛因斯坦"
if question in QA:
    answer = QA[question]
    m.bot_speak(answer, "zh-tw")
else:
    keyword = m.bot_get_google(question)
    content = m.bot_get_wiki(keyword)
    if content != None:
        m.bot_speak_re(content)
    else:
        m.bot_speak_re("No answer")