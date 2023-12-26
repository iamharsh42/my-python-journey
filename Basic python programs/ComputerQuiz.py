print('Welcome to Computer Quiz!')
playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    print('Game Over!')
    quit()
else:
    print("Let's start playing!")

score = 0


answer = input("What does RAM stand for: ")
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does ROM stand for: ")
if answer.lower() == 'read only memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does CPU stand for: ")
if answer.lower() == 'central processing memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does GPU stand for: ")
if answer.lower() == 'graphic processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('Game Over!')
print('Your score is '+ str(score)+"/4")