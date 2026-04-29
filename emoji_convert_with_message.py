

#date :- 29.04.2026
#Author :- Konik Rahman
# Email:- konikrahman06@gmail.com

#First python program: get the message from user with special sign, print these message with emoji, convert the special sign in emoji.

# example- smile :) - 😊, crying face :( - 🥲 etc

user_message = input("> ")

# splite this message.

words = user_message.split()

# creating a dictationary.

emojiDict = {
    ":(": "🥲",
    ":)": "😊"
}
output = " "
for word in words:
    output += emojiDict.get(word, word) + " "

print(output)

print("========@@@@@=======")
print("     Konik Rahman")
print("========@@@@@=======")


# ===End===