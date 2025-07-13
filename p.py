def minion_game(string):
    stu = kev = 0
    vow = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in vow:
            kev += len(string) - i
        else:
            stu += len(string) - i
    
    print(f"Stuart {stu}" if stu > kev else f"Kevin {kev}" if kev > stu else "Draw")

s = input()
minion_game(s)