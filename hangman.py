import random

def hangman(word):
    wrong = 0
    stages = ["",
            "__________          ",
            "|                   ",
            "|         |         ",
            "|         0         ",
            "|        /|\        ",
            "|        / \        ",
            "|                   "
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1もじをよそうしてね --> "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else :
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたのかち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたのまけ！せいかいは{}.".format(word))

#answers = ["らんたろう", "きりまる", "しんべえ", "しょうざえもん", "きさんた", "きんご", "だんぞう", "とらわか", "へいだゆう", "さんじろう", "いすけ"]
#answers = ["ふしきぞう", "あやかしまる", "へいた", "まごじろう"]
#answers = ["もんじろう", "せんぞう", "ちょうじ", "こへいた", "いさく", "とめさぶろう"]
answers = ["たきやしゃまる", "きはちろう", "みきえもん", "しゅいちろう", "たかまる", "とめさぶろう"]

hangman(answers[random.randrange(0,len(answers))])
