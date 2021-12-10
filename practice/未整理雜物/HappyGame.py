print('Happy Game',)
score = 0
def wanna(guess,ans):
    global score
    if guess == ans:
        print('GOOD JOB!')
        score +=1
    else: 
        print('Loser!')
q1 = input('倪睿謙讀什麼大學?(四個字)，請作答：')
wanna(q1,'慈濟大學')
q2 = input('倪睿謙讀什麼科系?(三個字)，請作答：')
wanna(q2,'護理系')
q3 = input('倪睿謙幾月幾號出生?(以XXXX作為答案，如0229，請作答：')
wanna(q3,'1019')
print('您得到了',str(score), '分，還不賴嘛')
input('press Enter to exit')