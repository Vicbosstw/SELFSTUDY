num = 500
while 500<= num <=1000:
    if num%3==2 and num%5==3 and num%7==2:
        print('Man maybe has', str(num), 'Girlfriends')    
    num+=1
print('Other Ans')
for num in range(500,1000):
    if num%3==2 and num%5==3 and num%7==2:
        print('Man maybe has', str(num), 'Girlfriends') 
print('Other Ans')
[print('Man maybe has', i, 'Girlfriends') for i in range(500,1000) if i%3==2 and i%5==3 and i%7==2]