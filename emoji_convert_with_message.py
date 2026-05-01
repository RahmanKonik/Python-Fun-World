

#date :- 29.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: get the message from user with special sign, print these message with emoji, convert the special sign in emoji.

# example- smile :) - 😊, crying face :( - 🥲 etc


# creating a reuseable function.

def emoji_convertor(user_message):
    # splite this message.

    words = user_message.split()

    # creating a dictationary.

    emojiDict = {
        ":(": "🥲",
        ":)": "😊",
        ":D": "😄",
        ":P": "😛",
        ";)": "😉",
    # cool & fun emoji
        "B)": "😎",
        "8-)": "😎",
        "XD": "😂",
        "xD": "😂",
        ":O": "😮",
        ":-O": "😮"
    }
    output = " "
    for word in words:
        output += emojiDict.get(word, word) + " "
    return output


user_message = input("> ")
result =  emoji_convertor(user_message)
print(result)

print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===