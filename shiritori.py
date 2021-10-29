
# https://open.kattis.com/problems/shiritori

n = int(input())

prev_word = input()
called_words = set([prev_word])
has_winner = False

for i in range(n-1):
    word = input()
    if (word[0] != prev_word[-1]) or (word in called_words):
        has_winner = True
        print(f"Player {(i+1)%2 + 1} lost")
        break
    called_words.add(word)
    prev_word = word


if has_winner:
    pass
else:
    print("Fair Game")
