import sys
sys.path.append("..")
sys.path.append("../VoicChatRobot")
#import VoiceChatRobot.chatBot_module as m
from VoiceChatRobot.chatBot_module import chatBot_module as m
import re

def bot_speak_re(sentence):
    s1 = re.sub(r"\\[[^\\]*\\]", "", sentence)
    print(s1)
    en_list = re.findall(r"[a-zA-z]+", s1)
    s2 = re.sub(r"[a-zA-z \-]+", "@English@", s1)
    all_list = s2.split("@")
    index = 0
    for text in all_list:
        if text != "English":
            m.run_bot_speak(text, "zh-tw")
        else:
            m.run_bot_speak(en_list[list], "en")
            index += 1

if __name__ == "__main__":
    sentence = """
    阿爾伯特·愛因斯坦（德語：Albert Einstein，1879年3月14日－1955年4月18日，是出生於德國、擁有瑞士和美國國籍的猶太裔理論物理學家。[6]
    """

    bot_speak_re(sentence)