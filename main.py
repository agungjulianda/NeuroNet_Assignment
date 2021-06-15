import time
from inputimeout import inputimeout, TimeoutOccurred

confirm_entity = None
recommendation_score_entity = None
repeat_entity = None
recommendation_entity = None
wrong_time_entity = None
question_entity = None
Tag = None


def warn_msg():
    print("Conversation will end in 10 seconds if there is no answer")


def hello(username):
    print(username, ", good afternoon! You are concerned about Company X, we are conducting a survey of satisfaction with our services. Tell me, is it convenient for you to talk now?")
    time.sleep(3)
    hello_null()


def hello_repeat():
    print("This is Company X,  Tell me, is it convenient for you to talk now?")
    recommend_main()


def hello_null():
    print("Sorry, I can't hear you. Could you repeat please?")
    print(
        "Chose one answere",
        "\n",
        "1.Yes",
        "\n",
        "2.No",
        "\n",
        "3.I am Busy",
        "\n",
        "4.Once Again")
    warn_msg()
    global confirm_entity, wrong_time_entity, repeat_entity
    try:
        ans = inputimeout(prompt='Chose your answere :', timeout=10)
        if ans == "1":
            recommend_main()
            confirm_entity = True
        elif ans == "2":
            hangup_wrongtime()
            confirm_entity = False
        elif ans == "3":
            hangup_wrongtime()
            wrong_time_entity = True
        elif ans == "4":
            hello_repeat()
            repeat_entity = True
        else:
            print("WRONG INPUT!!!")
            hangup_null()
    except TimeoutOccurred:
        hangup_null()


def recommend_main():
    print("Tell me, are you ready to recommend our company to your friends? Please rate it on a scale from 0 to 10, where 0 - I will not recommend it, 10 - I will definitely recommend it.")
    recommend_null()


def recommend_null():
    global recommendation_entity
    print("Sorry, I can't hear you. Could you repeat please?")
    print("1.Yes", "\n", "2.Hang Up")
    try:
        ans = inputimeout(prompt='Chose you answere : ', timeout=5)
        if ans == "1":
            recommendation_entity = "Positive"
            recommend_score_positive()
        else:
            hangup_null()
    except TimeoutOccurred:
        recommend_default()


def recommend_default():
    global recommendation_entity, question_entity, repeat_entity
    print(
        "Could You Repeat please",
        "\n",
        "1.Once Again",
        "\n",
        "2.I don't know",
        "\n",
        "3.I am Busy",
        "\n",
        "4.Question")
    warn_msg()
    try:
        ans = inputimeout(prompt='Chose you answere : ', timeout=10)
        if ans == "1":
            repeat_entity = True
            recommend_repeat()
        elif ans == "2":
            recommendation_entity = "dont_know"
            recommend_repeat2()
        elif ans == "3":
            wrong_time_entity = True
            hangup_wrongtime()
        elif ans == "4":
            question_entity = True
            forward()
        else:
            print("WRONG INPUT!!!")
    except TimeoutOccurred:
        hangup_null()


def recommend_repeat():
    print("How would you rate the opportunity to recommend our company to your friends on a scale from 0 to 10, where 0 - I will definitely not recommend it, 10-I will definitely recommend it.")
    recommend_default()


def recommend_repeat2():
    global recommendation_score_entity
    print("Well, if you were asked to recommend our company to friends, would you do it? If yes - then the score is 10, if exactly no - 0.")
    score = input("Please enter your score:")
    recommendation_score_entity = score
    hangup_negative()


def recommend_score_positive():
    global recommendation_entity
    print("Well, on a 10-point scale, how would you rate 8-9 or maybe 10 ?")
    print("1.Maybe", "\n", "2.Hang Up")
    ans = input("Chose your answere :")
    if ans == "1":
        recommendation_entity = "Neutral"
        recommend_score_neutral()
    else:
        hangup_null()


def recommend_score_neutral():
    global recommendation_entity
    print("Well, from 0 to 10, how would you rate it ?")
    print("1.No", "\n", "2.Hang Up")
    answere = input("Chose your answere :")
    if answere == "1":
        recommendation_entity = "Negative"
        recommend_score_negative()
    else:
        hangup_null()


def recommend_score_negative():
    global recommendation_score_entity
    print("Well, from 0 to 10, how would you rate: 0, 5 or maybe 7 ?")
    answere = int(input("Pelase enter your score :"))
    if answere >= 9:
        recommendation_score_entity = answere
        hangup_positive()
    else:
        print("WRONG ANSWERE!!!")
        recommend_score_negative()


def hangup_null():
    global Tag
    print("I can't hear you anyway, so I'd better call you back. All the best to you")
    Tag = "Problem with understanding"


def hangup_wrongtime():
    global Tag
    print("I'm sorry to bother you. All the best to you")
    Tag = "No time to talk"


def hangup_positive():
    global Tag
    print("Great! Thank you so much for your time! All the best to you!")
    Tag = "High score"


def hangup_negative():
    global Tag
    print("I understand you. In any case, thank you so much for your time! All the best to you.")
    Tag = "Low Score"


def forward():
    global Tag
    print("To understand your question, I will switch the call to my colleagues. Please stay on the line.")
    Tag = "Transfer to the operator"


if __name__ == '__main__':

    name = input("Please enter you name :")
    hello(name)
    print("\nConversation report")
    print("Confirm Entity: {}\nRecommendation Entity: {}\nRepeat Entity: {}\nWrong Time Entity: {}\nRecommendation Scroe: {}\nQuestion Entity: {} \nTag: {}".format(
        confirm_entity, recommendation_entity, repeat_entity, wrong_time_entity, recommendation_score_entity, question_entity, Tag))
