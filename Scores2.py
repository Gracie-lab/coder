print('Enter dot(.) after last score')
score_str = input('please enter score: ')
score_list = []
while score_str != '.' :
        score = int(score_str)
        score_list.append(score)
        score_str = input('Please enter score: ')

minimum = min(score_list)
maximum = max(score_list)
average = sum(score_list)/len(score_list)
total = sum(score_list)
print('Minimun score: ', minimum)
print('Maximum score: ', maximum)
print('Average score: ', average)
print('Total score: ', total)

