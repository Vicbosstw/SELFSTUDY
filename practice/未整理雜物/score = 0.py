score = 0
def func():
    score = 1  
    print(score)
func()
print(score)

score = 0
def add_score():
    global score
    score += 1
    print(score)    
add_score()
print(score)