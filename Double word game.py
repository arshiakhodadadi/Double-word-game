def word_game():
    # Play the first turn: 0, play the second turn: 1
    turn = 0
    round = 0
    repeated_words = []
    while True:
        if turn == 0 and round == 0:
            question0 = input().strip()
            turn = 1
            round +=1
            repeated_words.append(question0)

        elif turn == 1 and round != 0:
            question1 = input().strip()
            if question1[0] == question0[-1][-1] and question1 not in repeated_words:
                turn = 0
                round +=1
                repeated_words.append(question1)
            else:
                print("you lost :",round) 
                break
        elif turn == 0 and round != 0:
            question0 = input().strip()
            if question0[0] == question1[-1][-1] and question0 not in repeated_words:
                turn = 1
                round +=1
                repeated_words.append(question0)
            else:
                print("you lost :",round)
                break
word_game()


